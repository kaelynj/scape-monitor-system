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

# Meetings
* 29 December 2022 Meeting - Define Required Features, Basic Design, Team Availability
* 5 January 2023 Meeting - Updates on material/component orders, Define Timeline, Setup team sharing and comms
* 17 January 2023 Meeting (proposed) - Plan February prototyping session to be on-site at Woodcock, List materials needed for a successful session, Align on prework which must be completed prior to session

# Timeline
* February 2023 
  * Prototype and deploy garlic scape remote monitoring system at Woodcock
  * Use demo data and photos to confirm system capabilities
* February - April 2023
  * Upload photos (at least one daily) to test the stability of the connection and troubeshoot other potential issues
  * Add capabilities for remote monitoring system to act as a wifi node to enable weather station to upload data from the field (optional)
* May 2023
  * Deploy garlic scape remote monitoring system to garlic plot
  * Review photo resolution to determine if scape progress can be observed
* June 2023
  * Use photos to determine scape harvest timing
* July - October 2023
  * Move remote monitoring system to do timelapse photgraphy on another crop on the farm (e.g. oats, clover) (optional)

# Items needed for February Prototype Session
* SD card with Pi OS
* Computer monitor
* keyboard
* snacks and beverages (dietary restrictions)

# Parking Lot (put ideas to return to here)
* Rasp Pi Pico for next iteration of prototype for lower cost and lower energy consumption

