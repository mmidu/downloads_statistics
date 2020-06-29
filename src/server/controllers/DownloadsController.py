import json
import datetime

class DownloadsController():
	def __init__(self, redis):
		self.redis = redis

	def get(self):
		data = self.redis.client.smembers("downloads")
		downloads = [json.loads(i) for i in data]

		countries = {}
		appIds = {}
		timesOfDay = {
			"morning": 0,
			"afternoon": 0,
			"evening": 0,
			"night": 0
		}

		for elem in downloads:
			elem["coordinates"] = (elem["longitude"], elem["latitude"])
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

		for country in countries:
			countries[country] = {"label": country, "y": countries[country]}

		for app_id in appIds:
			appIds[app_id] = {"label": app_id, "y": appIds[app_id]}

		for tod in timesOfDay:
			timesOfDay[tod] = {"label": tod, "y": timesOfDay[tod]}

		ret = {
			"downloads": downloads,
			"countries": list(countries.values()),
			"appIds": list(appIds.values()),
			"timesOfDay": list(timesOfDay.values())
		}

		return ret

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