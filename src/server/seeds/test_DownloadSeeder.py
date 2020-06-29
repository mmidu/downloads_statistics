from DownloadSeeder import DownloadSeeder

def test_data():
	download = DownloadSeeder(0)
	assert download.latitude <= 90 and download.latitude >= -90
	assert download.longitude <= 180 and download.latitude >= -180
	assert download.app_id in ["IOS_ALERT", "IOS_MATE"]
	assert isinstance(download.downloaded_at, int)