# energy_monitor_api.py
# CPT316 Assignment 2 - Energy Monitor System
# Python Flask Backend API - FINAL VERSION

from flask import Flask, jsonify, request
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Simulated device data
devices = [
    {"id": 1, "name": "Air Conditioner", "power": 2000, "status": "active"},
    {"id": 2, "name": "Refrigerator", "power": 150, "status": "active"},
    {"id": 3, "name": "TV", "power": 100, "status": "inactive"},
    {"id": 4, "name": "Washing Machine", "power": 500, "status": "inactive"},
    {"id": 5, "name": "Lights", "power": 60, "status": "active"},
    {"id": 6, "name": "computer", "power": 20, "status": "active"}
]

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """Return list of devices with current status"""
    active_devices = [d for d in devices if d['status'] == 'active']
    total_power = sum(d['power'] for d in active_devices)
    
    return jsonify({
        'devices': devices,
        'active_count': len(active_devices),
        'total_power': total_power,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/consumption', methods=['GET'])
def get_consumption():
    """Calculate current power consumption"""
    active_devices = [d for d in devices if d['status'] == 'active']
    current_power = sum(d['power'] for d in active_devices)
    
    # Simulate some variation for realistic data
    current_power += random.randint(-50, 50)
    
    # Calculate daily consumption (kWh)
    daily_consumption = (current_power * 24) / 1000
    
    return jsonify({
        'current_power_watts': current_power,
        'daily_consumption_kwh': round(daily_consumption, 2),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/cost', methods=['GET'])
def get_cost():
    """Calculate electricity cost based on Malaysia rates"""
    active_devices = [d for d in devices if d['status'] == 'active']
    current_power = sum(d['power'] for d in active_devices)
    
    # Malaysia electricity rate (TNB approximate): RM 0.57 per kWh
    rate_per_kwh = 0.57
    
    # Daily consumption in kWh
    daily_kwh = (current_power * 24) / 1000
    
    # Calculate costs
    daily_cost = daily_kwh * rate_per_kwh
    monthly_cost = daily_cost * 30
    yearly_cost = daily_cost * 365
    
    return jsonify({
        'daily_cost_rm': round(daily_cost, 2),
        'monthly_cost_rm': round(monthly_cost, 2),
        'yearly_cost_rm': round(yearly_cost, 2),
        'rate_per_kwh': rate_per_kwh,
        'current_power_watts': current_power,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/toggle/<int:device_id>', methods=['GET', 'POST'])
def toggle_device(device_id):
    """Toggle device on/off"""
    try:
        for device in devices:
            if device['id'] == device_id:
                device['status'] = 'inactive' if device['status'] == 'active' else 'active'
                return jsonify({
                    'success': True,
                    'device': device,
                    'message': f"{device['name']} is now {device['status']}"
                }), 200
        
        return jsonify({
            'success': False, 
            'error': 'Device not found'
        }), 404
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """Get overall energy statistics"""
    active_devices = [d for d in devices if d['status'] == 'active']
    inactive_devices = [d for d in devices if d['status'] == 'inactive']
    
    total_power = sum(d['power'] for d in active_devices)
    potential_power = sum(d['power'] for d in devices)
    
    return jsonify({
        'total_devices': len(devices),
        'active_devices': len(active_devices),
        'inactive_devices': len(inactive_devices),
        'current_power_usage': total_power,
        'max_potential_power': potential_power,
        'efficiency_percentage': round((total_power / potential_power * 100), 2) if potential_power > 0 else 0,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/', methods=['GET'])
def home():
    """API Home/Health Check"""
    return jsonify({
        'message': 'Energy Monitor API is running!',
        'version': '1.0',
        'endpoints': {
            '/api/devices': 'GET - List all devices',
            '/api/consumption': 'GET - Current power consumption',
            '/api/cost': 'GET - Cost calculations',
            '/api/statistics': 'GET - Overall statistics',
            '/api/toggle/<device_id>': 'GET/POST - Toggle device on/off'
        }
    })

if __name__ == '__main__':
    print("="*50)
    print("CPT316 - Energy Monitor API Server")
    print("="*50)
    print("Starting Flask API Server...")
    print("API available at: http://localhost:5000")
    print("Endpoints:")
    print("  - GET  http://localhost:5000/api/devices")
    print("  - GET  http://localhost:5000/api/consumption")
    print("  - GET  http://localhost:5000/api/cost")
    print("  - GET  http://localhost:5000/api/statistics")
    print("  - GET/POST http://localhost:5000/api/toggle/<id>")
    print("="*50)
    print("Press Ctrl+C to stop the server")
    print("="*50)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
