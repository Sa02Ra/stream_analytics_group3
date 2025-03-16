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
  "event_id": "string",
  "timestamp": "string",
  "event_type": "string",
  "passenger_id": "string",
  "driver_id": ["null", "string"],
  "pickup_location": "string",
  "dropoff_location": ["null", "string"],
  "status": "string",
  "fare": ["null", "float"],
  "surge_multiplier": ["null", "float"],
  "traffic_condition": ["null", "string"],
  "vehicle_type": "string"
}
```



## Author  

Developed by **Anna Picolli, Antoni Heresi, Hugo Suarez, Louisa Schiefer, Saleh Haidar and Sara Baldovino**
