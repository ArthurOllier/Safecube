import requests
import haversine
import datetime

from requests_oauthlib import OAuth1
from datetime import datetime as dt
from haversine import haversine
from json import dumps
from logger import logger

if __name__ == '__main__':
    segment = [
        {"data": {"type": "HeartBeat", "geoloc": False, "magnet": "Open", "battery": 3.6}, "radius": 15100,
         "is_done": True, "latitude": 49.36079467825381, "longitude": 2.7844463352644944,
         "date_reached": "2021-01-20 15:32"},
        {"data": {"mac1": "00:3A:9A:69:F5:50", "mac2": "00:3A:9A:6E:33:40", "type": "Wifi", "geoloc": False},
         "radius": 75, "is_done": True, "latitude": 49.3519683, "longitude": 2.762727439,
         "date_reached": "2021-01-20 16:52"},
        {"data": {"mac1": "4C:77:6D:FA:EF:60", "mac2": "4C:77:6D:FA:EF:61", "type": "Wifi", "geoloc": False},
         "radius": 131, "is_done": True, "latitude": 49.3517125, "longitude": 2.762460709,
         "date_reached": "2021-01-20 16:52"},
        {"data": {"mac1": "4C:77:6D:F8:0C:E5", "mac2": "00:3A:9A:69:F5:50", "type": "Wifi", "geoloc": False},
         "radius": 147, "is_done": True, "latitude": 49.3521656, "longitude": 2.762288571,
         "date_reached": "2021-01-20 17:02"},
        {"data": {"mac1": "E4:9E:12:7E:E3:89", "mac2": "00:00:00:00:00:00", "type": "Wifi", "geoloc": False},
         "radius": 5100, "is_done": True, "latitude": 48.940112405596594, "longitude": 2.472072464098831,
         "date_reached": "2021-01-20 17:52"},
        {"data": {"mac1": "08:21:EF:14:30:5D", "mac2": "14:0C:76:7E:13:04", "type": "Wifi", "geoloc": False},
         "radius": 15900, "is_done": True, "latitude": 48.886234024172644, "longitude": 2.4716785393445897,
         "date_reached": "2021-01-20 18:02"},
        {"data": {"mac1": "14:0C:76:B1:B2:A7", "mac2": "68:A3:78:10:0D:C2", "type": "Wifi", "geoloc": False},
         "radius": 6100, "is_done": True, "latitude": 48.903838194328465, "longitude": 2.461976129348987,
         "date_reached": "2021-01-20 18:12"},
        {"data": {"mac1": "68:A3:78:10:0D:C0", "mac2": "00:00:00:00:00:00", "type": "Wifi", "geoloc": False},
         "radius": 680, "is_done": True, "latitude": 48.90146, "longitude": 2.469162,
         "date_reached": "2021-01-20 18:12"},
        {"data": {"mac1": "E8:BE:81:A1:44:70", "mac2": "D8:07:B6:7F:05:FF", "type": "Wifi", "geoloc": False},
         "radius": 97, "is_done": True, "latitude": 48.8112438, "longitude": 2.400947182,
         "date_reached": "2021-01-20 18:42"},
        {"data": {"mac1": "E4:9E:12:77:FB:EB", "mac2": "84:A1:D1:3B:AA:F0", "type": "Wifi", "geoloc": False},
         "radius": 6500, "is_done": True, "latitude": 48.81595567993225, "longitude": 2.4114014759409463,
         "date_reached": "2021-01-20 18:42"},
        {"data": {"mac1": "E8:BE:81:A1:44:70", "mac2": "34:27:92:D8:34:B0", "type": "Wifi", "geoloc": False},
         "radius": 56, "is_done": True, "latitude": 48.8111453, "longitude": 2.400685438,
         "date_reached": "2021-01-20 18:45"},
        {"data": {"mac1": "E4:9E:12:0F:B4:B5", "mac2": "E4:9E:12:0F:B4:B7", "type": "Wifi", "geoloc": False},
         "radius": 62, "is_done": True, "latitude": 48.8110864, "longitude": 2.400727272,
         "date_reached": "2021-01-20 18:46"},
        {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:1F:C9:FC:F2:50", "type": "Wifi", "geoloc": False},
         "radius": 250, "is_done": True, "latitude": 48.8111542, "longitude": 2.400504064,
         "date_reached": "2021-01-20 19:02"},
        {"data": {"mac1": "00:3A:99:7C:87:20", "mac2": "84:8A:8D:F4:F8:78", "type": "Wifi", "geoloc": False},
         "radius": 61, "is_done": True, "latitude": 48.8120502, "longitude": 2.399715718,
         "date_reached": "2021-01-20 19:02"},
        {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:24:98:99:01:00", "type": "Wifi", "geoloc": False},
         "radius": 123, "is_done": True, "latitude": 48.8112391, "longitude": 2.400305793,
         "date_reached": "2021-01-20 19:07"},
        {"data": {"mac1": "00:3A:99:7C:87:20", "mac2": "00:1F:C9:FC:F2:50", "type": "Wifi", "geoloc": False},
         "radius": 127, "is_done": True, "latitude": 48.8113913, "longitude": 2.399820891,
         "date_reached": "2021-01-20 19:08"},
        {"data": {"mac1": "00:1F:C9:FC:F3:B0", "mac2": "00:3A:99:7C:87:20", "type": "Wifi", "geoloc": False},
         "radius": 126, "is_done": True, "latitude": 48.8113828, "longitude": 2.399827458,
         "date_reached": "2021-01-20 21:10"},
        {"data": {"mac1": "00:1F:C9:FC:F2:50", "mac2": "84:8A:8D:F4:F8:78", "type": "Wifi", "geoloc": False},
         "radius": 70, "is_done": True, "latitude": 48.8123243, "longitude": 2.399805473,
         "date_reached": "2021-01-20 21:10"},
        {"data": {"mac1": "00:26:0A:EF:8B:80", "mac2": "00:3A:9A:3F:6F:50", "type": "Wifi", "geoloc": False},
         "radius": 48, "is_done": True, "latitude": 48.8127258, "longitude": 2.399676978,
         "date_reached": "2021-01-20 21:18"},
        {"data": {"mac1": "70:01:B5:31:5D:18", "mac2": "64:7C:34:F2:4B:6C", "type": "Wifi", "geoloc": False},
         "radius": 49, "is_done": True, "latitude": 48.8127092, "longitude": 2.399718476,
         "date_reached": "2021-01-20 21:18"},
        {"data": {"mac1": "70:01:B5:31:5D:18", "mac2": "00:26:0A:EF:8B:80", "type": "Wifi", "geoloc": False},
         "radius": 45, "is_done": True, "latitude": 48.8125931, "longitude": 2.399841137,
         "date_reached": "2021-01-21 06:09"},
        {"data": {"mac1": "00:3A:9A:3F:6F:50", "mac2": "EC:8E:B5:AC:79:8C", "type": "Wifi", "geoloc": False},
         "radius": 55, "is_done": True, "latitude": 48.8125821, "longitude": 2.399738258,
         "date_reached": "2021-01-21 06:09"},
        {"data": {"mac1": "34:27:92:47:77:69", "mac2": "34:27:92:47:77:6B", "type": "Wifi", "geoloc": False},
         "radius": 72, "is_done": True, "latitude": 48.8129672, "longitude": 2.39961969,
         "date_reached": "2021-01-21 06:19"},
        {"data": {"mac1": "34:27:92:47:77:6A", "mac2": "44:CE:7D:D3:26:56", "type": "Wifi", "geoloc": False},
         "radius": 62, "is_done": True, "latitude": 48.8129618, "longitude": 2.400074506,
         "date_reached": "2021-01-21 06:19"},
        {"data": {"mac1": "34:27:92:47:77:6B", "mac2": "34:27:92:47:77:6A", "type": "Wifi", "geoloc": False},
         "radius": 69, "is_done": True, "latitude": 48.8129651, "longitude": 2.399579219,
         "date_reached": "2021-01-21 06:21"},
        {"data": {"mac1": "34:27:92:47:77:69", "mac2": "44:CE:7D:D3:26:56", "type": "Wifi", "geoloc": False},
         "radius": 61, "is_done": True, "latitude": 48.8129533, "longitude": 2.400144078,
         "date_reached": "2021-01-21 06:21"},
        {"data": {"mac1": "00:3A:9A:1A:C5:D0", "mac2": "68:A3:78:0D:39:BC", "type": "Wifi", "geoloc": False},
         "radius": 65, "is_done": True, "latitude": 48.8130416, "longitude": 2.399362081,
         "date_reached": "2021-01-21 06:41"},
        {"data": {"mac1": "94:10:3E:A7:D9:7C", "mac2": "68:A3:78:0D:39:BA", "type": "Wifi", "geoloc": False},
         "radius": 82, "is_done": True, "latitude": 48.8131206, "longitude": 2.399266009,
         "date_reached": "2021-01-21 06:41"},
        {"data": {"mac1": "68:A3:78:0D:39:BC", "mac2": "68:A3:78:0D:39:BA", "type": "Wifi", "geoloc": False},
         "radius": 70, "is_done": True, "latitude": 48.8131257, "longitude": 2.39933306,
         "date_reached": "2021-01-21 06:46"},
        {"data": {"mac1": "00:3A:9A:1A:C5:D0", "mac2": "00:00:00:00:00:00", "type": "Wifi", "geoloc": False},
         "radius": 553, "is_done": True, "latitude": 48.812571, "longitude": 2.405984,
         "date_reached": "2021-01-21 06:46"},
        {"data": {"mac1": "34:27:92:42:CB:A3", "mac2": "70:FC:8F:52:25:18", "type": "Wifi", "geoloc": False},
         "radius": 60, "is_done": True, "latitude": 48.8124271, "longitude": 2.397505111,
         "date_reached": "2021-01-21 07:01"},
        {"data": {"mac1": "8C:45:00:01:70:E5", "mac2": "00:00:00:00:00:00", "type": "Wifi", "geoloc": False},
         "radius": 775, "is_done": True, "latitude": 48.83112, "longitude": 2.389436,
         "date_reached": "2021-01-21 07:11"},
        {"data": {"mac1": "54:B8:0A:3E:6F:98", "mac2": "00:00:00:00:00:00", "type": "Wifi", "geoloc": False},
         "radius": 541, "is_done": True, "latitude": 48.74274, "longitude": 2.87396,
         "date_reached": "2021-01-21 22:17"},
        {"data": {"mac1": "34:FA:9F:2F:11:58", "mac2": "EC:AD:E0:EC:3D:63", "type": "Wifi", "geoloc": False},
         "radius": 84, "is_done": True, "latitude": 48.8660382, "longitude": 2.334203008,
         "date_reached": "2021-01-21 23:07"},
        {"data": {"mac1": "00:1B:93:01:03:F0", "mac2": "2C:4F:52:64:9F:C2", "type": "Wifi", "geoloc": False},
         "radius": 66, "is_done": True, "latitude": 48.8661625, "longitude": 2.334117512,
         "date_reached": "2021-01-21 23:07"}
    ]
