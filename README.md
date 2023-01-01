# webServerRPi
Updating inputs on RPi webserver using Python, Flask and jQuery

######################################################################
This is an example of how to set up a RPi webserver and update the input values of certain inputs automatically. 
For this case, the inputs are: GPIO4, GPIO17, GPIO27, GPIO22, GPIO5, GPIO6, GPIO13, GPIO19

##########################################################
Step by step guide to install the necessary packages
##########################################################
#For starters I guess you already have python and pip3, if not:

sudo apt update
sudo apt upgrade
sudo apt-get install python3
sudo apt install python3-pip

# Now let’s get Flask (The webserver)
sudo pip3 install Flask
# Get the files from the repository and bear in mind that I had them in this manner:
# /home/pi
#         /app.py
#         /templates/index.html
#         /static/rightLogo.png, ....
# Now to run the server:
set FLASK_APP = app.py
sudo flask run --host=0.0.0.0

# In my case if I didn't run it in that manner it simply didn't work.

################################################
More information and tips about the project at:
code2control.wordpress.com/2023/01/01/updating-inputs-in-a-raspberry-pi-webserver-using-flask-python-and-jquery/
