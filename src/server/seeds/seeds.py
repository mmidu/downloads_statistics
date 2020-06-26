from seeds.DownloadSeeder import DownloadSeeder

class Seeder():
	def __init__(self, redis):
		self.redis = redis

	def run(self):
		for i in range(20):
			id = self.redis.client.scard("downloads") + 1
			download = DownloadSeeder(id)
			self.redis.client.sadd("downloads", str(download))