from datetime import datetime
from playsound import playsound
from os import chdir


def is_valid_time(time):
    if len(time) != 11:
        return "Invalid input for time! Try again..."
    else:
        if int(time[0:2]) > 12 or int(time[3:5]) > 59 or int(time[6:8]) > 59:
            return "Invalid input! Try again..."

        else:
            return "perfect"


def set_alarm():
    while True:

        time = input(
            "Enter the time you want to set a alarm \n"
            "for in the following format 'HH:MM:SS AM/PM': ")

        hour = time[0:2]
        minute = time[3:5]
        sec = time[6:8]
        am_pm = time[9:].upper()

        true = is_valid_time(time.lower())

        if true != "perfect":
            print(true)

        else:
            print(f"Alarm set for {time}...")
            break

    while True:
        curr_time = datetime.now()

        curr_hour = curr_time.strftime("%I")
        curr_min = curr_time.strftime("%M")
        curr_sec = curr_time.strftime("%S")
        curr_am_pm = curr_time.strftime("%p")

        if am_pm == curr_am_pm and hour == curr_hour and minute == curr_min and sec == curr_sec:
            print("Times Up!")
            playsound("mixkit-data-scaner-2847.wav")
            break
