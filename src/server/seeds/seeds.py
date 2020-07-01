from seeds.DownloadSeeder import DownloadSeeder
from utils.database.RedisClient import Redis

class Seeder():
	def run(self):
		for i in range(20):
			id = Redis.client.scard("downloads") + 1
			download = DownloadSeeder(id)
			Redis.client.sadd("downloads", str(download))