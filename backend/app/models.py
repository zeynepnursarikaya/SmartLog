from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from .database import Base #bir önceki dosyada tanımladığımız Base sınıfını içeri alıyoruz (. işareti "aynı klasördeki" anlamına geliyor)


class TelemetryData(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    temperature = Column(Float)
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    is_anomaly = Column(Integer, default=0)