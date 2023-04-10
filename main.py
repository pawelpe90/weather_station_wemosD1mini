import urllib.request
import ast
from datetime import datetime
import csv
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def read_ip(ip):
    with urllib.request.urlopen(ip) as response:
        html = response.read()
    return html


def date_time():
    x = datetime.now()
    date = x.strftime("%d-%m-%Y")
    time = x.strftime("%H:%M")

    return date, time


def conflate_date_and_weather_data():
    data = dict()
    data["date"] = date_time()[0]
    data["time"] = date_time()[1]
    data.update(ast.literal_eval(read_ip(ip).decode('utf-8')))

    return data


def save_to_csv(dictionary):
    filename = os.path.join(dir_path, 'weather_data_lakowa.csv')
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f, dictionary.keys())
        # w.writeheader()
        w.writerow(dictionary)


def save_to_json(dictionary):
    with open('weather_data_lakowa.json', 'a', newline='\n') as f:
        json.dump(dictionary, f)


if __name__ == '__main__':
    ip = 'http://192.168.1.52/'
    wd = conflate_date_and_weather_data()
    save_to_csv(wd)
    # save_to_json(wd)
