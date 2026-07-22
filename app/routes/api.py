from flask import Blueprint, jsonify
from datetime import date, timedelta, datetime
import random

api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)

doctors = [
    {
        "id": 1,
        "name": "Dr. Carlos Mendes",
        "specialty": "Cardiologia"
    },
    {
        "id": 2,
        "name": "Dra. Ana Silva",
        "specialty": "Dermatologia"
    },
    {
        "id": 3,
        "name": "Dr. João Souza",
        "specialty": "Ortopedia"
    }
]

patients = [
    {
        id: 1,
        "name": "John Silva",
        "cpf": "123.456.789-00",
        "insurance": "Unimed"
    },
    {
        id: 2,
        "name": "Mary Oliveira",
        "cpf": "987.654.321-00",
        "insurance": "Amil"
    },
    {
        id: 3,
        "name": "Carlos Pereira",
        "cpf": "456.789.123-00",
        "insurance": "Bradesco Health"
    },
    {
        id: 4,
        "name": "Ana Souza",
        "cpf": "789.123.456-00",
        "insurance": "SulAmérica"
    },
    {
        id: 5,
        "name": "Peter Santos",
        "cpf": "321.654.987-00",
        "insurance": "Hapvida"
    }
];

@api.route("/availability/<int:doctor_id>")
def availability(doctor_id):
    today = date.today()

    slots = []
    for hour in ["08:00", "09:00", "10:00", "14:00", "15:00"]:
        day = today + timedelta(days=1)
        appointment = {
            "doctor_id": doctor_id,
            "date": day.isoformat(),
            "time": hour,
            "availability": random.choice([True, False])
        }
        slots.append(appointment)

    return jsonify({
        "success": True,
        "data": slots
    })

@api.route("/appointments")
def appointment():
    today = date.today()
    slots = []
    current_hour = datetime.now().strftime("%H:%M")
    for doctor in doctors:
        for hour in ["08:00", "09:00", "10:00", "14:00", "15:00"]:
            status = random.choice(["Cancelada", "Agendada"]) if hour > current_hour else random.choice(["Cancelada", "Atendido"])
            day = today + timedelta(days=1)
            patient = random.choice(patients)
            appointment = {
                "doctor_name": doctor["name"],
                "specialty": doctor["specialty"],
                "patient_name": patient["name"],
                "patient_cpf": patient["cpf"],
                "patient_insurance": patient["insurance"],
                "date": day.isoformat(),
                "time": hour,
                "availability": status
            }
        
            slots.append(appointment)
    
    
    return jsonify({
        "success": True,
        "data": slots
    })
    