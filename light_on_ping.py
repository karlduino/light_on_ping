#!/usr/bin/env python3

from gpiozero import LED
import platform   # for getting operating system name
import subprocess # for executing a shell command
import os         # for devnull
from time import sleep

# wait time between pings
ping_wait = 40
startup_wait = 0.5

# hosts
host1 = '192.168.0.1'
host2 = '192.168.0.2'
host3 = '192.168.0.3'

# LED pins
green1 = 25    # (pin 22 on old raspberry pi with 13x2 layout)
red1   = 24    # (pin 18)

green2 = 23    # (pin 16)
red2   = 22    # (pin 15)

green3 = 27    # (pin 13)
red3   =  4    # (pin 7)


def ping(host):
    """
    Returns True if host (str) responds to a ping request
    """

    # Option for the number of packets
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Build the command
    command = ['ping', param, '3', host]

    with open(os.devnull, 'w') as DEVNULL:
        return subprocess.call(command, stdout=DEVNULL, stderr=DEVNULL) == 0

def light_on_ping(host, green_led, red_led):
    if ping(host):
        green_led.on()
        red_led.off()
    else:
        green_led.off()
        red_led.on()

def startup(leds, wait):
    for led in leds:
        led.on()
        sleep(wait)
    sleep(wait)
    for led in leds:
        led.off()
        sleep(wait)

led_green1 = LED(green1)
led_red1 = LED(red1)

led_green2 = LED(green2)
led_red2 = LED(red2)

led_green3 = LED(green3)
led_red3 = LED(red3)

startup([led_green1, led_green2, led_green3,
         led_red1, led_red2, led_red3], startup_wait)

wait_time = 0
while True:
    light_on_ping(host1, led_green1, led_red1)
    sleep(wait_time)

    light_on_ping(host2, led_green2, led_red2)
    sleep(wait_time)

    light_on_ping(host3, led_green3, led_red3)
    sleep(wait_time)

    wait_time = ping_wait
