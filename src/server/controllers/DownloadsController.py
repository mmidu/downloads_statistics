import json
import datetime
import random
from utils.database.RedisClient import Redis
from models.Download import Download

class DownloadsController():
	def new(self):
		latitude = random.uniform(-90, 90)
		longitude = random.uniform(-180, 180)
		app_id = random.random() > 0.5 and "IOS_ALERT" or "IOS_MATE"
		download = Download(latitude, longitude, app_id)
		Redis.client.sadd("downloads", str(download))
		return self.format_one(download.to_json())		

	def get(self):
		downloads = []
		countries = {}
		appIds = {}
		timesOfDay = {
			"morning": 0,
			"afternoon": 0,
			"evening": 0,
			"night": 0
		}

		for elem in Redis.client.smembers("downloads"):
			elem = json.loads(elem)

			elem["coordinates"] = (elem["longitude"], elem["latitude"])

			downloads.append(elem)

			if elem["country"] in countries:
				countries[elem["country"]] += 1
			else: 
				countries[elem["country"]] = 1
			if elem["app_id"] in appIds:
				appIds[elem["app_id"]] += 1
			else:
				appIds[elem["app_id"]] = 1
			
			date = datetime.datetime.fromtimestamp(elem["downloaded_at"] / 1e3)
			hour = int(date.strftime("%H"))
			timesOfDay[self.get_time_of_day(hour)] += 1 

		return {
			"downloads": downloads,
			"countries": countries,
			"appIds": appIds,
			"timesOfDay": timesOfDay
		}

	def format_one(self, download):
		download["coordinates"] = (download["longitude"], download["latitude"])
		date = datetime.datetime.fromtimestamp(download["downloaded_at"] / 1e3)	
		hour = int(date.strftime("%H"))
		timeOfDay = self.get_time_of_day(hour)
		return {
			"download": download,
			"country": download["country"],
			"appId": download["app_id"],
			"timeOfDay": timeOfDay
		}	

	def get_time_of_day(self, hour):
		return (
			"morning" if 5 <= hour <= 11
			else
			"afternoon" if 12 <= hour <= 17
			else
			"evening" if 18 <= hour <= 22
			else
			"night"
		)