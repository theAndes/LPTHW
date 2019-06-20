import urllib.request
import json
import datetime


class range:
    end_time = datetime.date.today()
    start_time = end_time - datetime.timedelta(days=1)


def get_USGS_earthquake_data():
    webURL = urllib.request.urlopen(
        "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime="+str(range.start_time) +
        "&endtime="+str(range.end_time))
    if webURL.getcode() != 200:
        print("Error:", webURL.getcode())
    data = webURL.read()
    print_results(data)


def print_results(data):
    USGS = json.loads(data)
    if "title" in USGS["metadata"]:
        print(USGS["metadata"]["title"])
        print(f"Date range of sample: {range.start_time} to {range.end_time}.")
    count = USGS["metadata"]["count"]
    print(f"There were "+str(count) +
          " earthquakes in the last 24hrs. Below are of magnitude of 1 and felt by at least 2 people")
    print("-"*10)

    for i in USGS["features"]:

        if i["properties"]["mag"] >= 1.0 and i["properties"]["felt"] != None:
            number_of_people = i["properties"]["felt"]
            person = ''
            if number_of_people == 1:
                person = "person"
            else:
                person = "people"

            print(f"Location: {i['properties']['place']} with a magnitude of", i["properties"]["mag"],
                  "and was felt by", i["properties"]["felt"], person+".")
            print("-"*10)


get_USGS_earthquake_data()
