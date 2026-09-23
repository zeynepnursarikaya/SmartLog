from .services.anomaly import detect_anomaly
from typing import Optional
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_db
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartLog API")


@app.get("/")
def root():
    return {"message": "SmartLog API çalışıyor"}


@app.post("/telemetry", response_model=schemas.TelemetryResponse)
def create_telemetry(data: schemas.TelemetryCreate, db: Session = Depends(get_db)):
    # Aynı cihazın geçmiş sıcaklık değerlerini çek
    past_temps = [
        row.temperature
        for row in db.query(models.TelemetryData)
        .filter(models.TelemetryData.device_id == data.device_id)
        .all()
    ]

    is_anomaly = detect_anomaly(data.temperature, past_temps)

    db_record = models.TelemetryData(
        device_id=data.device_id,
        temperature=data.temperature,
        cpu_usage=data.cpu_usage,
        memory_usage=data.memory_usage,
        is_anomaly=int(is_anomaly),
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


@app.get("/telemetry", response_model=List[schemas.TelemetryResponse])
def list_telemetry(
    skip: int = 0,
    limit: int = 100,
    device_id: Optional[str] = None,
    only_anomalies: bool = False,
    db: Session = Depends(get_db),
):
    query = db.query(models.TelemetryData)

    if device_id:
        query = query.filter(models.TelemetryData.device_id == device_id)
    if only_anomalies:
        query = query.filter(models.TelemetryData.is_anomaly == 1)

    return query.offset(skip).limit(limit).all()
@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(models.TelemetryData).count()
    anomalies = db.query(models.TelemetryData).filter(models.TelemetryData.is_anomaly == 1).count()

    return {
        "total_records": total,
        "anomaly_count": anomalies,
        "anomaly_rate": round(anomalies / total, 3) if total > 0 else 0,
    }