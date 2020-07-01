from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from utils.database.RedisClient import Redis
from seeds import seeds
from controllers import DownloadsController
from seeds.DownloadSeeder import DownloadSeeder
import json
import os

app = FastAPI()

@app.get("/api")
def read_root():
	return {"app": {"version": "0.01"}}


@app.get("/downloads")
def get_downloads():
	downloadsController = DownloadsController.DownloadsController()
	return downloadsController.get()


@app.get("/seed")
def seed_redis():
	Redis.client.flushdb()
	seeder = seeds.Seeder()
	seeder.run()
	return {"status": "ok"}

@app.get("/")
def redirect():
	return RedirectResponse(url="/index.html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
	await websocket.accept()
	while True:
		data = await websocket.receive_text()
		downloadsController = DownloadsController.DownloadsController()
		download = downloadsController.new()
		await websocket.send_json({"msg": download})

app.mount("/", StaticFiles(directory="../client/build"), name="client")