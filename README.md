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



## Authors  

Developed by **Anna Picolli, Antoni Heresi, Hugo Suarez, Louisa Schiefer, Saleh Haidar and Sara Baldovino**