else:
    segment = []

HERE_CLIENT_ID = "."
HERE_CLIENT_SECRET = "."


def fetch_here_reverse_geocoding(lat, lng):
    data = {
        "grantType": "client_credentials",
        "clientId": HERE_CLIENT_ID,
        "clientSecret": HERE_CLIENT_SECRET,
    }

    response = requests.post(
        url="https://account.api.here.com/oauth2/token",
        auth=OAuth1(HERE_CLIENT_ID, client_secret=HERE_CLIENT_SECRET),
        headers={"Content-type": "application/json"},
        data=dumps(data),
    ).json()

    token = response["accessToken"]
    token_type = response["tokenType"]

    headers = {"Authorization": f"{token_type} {token}"}
    resp = requests.get(
        f"https://revgeocode.search.hereapi.com/v1/revgeocode?at={lat}%2C{lng}&lang=en-US",
        headers=headers,
    )
    logger.debug(f"Response {resp.status_code}:{resp}")
    if not resp.status_code == 200:
        return None
    payload = resp.json()
    if not len(payload.get("items", [])) or not payload["items"][0].get("address"):
        return None
    return payload["items"][0]["address"]


# Your function
def dist_between_points(tp1, tp2):
    dist = haversine((tp1['latitude'], tp1['longitude']), (tp2['latitude'], tp2['longitude']))
    return dist


