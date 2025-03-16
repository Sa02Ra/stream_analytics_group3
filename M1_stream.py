import json
import random
import time
import uuid
import logging
import argparse
from datetime import datetime, timezone
import fastavro
from faker import Faker
from flask import Flask, send_file

# Initialize Flask app
app = Flask(__name__)

# Initialize Faker for synthetic data generation
fake = Faker()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Persistent ID lists for realism
active_passengers = [str(uuid.uuid4()) for _ in range(100)] 
active_drivers = [str(uuid.uuid4()) for _ in range(50)]  

# Define AVRO schema for ride-hailing events
avro_schema = {
    "type": "record",
    "name": "RideHailingEvent",
    "fields": [
        {"name": "event_id", "type": "string"},
        {"name": "timestamp", "type": "string"},
        {"name": "event_type", "type": "string"},
        {"name": "passenger_id", "type": "string"},
        {"name": "driver_id", "type": ["null", "string"], "default": None},
        {"name": "pickup_location", "type": "string"},
        {"name": "dropoff_location", "type": ["null", "string"], "default": None},
        {"name": "status", "type": "string"},
        {"name": "fare", "type": ["null", "float"], "default": None},
        {"name": "surge_multiplier", "type": ["null", "float"], "default": None},
        {"name": "traffic_condition", "type": ["null", "string"], "default": None},
        {"name": "vehicle_type", "type": "string"}
    ]
}

def save_avro_schema():
    with open("ride_hailing_schema.avsc", "w") as f:
        json.dump(avro_schema, f, indent=4)

# Fare model based on vehicle type
fare_model = {
    "economy": {"base_fare": 3.0, "per_km": 0.8, "multiplier": 1.0},
    "premium": {"base_fare": 5.0, "per_km": 1.5, "multiplier": 1.3},
    "shared": {"base_fare": 2.0, "per_km": 0.5, "multiplier": 0.85}
}

def calculate_fare(vehicle_type, distance_km, surge_multiplier):
    model = fare_model.get(vehicle_type, fare_model["economy"])
    base = model["base_fare"]
    per_km = model["per_km"]
    mult = model["multiplier"]
    return round((base + per_km * distance_km) * mult * surge_multiplier, 2)

def generate_passenger_request():
    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": "passenger_request",
        "passenger_id": random.choice(active_passengers),
        "driver_id": None,
        "pickup_location": fake.address(),
        "dropoff_location": None,
        "status": random.choice(["requested", "cancelled"]),
        "fare": None,
        "surge_multiplier": None,
        "traffic_condition": None,
        "vehicle_type": random.choice(["economy", "premium", "shared"])
    }

def generate_ride_status():
    status = random.choice(["accepted", "ongoing", "completed", "cancelled"])
    vehicle_type = random.choice(["economy", "premium", "shared"])
    surge_multiplier = round(random.uniform(1.0, 3.0), 2)
    distance_km = round(random.uniform(2, 20), 1) 
    
    fare = calculate_fare(vehicle_type, distance_km, surge_multiplier) if status == "completed" else None
    
    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": "ride_status",
        "passenger_id": random.choice(active_passengers),
        "driver_id": random.choice(active_drivers),
        "pickup_location": fake.address(),
        "dropoff_location": fake.address() if status in ["completed", "ongoing"] else None,
        "status": status,
        "fare": fare,
        "surge_multiplier": surge_multiplier if status == "completed" else None,
        "traffic_condition": random.choice(["green", "orange", "red"]),
        "vehicle_type": vehicle_type
    }

def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def write_avro(data, filename):
    try:
        with open(filename, "wb") as f:
            fastavro.writer(f, fastavro.parse_schema(avro_schema), data)
    except Exception as e:
        logging.error(f"Failed to write AVRO file: {e}")

def generate_and_save_events(event_count=500):
    json_filename = "ride_hailing_events.json"
    avro_filename = "ride_hailing_events.avro"
    
    peak_hours = [7, 8, 9, 17, 18, 19]
    current_hour = datetime.now(timezone.utc).hour
    if current_hour in peak_hours:
        logging.info("Peak hours detected. Generating more ride requests.")
        event_count *= 1.5

    events = [generate_passenger_request() if random.random() < 0.5 else generate_ride_status() for _ in range(int(event_count))]
    logging.info(f"Generated {len(events)} events")
    
    write_json(events, json_filename)
    write_avro(events, avro_filename)
    logging.info(f"Saved events in {json_filename} and {avro_filename}")

@app.route("/download/json")
def download_json():
    return send_file("ride_hailing_events.json", as_attachment=True)

@app.route("/download/avro")
def download_avro():
    return send_file("ride_hailing_events.avro", as_attachment=True)

def main():
    parser = argparse.ArgumentParser(description="Generate ride-hailing event data")
    parser.add_argument("--events", type=int, default=500, help="Number of events to generate")
    args = parser.parse_args()
    
    save_avro_schema()
    generate_and_save_events(args.events)
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
