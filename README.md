# scape-monitor-system
 Project to automate obtaining pictures of garlic scapes and upload the photos to google drive.

# Required Features
* Take one picture a day for several hours during daylight with the date & time as filename
  * Script automation either through bash scheduler or python APScheduler
  * Scheduling script should happen at startup
* Once a picture is taken, verify internet connection to connect to google drive and:
  * Create a new gdrive directory for the day's photos (if doesn't exist)
  * Upload each photo to the directory
* At the day's end:
  * Verify all photos were successfully uploaded.  Upload any that were missed
  * Delete all photos older than one week from current date locally
  * Power off/hibernate the device?
* Test internet connection periodically

# Libraries needed
* Python >= 3.10.7
* pip, conda
* PiCamera
* google-api-python-client
* google-auth-httplib2 google-auth-oauthlib

# Websites to reference
* [Raspi Camera Interface](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/0)
* [GDrive API Reference](https://developers.google.com/drive/api/quickstart/python)
* [Stack OverFlow on Automating Python Script](https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day)
  * [APScheduler Python](https://apscheduler.readthedocs.io/en/latest/)
  * [Bash Schedule at Time](https://stackoverflow.com/questions/18945669/how-to-run-a-script-at-a-certain-time-on-linux)
  * [Use cron to automate scripts](https://stackoverflow.com/questions/878600/how-to-create-a-cron-job-using-bash-automatically-without-the-interactive-editor)
