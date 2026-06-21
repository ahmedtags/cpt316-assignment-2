# CPT316 - Programming Language Implementation and Paradigms (Assignment 2)

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
