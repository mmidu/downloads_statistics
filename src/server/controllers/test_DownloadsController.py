from DownloadsController import DownloadsController
import random

dc = DownloadsController()

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