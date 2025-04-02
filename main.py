from fastapi import FastAPI, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
import httpx
import os

app = FastAPI()

REGION_NAME = os.getenv("REGION_NAME", "undefined")
NODE_LIST = os.getenv("CLUSTER_NODES", "").split(",")

cluster_status_gauge = Gauge('heartbeat_cluster_status', 'Cluster-wide health status (1 = healthy, 0 = unhealthy)', ['region'])

@app.get("/health")
async def health_check():
    healthy = False
    async with httpx.AsyncClient(timeout=2.0) as client:
        for node in NODE_LIST:
            try:
                res = await client.get(f"http://{node}/heartbeat")
                if res.status_code == 200:
                    healthy = True
                    break
            except Exception:
                continue
    cluster_status_gauge.labels(region=REGION_NAME).set(1 if healthy else 0)
    return Response(status_code=200 if healthy else 503)

@app.get("/heartbeat")
def heartbeat():
    return Response("OK", status_code=200)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
