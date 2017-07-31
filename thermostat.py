import nest
import csv
import time
import os
import sys
from datetime import datetime




client_id = os.environ['nestclientid']
client_secret = os.environ['nestclientsecret']

access_token_cache_file = 'nest.json'

napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)


# if napi.authorization_required:
#     print('Go to ' + napi.authorize_url + ' to authorize, then enter PIN below')
#     pin = input("PIN: ")
#     napi.request_token(pin)
# VH6YKMC8

def get_temperature():
    for device in napi.thermostats:
        temp = device.temperature
        return temp


def get_temp_scale():
    for device in napi.thermostats:
        scale = device.temperature_scale
        return scale


def get_date_time():
    # d = date.today()
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return dt


def get_target_temp():
    for device in napi.thermostats:
        target_temp = device.target
        return target_temp


def get_hvac_state():
    for device in napi.thermostats:
        hvac_state = device.hvac_state
        return hvac_state


def get_is_fan_timer_active():
        for device in napi.thermostats:
            is_fan_timer_active = device.fan
            return is_fan_timer_active


# def get_json_data():
#     for structure in napi.structures:
#         print ('Structure: %s' % structure.name)
#         print ('    Away: %s' % structure.away)
#         val = (structure.time_zone)
#
#     for device in structure.thermostats:
#         print ('        Device: %s' % device.name)
#         print ('            Temp: %0.1f' % device.temperature)
#         print ('            Humidity: %s' % device.humidity)
#         print ('            Has_Fan: %s' % device.has_fan)
#         print ('            Is_Using_Emergency_Heat:%s' % device.is_using_emergency_heat)
#         print ('            Temp_Scale:%s' % device.temperature_scale)
#         print ('            hvac_state:%s' % device.hvac_state)
#         print ('            can_cool:%s' % device.can_cool)
#
#     # Access advanced structure properties:
#     for structure in napi.structures:
#         print ('Structure   : %s' % structure.name)
#         print (' Postal Code                    : %s' % structure.postal_code)
#         print (' Country                        : %s' % structure.country_code)
#         print (' num_thermostats                : %s' % structure.num_thermostats)
#
#         return val


def get_data():
    with open('thermal_model.csv', "a") as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
        # wr.writerow("Temperature".split(','))
        # wr.writerow(str(get_temperature()).split(','))
        # wr.writerow(get_temp_scale())
        while (True):
            wr.writerow(
                ["{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format("Temperature:", get_temperature(), get_temp_scale(), "||",
                                                              "Date and Time:", get_date_time(), "||", "Hvac State:",
                                                              get_hvac_state(), "||", "Target Temperature in F:",
                                                              get_target_temp(), "||", "Is Fan Timer Active:", get_is_fan_timer_active())])

            print "Starting to Sleep"
            time.sleep(60)
            print "*" * 20
            print "TADAAA! AWAKE"
            print "Writing the data"


get_data()
