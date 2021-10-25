import datetime
from unittest import TestCase
from main import dist_between_points, time_between_points, segment_radius, segment_time


class TestDistBetweenPoints(TestCase):

    def test_dist_between_same_points(self):
        tp1 = {"data": {"type": "HeartBeat", "geoloc": False, "magnet": "Open", "battery": 3.6}, "radius": 15100,
               "is_done": True, "latitude": 49.36079467825381, "longitude": 2.7844463352644944,
               "date_reached": "2021-01-20 15:32"}
        self.assertEqual(dist_between_points(tp1, tp1), 0, "must return 0")

    def test_dist_between_points(self):
        tp1 = {"data": {"type": "HeartBeat", "geoloc": False, "magnet": "Open", "battery": 3.6}, "radius": 15100,
               "is_done": True, "latitude": 49.36079467825381, "longitude": 2.7844463352644944,
               "date_reached": "2021-01-20 15:32"}
        tp2 = {"data": {"mac1": "00:3A:9A:69:F5:50", "mac2": "00:3A:9A:6E:33:40", "type": "Wifi", "geoloc": False},
               "radius": 75, "is_done": True, "latitude": 49.3519683, "longitude": 2.762727439,
               "date_reached": "2021-01-20 16:52"}
        self.assertEqual(dist_between_points(tp1, tp2), 1.8541011557755416, "must return 1.8541011557755416")

class TestTimeBetweenPoints(TestCase):
    def test_time_between_same_points(self):
        tp1 = {"data": {"type": "HeartBeat", "geoloc": False, "magnet": "Open", "battery": 3.6}, "radius": 15100,
               "is_done": True, "latitude": 49.36079467825381, "longitude": 2.7844463352644944,
               "date_reached": "2021-01-20 15:32"}
        self.assertEqual(time_between_points(tp1, tp1), datetime.timedelta(0), "must return 0")

    def test_time_between_points(self):
        tp1 = {"data": {"type": "HeartBeat", "geoloc": False, "magnet": "Open", "battery": 3.6}, "radius": 15100,
               "is_done": True, "latitude": 49.36079467825381, "longitude": 2.7844463352644944,
               "date_reached": "2021-01-20 15:32"}
        tp2 = {"data": {"mac1": "00:3A:9A:69:F5:50", "mac2": "00:3A:9A:6E:33:40", "type": "Wifi", "geoloc": False},
               "radius": 75, "is_done": True, "latitude": 49.3519683, "longitude": 2.762727439,
               "date_reached": "2021-01-20 16:52"}
        self.assertEqual(time_between_points(tp1, tp2), datetime.timedelta(hours=1, minutes=20), "must return 1h20")


class TestSegmentradius(TestCase):
    def test_segment_radius(self):
        segment = [{"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:24:98:99:01:00", "type": "Wifi", "geoloc": False},
                    "radius": 123, "is_done": True, "latitude": 48.8112391, "longitude": 2.400305793,
                    "date_reached": "2021-01-20 19:07"},
                   {"data": {"mac1": "00:3A:99:7C:87:20", "mac2": "00:1F:C9:FC:F2:50", "type": "Wifi", "geoloc": False},
                    "radius": 127, "is_done": True, "latitude": 48.8113913, "longitude": 2.399820891,
                    "date_reached": "2021-01-20 19:08"},
                   {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:3A:99:7C:87:20", "type": "Wifi", "geoloc": False},
                    "radius": 126, "is_done": True, "latitude": 48.8113828, "longitude": 2.399827458,
                    "date_reached": "2021-01-20 21:10"}]
        self.assertEqual(segment_radius(segment),0.038499308997767726,"must be 0.038499308997767726")

    def test_segment_radius_null(self):
        segment = [{"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:24:98:99:01:00", "type": "Wifi", "geoloc": False},
                    "radius": 123, "is_done": True, "latitude": 48.8112391, "longitude": 2.400305793,
                    "date_reached": "2021-01-20 19:07"},
                   {"data": {"mac1": "00:3A:99:7C:87:20", "mac2": "00:1F:C9:FC:F2:50", "type": "Wifi", "geoloc": False},
                    "radius": 127, "is_done": True, "latitude": 48.8112391, "longitude": 2.400305793,
                    "date_reached": "2021-01-20 19:08"},
                   {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:3A:99:7C:87:20", "type": "Wifi", "geoloc": False},
                    "radius": 126, "is_done": True, "latitude": 48.8112391, "longitude": 2.400305793,
                    "date_reached": "2021-01-20 21:10"}]
        self.assertEqual(segment_radius(segment),0,"must be 0")


class TestSegmentTime(TestCase):
    def test_segment_time(self):
        segment = [{"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:24:98:99:01:00", "type": "Wifi", "geoloc": False},
                    "radius": 123, "is_done": True, "latitude": 48.8112391, "longitude": 2.400305793,
                    "date_reached": "2021-01-20 19:07"},
                   {"data": {"mac1": "00:3A:99:7C:87:20", "mac2": "00:1F:C9:FC:F2:50", "type": "Wifi", "geoloc": False},
                    "radius": 127, "is_done": True, "latitude": 48.8113913, "longitude": 2.399820891,
                    "date_reached": "2021-01-20 19:08"},
                   {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:3A:99:7C:87:20", "type": "Wifi", "geoloc": False},
                    "radius": 126, "is_done": True, "latitude": 48.8113828, "longitude": 2.399827458,
                    "date_reached": "2021-01-20 21:10"}]
        self.assertEqual(segment_time(segment), datetime.timedelta(hours=2, minutes=3), "must return 20 minutes")
    def test_segment_time_null(self):
        segment = [{"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:24:98:99:01:00", "type": "Wifi", "geoloc": False},
                    "radius": 123, "is_done": True, "latitude": 48.8112391, "longitude": 2.400305793,
                    "date_reached": "2021-01-20 19:07"},
                   {"data": {"mac1": "00:3A:99:7C:87:20", "mac2": "00:1F:C9:FC:F2:50", "type": "Wifi", "geoloc": False},
                    "radius": 127, "is_done": True, "latitude": 48.8113913, "longitude": 2.399820891,
                    "date_reached": "2021-01-20 19:07"},
                   {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:3A:99:7C:87:20", "type": "Wifi", "geoloc": False},
                    "radius": 126, "is_done": True, "latitude": 48.8113828, "longitude": 2.399827458,
                    "date_reached": "2021-01-20 19:07"}]
        self.assertEqual(segment_time(segment), datetime.timedelta(0), "must return 0")
