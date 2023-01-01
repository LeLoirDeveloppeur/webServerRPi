from flask import Flask, render_template, send_from_directory
import RPi.GPIO as GPIO

## Setting GPIO MODE
GPIO.setmode(GPIO.BCM)

##Input assignment to BCM mapped pins.
GPI4 = 4
GPI17 = 17
GPI27 = 27
GPI22 = 22
GPI5 = 5
GPI6 = 6
GPI13 = 13
GPI19 = 19 

## Arranging the inputs in an array list to make it easier to go through all inputs
INPUT_LIST = [ GPI4, GPI17, GPI27, GPI22, GPI5, GPI6, GPI13, GPI19]
## Setting as an input the inputs we defined
for GPI_X in INPUT_LIST:
    GPIO.setup(GPI_X,GPIO.IN)

#############################################
##          Flask part mircroservice         
#############################################

## Create a folder STATIC on the app.py main folder so we have
## the following structure:
## In my case:
## /home/pi
## app.py
## static --> image1.png, image2.png, .. imageN.png
## templates -->index.html

app = Flask(__name__, static_folder='static')

## Folder where index.html is
@app.route('/')
def index():
    templateData= {
            'GPIO4':GPIO.input(GPI4),
            'GPIO17': GPIO.input(GPI17),
            'GPIO27': GPIO.input(GPI27),
            'GPIO22': GPIO.input(GPI22),
            'GPIO5':GPIO.input(GPI5),
            'GPIO6':GPIO.input(GPI6),
            'GPIO13': GPIO.input(GPI13),
            'GPIO19': GPIO.input(GPI19)
        }
    return render_template("index.html", **templateData)
      

## Get request from the client to get the CenterLogo.png
@app.route('/CenterLogo.png', methods=['GET'])
def centerLogo():
    return send_from_directory("static", "CenterLogo.png")
    
## Get request from the client to get the leftLogo.png
@app.route('/leftLogo.png', methods=['GET'])
def rPILogo():
    return send_from_directory("static", "leftLogo.png")   

## Get request from the client to get the RightLogo.png
@app.route('/RightLogo.png', methods=['GET'])
def rightLogo():
    return send_from_directory("static", "RightLogo.png")   


@app.route('/getGPIO')
def getGPIO():
    templateData= {
            'GPIO4':GPIO.input(GPI4),
            'GPIO17': GPIO.input(GPI17),
            'GPIO27': GPIO.input(GPI27),
            'GPIO22': GPIO.input(GPI22),
            'GPIO5':GPIO.input(GPI5),
            'GPIO6':GPIO.input(GPI6),
            'GPIO13': GPIO.input(GPI13),
            'GPIO19': GPIO.input(GPI19)
        }
    return templateData

if __name__ == "__main__":
    app.run(debug=True)


    
## Remember to run the app like this: flask run --host=0.0.0.0
## in my case, in case of not doing it in this manner it didn't work at all.
