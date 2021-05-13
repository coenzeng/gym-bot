## Setup

This script works by using selenium to scrape web elements in a chrome browser. First, download a chrome driver here:

https://sites.google.com/a/chromium.org/chromedriver/downloads

Use the version that corressponds to your version of chrome. To check your version of chrome, click the the 3 dots at the top-right of chrome, then Help > About Google Chrome.

Place the chrome driver in a recognizable path, such as "C:\Program Files (x86)\selenium\chromedriver.exe". Take your chrome driver path and replace the default path on line 40.

## How to run
The program takes 2 additional arguments, the email and the password. Run the program like so:

`python gym-booking-bot.py email password`

If gyms are closed, the script can tell (due to the lack of some buttons) and the program will terminate early.

