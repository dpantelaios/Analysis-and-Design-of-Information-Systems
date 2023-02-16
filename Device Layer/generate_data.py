import datetime, timedelta
from randomtimestamp import random_time
import random
import time

starting_date = datetime.datetime(2020, 5, 17)
print(str(starting_date))

random.seed(15)
print(1.5%1)
#GENERATE EVERY 15 MINUTES(1 seconds in our simulation)
def generate_thermal_sensor_values():
    return round(random.uniform(12, 35), 2)

def generate_energy_air_conditioner(min_value, max_value):
    return round(random.uniform(min_value, max_value), 2)

def generate_energy_rest_devices(min_value, max_value):
    return round(random.uniform(min_value, max_value), 2)

def generate_water_consumption():
    return round(random.uniform(0, 1), 2)

#GENERATE EVERY 1 DAY(96 seconds in our simulation)
def generate_Energy_total():
    return round(random.uniform(-1000, 1000), 2)

def generate_total_water_consumptions():
    return 110 + round(random.uniform(-10, 10), 2)

def generate_move_detection_daily(date):
    total_moves = random.randint(4, 6)
    timestamps = []
    for i in range(total_moves):
        temp_time = random_time()
        # print(temp_time)
        # print(temp_time.hour)
        temp_time = date + timedelta.Timedelta(hours = temp_time.hour, minutes = temp_time.minute)
        timestamps.append(temp_time)
    timestamps.sort()
    # print(timestamps)
    return timestamps

starttime = time.time()
Etotal = Water_total = 0
while True:
    print(starting_date)

    th1 = str(starting_date) + " | " + str(generate_thermal_sensor_values())
    th2 = str(starting_date) + " | " + str(generate_thermal_sensor_values())
    hvac1 = str(starting_date) + " | " + str(generate_energy_air_conditioner(0, 100))
    hvac2 = str(starting_date) + " | " + str(generate_energy_air_conditioner(0, 200))
    miac1 = str(starting_date) + " | " + str(generate_energy_rest_devices(0, 150))
    miac2 = str(starting_date) + " | " + str(generate_energy_rest_devices(0, 200))
    w1 = str(starting_date) + " | " + str(generate_water_consumption())
    
    print("TH1: ", th1)
    print("TH2: ", th2)
    print("HVAC1: ", hvac1)
    print("HVAC2: ", hvac2)
    print("miac1: ", miac1)
    print("MIAC2: ", miac2)
    print("W1: ", w1)

    if starting_date.hour == 0 and starting_date.minute == 0:
        Etotal += 2600*24 + generate_Energy_total()
        Etotal = round(Etotal, 2)
        Water_total += generate_total_water_consumptions()
        Water_total = round(Water_total, 2)
        timestamps = generate_move_detection_daily(starting_date)
        Etotal_str = str(starting_date) + " | " + str(Etotal)
        Water_total_str = str(starting_date) + " | " + str(Water_total)
        print("Etot: ", Etotal_str)
        print("Water_total_str: ", Water_total_str)
        
    for temp_timestamp in timestamps:
        if temp_timestamp <= starting_date:
            print("SENT MOVE DETECTION")
            print(str(temp_timestamp) + " | 1")
            timestamps.pop(0)

    starting_date = starting_date + timedelta.Timedelta(minutes=15)
    time.sleep(1 - ((time.time() - starttime) % 1))