from DownloadsController import DownloadsController
from utils.database.RedisClient import RedisClient
import random

redis = RedisClient('ds_redis', 6379, 0)
dc = DownloadsController(redis)

def test_format_data():
    collection = {
        "foo": 1,
        "bar": 2
    }
    formattedCollection = dc.format_data(collection)
    assert isinstance(formattedCollection, list)

def test_get_time_of_day():
    morning = dc.get_time_of_day(random.random() * 6 + 5)
    afternoon = dc.get_time_of_day(random.random() * 5 + 12)
    evening = dc.get_time_of_day(random.random() * 4 + 18)

    t = random.random()
    night = dc.get_time_of_day(t > 0.5 and t * 2 + 23 or t * 5)

    assert morning == "morning"
    assert afternoon == "afternoon"
    assert evening == "evening"
    assert night == "night"