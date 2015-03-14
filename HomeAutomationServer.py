# -*- coding: utf-8 -*-
"""
    Home Automation Server
    ~~~~~~~~~~~~~~~~~~~~~~

    A simple application that allows home automation
    python scripts to be executed from a web browser.

    @author: Jacob Friedmann
    @date: 2015-03-09
    @license: MIT
"""
import time
import picamera
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import os
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/garage_door')
def garage_door():
    """Opens the garage door and takes a picture to show state"""

    date_string = time.strftime("%Y-%m-%d-%H:%M:%S")

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(23, GPIO.IN)
    # activate input with PullUp
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.output(24, GPIO.LOW)
    # GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    sleep(15)
    
    status = "closed"
    if GPIO.input(23):
        status = "opened"

    with picamera.PiCamera() as camera:
        print "before pic"
        # camera.capture('/home/pi/Pictures/relay_on{counter:02d}.jpg')
        camera.capture('/home/pi/Pictures/doorposition' + date_string + '.jpg')
        print "after pic"
        sleep(3)

        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

    GPIO.cleanup()
    return jsonify(result="Garage door " + status + " succesfully!")

@app.route('/ac_on')
def ac_on():
    """Turns on the nest ac (an example of what adding additional
        functionality could look like"""
    #INSERT CODE HERE
    return jsonify(result="AC turned on succesfully!")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)