def time_between_points(tp1, tp2):
    time = abs(dt.strptime(tp1['date_reached'], "%Y-%m-%d %H:%M") - dt.strptime(tp2['date_reached'], "%Y-%m-%d %H:%M"))
    return time


def segment_length(trackpoints):
    length = 0
    subsegment = []
    for tp in trackpoints:
        if len(subsegment) >= 1:
            length += dist_between_points(tp, subsegment[-1])
        subsegment.append(tp)
    return length


def segment_radius(trackpoints):
    radius = dist_between_points(trackpoints[0], trackpoints[-1])
    return radius


def segment_time(trackpoints):
    time = time_between_points(trackpoints[0], trackpoints[-1])
    return time


def append_track_points(trackpoints, tp):
    trackpoints.append(tp)
    sort_segment(trackpoints)
    return trackpoints

def sort_segment(segment):
    return segment.sort(key=sorting_by_date)

def sorting_by_date(e):
    return e['date_reached']

# minDist : Minimal distance done in Km
# maxTime : Maximal time in this radius in Hours
def find_stops(minDist, maxTime, segment):
    maxTimeDelta = datetime.timedelta(hours=maxTime)
    result = []
    subsegment = []
    stops = []

    for tp in segment:
        if len(result) >= 1:
            if segment_radius(subsegment) < minDist and segment_time(subsegment) > maxTimeDelta:
                # Kilometer radius from start is < to minDist and Time in these minDist radius is > to maxTime
                print("pause started at lat:", subsegment[0]["latitude"], "lon :", subsegment[0]["longitude"],
                      "From : ", subsegment[0]["date_reached"], "to", subsegment[-1]["date_reached"],
                      "break duration : ", segment_time(subsegment), "break radius : ", segment_radius(subsegment))
                stops.append(fetch_here_reverse_geocoding(subsegment[0]["latitude"], subsegment[0]["longitude"]))
                stops.append(subsegment[0])
                stops.append(subsegment[-1])
                subsegment = []
            elif segment_radius(subsegment) > minDist:
                # kilometer traveled > minDist, we are still running removing the oldest point
                subsegment.pop(0)

        subsegment.append(tp)
        result = append_track_points(result, tp)

    return stops


print(find_stops(2, 12, segment))

# BONUS
from random import randrange

bonus = []
while segment:
    bonus = append_track_points(bonus, segment.pop(randrange(0, len(segment), 1)))

print(find_stops(2, 12, bonus))
