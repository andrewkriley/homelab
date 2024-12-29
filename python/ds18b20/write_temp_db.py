from w1thermsensor import W1ThermSensor
from influxdb import InfluxDBClient

sensors = W1ThermSensor.get_available_sensors()
outside1_hotisle_041781b282ff_sensor = sensors[0]
outside1_hotisle_041781b282ff_sensor.get_temperature()

crac1_coldisle_031771e93cff_sensor = sensors[1]
crac1_coldisle_031771e93cff_sensor.get_temperature()

outside2_hotisle_041781e887ff_sensor = sensors[2]
outside2_hotisle_041781e887ff_sensor.get_temperature()

crac2_coldisle_0317714b31ff_sensor = sensors[3]
crac2_coldisle_0317714b31ff_sensor.get_temperature()

centre_coldisle_041781a26eff_sensor = sensors[4]
centre_coldisle_041781a26eff_sensor.get_temperature()


client = InfluxDBClient(database='tempDB')

series = []
point_outside1_hotisle_041781b282ff = {
    "measurement": "temperature",
    "tags": {
        "location": "Server Room",
        "room": "1",
        "usage": "outside1_hotisle_041781b282ff",
        "type": "ds18b20"
    },
    "fields": {
        "value": outside1_hotisle_041781b282ff_sensor.get_temperature()
    }
}

point_outside2_hotisle_041781e887ff = {
    "measurement": "temperature",
    "tags": {
        "location": "Server Room",
        "room": "1",
        "usage": "outside2_hotisle_041781e887ff",
        "type": "ds18b20"
    },
    "fields": {
        "value": outside2_hotisle_041781e887ff_sensor.get_temperature()
    }
}

point_crac1_coldisle_031771e93cff = {
    "measurement": "temperature",
    "tags": {
        "location": "Server Room",
        "room": "1",
        "usage": "crac1_coldisle_031771e93cff",
        "type": "ds18b20"
    },
    "fields": {
        "value": crac1_coldisle_031771e93cff_sensor.get_temperature()
    }
}

point_crac2_coldisle_0317714b31ff = {
    "measurement": "temperature",
    "tags": {
        "location": "Server Room",
        "room": "1",
        "usage": "crac2_coldisle_0317714b31ff",
        "type": "ds18b20"
    },
    "fields": {
        "value": crac2_coldisle_0317714b31ff_sensor.get_temperature()
    }
}

point_centre_coldisle_041781a26eff = {
    "measurement": "temperature",
    "tags": {
        "location": "Server Room",
        "room": "1",
        "usage": "centre_coldisle_041781a26eff",
        "type": "ds18b20"
    },
    "fields": {
        "value": centre_coldisle_041781a26eff_sensor.get_temperature()
    }
}

series.append(point_outside1_hotisle_041781b282ff)
series.append(point_outside2_hotisle_041781e887ff)
series.append(point_crac1_coldisle_031771e93cff)
series.append(point_crac2_coldisle_0317714b31ff)
series.append(point_centre_coldisle_041781a26eff)


client.write_points(series)
