from pydantic import BaseModel
from datetime import datetime


class TelemetryCreate(BaseModel):
    device_id: str
    temperature: float
    cpu_usage: float
    memory_usage: float


class TelemetryResponse(BaseModel):
    id: int
    device_id: str
    temperature: float
    cpu_usage: float
    memory_usage: float
    timestamp: datetime
    is_anomaly: int

    class Config:
        from_attributes = True









        # TelemetryCreate — bu, kullanıcıdan bize veri gelirken (yani biri API'ye "işte yeni bir ölçüm" diye POST isteği attığında) 
        # beklediğimiz format. Dikkat et: id, timestamp, is_anomaly burada yok — çünkü bunları kullanıcı göndermiyor, sistem kendisi
        # üretiyor (id otomatik artıyor, timestamp otomatik ekleniyor, anomali durumu bizim analizimizle belirleniyor).
        # TelemetryResponse — bu ise bizim kullanıcıya geri gönderdiğimiz veri formatı. Burada tüm alanlar var, çünkü artık veritabanına
        # kaydedilmiş, tam bir kayıt döndürüyoruz.
       