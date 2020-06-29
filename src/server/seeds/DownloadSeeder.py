import random
import json
from datetime import datetime, timedelta
import requests
from pprint import pprint

MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoibW1pZHUiLCJhIjoiY2tidzA1c2QyMDhuZzMwbGJiZnRjdDR4NCJ9.ju4H1Kr-i794PCLtkBYOgg'

class DownloadSeeder():
	def __init__(self, id):
		self.latitude = random.uniform(-90, 90)
		self.longitude = random.uniform(-180, 180)
		self.app_id = random.random() > 0.5 and "IOS_ALERT" or "IOS_MATE"
		self.downloaded_at = random.uniform(datetime.today().timestamp(), (datetime.today() + timedelta(days = 1)).timestamp()) * 1000

		res = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/{},{}.json?types=country&access_token={}".format(self.longitude, self.latitude, MAPBOX_ACCESS_TOKEN)).json()

		self.country = res['features'] and res['features'][0]['text'] or 'NA'
		self.id = id

	def __str__(self):
		return json.dumps({
			"id": self.id,
			"latitude": self.latitude,
			"longitude": self.longitude,
			"app_id": self.app_id,
			"downloaded_at": self.downloaded_at,
			"country": self.country
		})
