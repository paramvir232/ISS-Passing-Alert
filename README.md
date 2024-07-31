# ISS Alert Python Program
This Python program sends an email alert when the International Space Station (ISS) is passing overhead during nighttime. It uses APIs to track the ISS's position and smtplib to send the alert email.

## Features

**Real-time Tracking:** Checks ISS position every 60 seconds.

**Email Alerts:** Sends an email notification when the ISS is overhead and it’s dark.

**Customizable:** Easy to adjust location and email settings.

## Prerequisites
Before running the program, make sure you have:

Python 3.x installed.
An active email account for sending notifications (e.g., Gmail).
Installation

**Clone the repository:**

bash
Copy code
git clone https://github.com/your-username/iss-alert-python.git
Navigate to the project directory:

bash
Copy code
cd iss-alert-python
Install the required packages:

bash
Copy code
pip install requests
Configuration
API and Email Setup:

Open config.py and set your email credentials and recipient email address.

**Set your location coordinates (latitude and longitude).**

**Modify Email Settings:**

Configure the email sender and SMTP server settings in config.py.
Usage
Run the program:

bash
Copy code
python iss_alert.py
Program Operation:

The script will check every 60 seconds to see if the ISS is visible from your location during nighttime.
If conditions are met, an email alert will be sent with the subject "LOOK UP, ISS IS THERE!"
Example config.py
python
Copy code

## Email Configuration
EMAIL_ADDRESS = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'
RECIPIENT_EMAIL = 'recipient@example.com'
SMTP_SERVER = 'smtp.example.com'


## Location Coordinates
LATITUDE = 40.7128  # Example: New York City Latitude
LONGITUDE = -74.0060  # Example: New York City Longitude
Troubleshooting
Email not sending: Ensure SMTP settings and credentials are correct.
No alerts: Verify that your location coordinates are accurate and it's nighttime.
Contributing
Feel free to submit pull requests or open issues if you have suggestions or encounter problems.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, please contact paramvirgrewal232@gmail.com.

**Happy stargazing! 🌟🚀**

Feel free to modify this template as needed to better suit your project details and preferences!
