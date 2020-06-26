import random
import json
from datetime import datetime, timedelta

class DownloadSeeder():
	def __init__(self, id):
		self.id = id

	@property
	def latitude(self):
		return random.uniform(-90, 90)

	@property
	def longitude(self):
		return random.uniform(-180, 180)

	@property
	def app_id(self):
		return random.random() > 0.5 and "IOS_ALERT" or "IOS_MATE"

	@property
	def downloaded_at(self):
		return random.uniform(datetime.today().timestamp(), (datetime.today() + timedelta(days = 1)).timestamp()) 

	def __str__(self):
		return json.dumps({
			"id": self.id,
			"latitude": self.latitude,
			"longitude": self.longitude,
			"app_id": self.app_id,
			"downloaded_at": self.downloaded_at
		})
