import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 30.900965  # Your latitude
MY_LONG = 75.857277  # Your longitude

my_google_email = 'pythonmail887@gmail.com'
my_yahoo_email = 'python_testing_mail@yahoo.com'
google_password = 'mlphuwrgqylhbqgn'

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    'tzid': 'Asia/Kolkata'
}


def is_iss_close():
    """ Returns True if ISS is Nearby my location and can be observed. Otherwise False"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT + 5 > iss_latitude > MY_LAT - 5 and MY_LONG + 5 > iss_longitude > MY_LONG - 5:
        return True
    return False


def is_dark():
    """ Returns True if is night time. Otherwise False  """
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if sunrise_hour > now_hour > sunset_hour:
        return True
    return False


while True:

    time_now = datetime.now()
    now_hour = time_now.hour

    # Checks if ISS is close to my location and its night time so that I can observe it
    if is_iss_close() and is_dark():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_google_email, password=google_password)
            connection.sendmail(from_addr=my_google_email, to_addrs=my_yahoo_email,
                                msg=f'Subject:ISS ALERT !!\n\n LOOK UP ISS IS THERE !!')
    time.sleep(60)
