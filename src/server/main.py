from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from utils.database.RedisClient import RedisClient
from seeds import seeds
from controllers import DownloadsController
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
    return RedirectResponse(url="/now-ui-dashboard-react/index.html")


app.mount("/now-ui-dashboard-react", StaticFiles(directory="../now-ui-dashboard-react/build"), name="static")