import time
import json
import requests
from config.app import MAPBOX_ACCESS_TOKEN
from utils.database.RedisClient import Redis

class Download():
	def __init__(self, latitude, longitude, app_id):
		self.id = Redis.client.scard("downloads") + 1
		self.latitude = latitude
		self.longitude = longitude
		self.app_id = app_id
		self.downloaded_at = int(time.time())

	@property
	def country(self):
		res = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/{},{}.json?types=country&access_token={}".format(self.longitude, self.latitude, MAPBOX_ACCESS_TOKEN)).json()
		return res['features'] and res['features'][0]['text'] or 'NA'

	def to_json(self):
		return {
			"id": self.id,
			"latitude": self.latitude,
			"longitude": self.longitude,
			"app_id": self.app_id,
			"downloaded_at": self.downloaded_at,
			"country": self.country
		}

	def __str__(self):
		return json.dumps(self.to_json())
