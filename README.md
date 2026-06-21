# CPT316 - Programming Language Implementation and Paradigms (Assignment 2)

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%20%26%20Flask-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Language" />
  <img src="https://img.shields.io/badge/Course-CPT316-24292e?style=for-the-badge" alt="Course" />
  <a href="https://github.com/ahmedtags">
    <img src="https://img.shields.io/badge/Profile-ahmedtags-D9A34A?style=for-the-badge&logo=github&logoColor=white" alt="Profile" />
  </a>
  <a href="https://blxman-37fy.vercel.app/">
    <img src="https://img.shields.io/badge/Portfolio-blxman--37fy-0A66C2?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio" />
  </a>
</p>

---

This repository contains the multi-paradigm system implementation (Node-RED + Python Flask API) and PDF report for **CPT316: Programming Language Implementation and Paradigms - Assignment 2** (Semester 1, Academic Session 2025/2026) at Universiti Sains Malaysia (USM).

## Course Details
- **Course Code:** CPT316
- **Course Name:** Programming Language Implementation and Paradigms
- **Semester:** Semester 1, Year 3 (2025/2026)
- **Project Title:** Smart IoT Energy Monitoring System (Integration of Node-RED and Python API)

---

## Assignment Overview

The assignment requires building an application demonstrating the capability to integrate two different programming paradigms and languages:
1. **Node-RED System (JavaScript Paradigm - Compulsory):**
   - Implements data flow logic, triggers, dashboard visualizations, and message routing.
   - Configured in [`flows.json`](flows.json).
2. **Python Flask API (Python Procedural/OOP Paradigm):**
   - Acts as the backend service handling HTTP API requests, calculating analytics, database operations, or simulation of device energy parameters.
   - Implemented in [`FINAL_energy_monitor_api.py`](FINAL_energy_monitor_api.py).
3. **Integration / Communication:**
   - Communication between Node-RED nodes and Flask API endpoints over HTTP POST/GET requests carrying JSON payloads.

---

## What I Did
- Developed the Python backend Flask service in [`FINAL_energy_monitor_api.py`](FINAL_energy_monitor_api.py) to simulate and monitor IoT energy reading profiles.
- Set up Node-RED visual workflows and dashboard in [`flows.json`](flows.json).
- Documented paradigm comparisons, communication protocol, systems architecture, and testing in the report: [`CPT316_Assignment2_Report_g29.pdf`](CPT316_Assignment2_Report_g29.pdf).
- Consolidated the original assignment guideline: [`CPT316 ASSIGNMENT20252026.pdf`](CPT316%20ASSIGNMENT20252026.pdf).

---

## Tools & Tech Stack
- **Languages:** JavaScript (Node-RED), Python
- **Frameworks:** Node-RED (IoT workflows), Flask (Python Web API)
- **Data Exchange:** JSON payloads over HTTP REST APIs

---

## How to Run

### 1. Flask API Backend
1. Install Python 3.x and dependencies:
   ```bash
   pip install flask flask-cors
   ```
2. Start the API server:
   ```bash
   python FINAL_energy_monitor_api.py
   ```
   The backend runs by default on `http://localhost:5000`.

### 2. Node-RED Setup
1. Install Node-RED globally via npm:
   ```bash
   npm install -g node-red
   ```
2. Start Node-RED:
   ```bash
   node-red
   ```
3. Open Node-RED editor (usually `http://localhost:1880`), select Import from the menu, and upload the [`flows.json`](flows.json) file.
4. Deploy the flow to establish communication with the Python API and view the dashboard.

---

## 📸 Sample API Output

**`GET /api/devices`** — List all monitored devices and current status:
```json
{
  "active_count": 4,
  "devices": [
    {"id": 1, "name": "Air Conditioner", "power": 2000, "status": "active"},
    {"id": 2, "name": "Refrigerator",    "power": 150,  "status": "active"},
    {"id": 3, "name": "TV",              "power": 100,  "status": "inactive"},
    {"id": 4, "name": "Washing Machine", "power": 500,  "status": "inactive"},
    {"id": 5, "name": "Lights",          "power": 60,   "status": "active"},
    {"id": 6, "name": "computer",        "power": 20,   "status": "active"}
  ],
  "timestamp": "2025-11-15T14:32:10.847321",
  "total_power": 2230
}
```

**`GET /api/consumption`** — Real-time power consumption:
```json
{
  "current_power_watts": 2257,
  "daily_consumption_kwh": 54.17,
  "timestamp": "2025-11-15T14:32:12.013455"
}
```

**`GET /api/cost`** — Electricity cost estimation (Malaysia TNB rates):
```json
{
  "current_power_watts": 2230,
  "daily_cost_rm": 30.51,
  "monthly_cost_rm": 915.35,
  "rate_per_kwh": 0.57,
  "timestamp": "2025-11-15T14:32:13.204871",
  "yearly_cost_rm": 11136.86
}
```

> Node-RED dashboard reads these endpoints on a 5-second interval and renders live power gauges and cost charts.
