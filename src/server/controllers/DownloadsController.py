import json

class DownloadsController():
    def __init__(self, redis):
        self.redis = redis

    def get(self):
	    data = self.redis.client.smembers("downloads")
	    json_data = [json.loads(i) for i in data]
	    json_data = [{"id": i["id"], "coordinates": [i["longitude"], i["latitude"]]} for i in json_data]
	    return json_data