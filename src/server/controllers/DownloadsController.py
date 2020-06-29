import json
import datetime

class DownloadsController():
	def __init__(self, redis):
		self.redis = redis

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

		for elem in self.redis.client.smembers("downloads"):
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
			"countries": self.format_data(countries),
			"appIds": self.format_data(appIds),
			"timesOfDay": self.format_data(timesOfDay)
		}



	def format_data(self, collection):
		for elem in collection:
			collection[elem] = {"label": elem, "y": collection[elem]}
		return list(collection.values())


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