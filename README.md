# SmartLog

Telemetry Monitoring & Anomaly Detection API — sistemlerden gelen sıcaklık, CPU ve bellek kullanımı gibi ölçümleri toplayan, saklayan ve anormal değerleri tespit eden bir backend sistemi.

## Teknoloji Yığını

- **FastAPI** — REST API
- **SQLAlchemy + SQLite** — veri katmanı
- **Pydantic** — veri doğrulama

## Kurulum

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
```

## Çalıştırma

```bash
uvicorn backend.app.main:app --reload
```

API dokümantasyonu: `http://127.0.0.1:8000/docs`

## Endpoint'ler

| Method | Endpoint      | Açıklama                          |
|--------|---------------|------------------------------------|
| GET    | `/`           | Sağlık kontrolü                    |
| POST   | `/telemetry`  | Yeni telemetri kaydı oluşturur     |
| GET    | `/telemetry`  | Kayıtları listeler (pagination'lı) |

## Yol Haritası

- [x] Backend + veritabanı iskeleti
- [ ] İstatistiksel anomali tespiti
- [ ] Test coverage
- [ ] Docker desteği

## Lisans

MIT