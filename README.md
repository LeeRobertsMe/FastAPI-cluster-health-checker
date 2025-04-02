# 🚀 Cluster Health Template

A clean, production-ready Docker setup for running cluster health checks with FastAPI — designed for Cloudflare Load Balancing and Prometheus integration.

This template provides a smart and lightweight foundation for regional node health monitoring with:

- FastAPI microservice
- Docker & Docker Compose
- `/health` endpoint for Cloudflare
- `/metrics` endpoint for Prometheus (optional NOC integration)
- Cluster-wide status check logic
- `.env` driven config

---

## 🧱 Stack

- App: FastAPI (Python 3.11)
- Monitoring: Prometheus-compatible `/metrics`
- Containerisation: Docker + Docker Compose

---

## 🛠️ Usage

### 1. Clone the Template

```bash
git clone https://github.com/your-username/cluster-health-template your-cluster-health
cd your-cluster-health
```

### 2. Environment Setup

```bash
cp .env.example .env
```

Edit `.env` to define your cluster region name and node list:

```
REGION_NAME=eu
CLUSTER_NODES=eu-01:8000,eu-02:8000,eu-03:8000
```

---

## 📂 Folder Structure

- `.env.example`
- `.gitignore`
- `Dockerfile`
- `docker-compose.yml`
- `main.py`
- `requirements.txt`

---

## ⚙️ Endpoints

| Path         | Purpose                                                              |
| ------------ | -------------------------------------------------------------------- |
| `/health`    | Cloudflare health check (200/503 based on cluster)                   |
| `/heartbeat` | Individual node heartbeat check                                      |
| `/metrics`   | Prometheus-compatible output (scraped by NOC-level Prometheus later) |

---

## ✅ Features

- Cluster-aware logic
- Centralised health check via FastAPI
- Prometheus metrics ready
- Minimal footprint
- Cleanly structured for use in any stack
- MIT License

---

## 🧑‍💻 Author

Lee Roberts — https://github.com/LeeRobertsMe

---

## 🤝 Contributing

1. Fork
2. Create a branch
3. Commit changes
4. PR with clear description

---

## 📜 License

MIT License — see `LICENSE` file.

---
