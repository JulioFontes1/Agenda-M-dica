from app.database import db
from datetime import datetime


class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)

    patient_name = db.Column(
        db.String(100),
        nullable=False
    )

    doctor = db.Column(
        db.String(100),
        nullable=False
    )

    specialty = db.Column(
        db.String(100),
        nullable=False
    )

    date = db.Column(
        db.Date,
        nullable=False
    )

    time = db.Column(
        db.String(5),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="scheduled"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.now()
    )


    def to_dict(self):
        return {
            "id": self.id,
            "patient": self.patient_name,
            "doctor": self.doctor,
            "specialty": self.specialty,
            "date": self.date.isoformat(),
            "time": self.time,
            "status": self.status
        }