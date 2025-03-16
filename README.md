# stream_analytics_group3
Stream Analytics Final Group Project - Group 3

# Ride-Hailing Event Generator

This repository contains a Python-based **Ride-Hailing Event Generator** that simulates ride-hailing activity, generating event data in **JSON** and **AVRO** formats. The data includes **passenger requests, ride statuses, fares, and traffic conditions**, making it useful for analytics, data science, and machine learning applications.  


## Features  
**Generates realistic ride-hailing events**  
**Creates JSON and AVRO files for easy data consumption**  
**Simulates peak-hour demand**  
**Flask API for downloading generated data**  
**Customizable event count via CLI**  
**Includes surge pricing & traffic conditions**  

## Objectives
The project aims to:
**Develop a Data Generator to simulate ride-hailing events.**
**Implement AVRO serialization for structured data storage.**
**Ensure realism and variety in generated data.**
**Allow scalability to simulate varying demand loads.**
**Provide a Flask API to download generated data.**



## How to Run the Project  

### Install Dependencies  

Ensure you have **Python 3.7+** installed, then install the required libraries:  

```
pip install -r requirements.txt
```

OR manually install the dependencies:  

```
pip install json fastavro faker flask argparse logging
```

---

### Run the Data Generator  

To generate **500 ride-hailing events** (default):  

```
python main.py
```

To specify a **custom number of events**, use the `--events` flag:  

```
python main.py --events 1000
```

This will generate **ride_hailing_events.json** and **ride_hailing_events.avro** files in the project directory.  

---

### Download Generated Data via Flask API  

The project also runs a **Flask server** that allows you to download the generated data.  

#### Start the Flask server:  

```
python main.py
```



## Data Schema  

The events follow a **well-defined AVRO schema**, ensuring **structured** and **consistent** data:  

```json
{
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
}
```

## Example Generated Data (JSON)

```json
{
  "event_id": "123e4567-e89b-12d3-a456-426614174000",
  "timestamp": "2025-03-16T12:34:56.789Z",
  "event_type": "passenger_request",
  "passenger_id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6",
  "driver_id": null,
  "pickup_location": "123 Main St, New York, NY",
  "dropoff_location": null,
  "status": "requested",
  "fare": null,
  "surge_multiplier": null,
  "traffic_condition": null,
  "vehicle_type": "economy"
}
```

## Future Improvements
**Enhance event types with driver feedback & trip ratings.**
**Implement Kafka or Azure EventHub for real-time event streaming.**
**Expand data visualization with a dashboard.**

## Authors  

Developed by **Anna Picolli, Antoni Heresi, Hugo Suarez, Louisa Schiefer, Saleh Haidar and Sara Baldovino**

University: **IE University**
