from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from utils.database.RedisClient import RedisClient
from seeds import seeds
from controllers import DownloadsController
from seeds.DownloadSeeder import DownloadSeeder
import json
import os

app = FastAPI()

redis = RedisClient('ds_redis', 6379, 0)



@app.get("/api")
def read_root():
	return {"app": {"version": "0.01"}}


@app.get("/downloads")
def get_downloads():
	downloadsController = DownloadsController.DownloadsController(redis)
	return downloadsController.get()


@app.get("/seed")
def seed_redis():
	redis.client.flushdb()
	seeder = seeds.Seeder(redis)
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
		id = redis.client.scard("downloads") + 1
		download = DownloadSeeder(id)
		redis.client.sadd("downloads", str(download))
		downloadsController = DownloadsController.DownloadsController(redis)
		formatted = downloadsController.format_one(download.toJSON())
		await websocket.send_json({"msg": formatted})

app.mount("/", StaticFiles(directory="../client/build"), name="client")