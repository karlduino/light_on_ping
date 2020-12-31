#!/usr/bin/env python3

from gpiozero import LED
import platform   # for getting operating system name
import subprocess # for executing a shell command
from time import sleep

green1 = 20
red1   = 21

green2 = 25
red2   = 12

green3 = 23
red3   = 24

def ping(host):
    """
    Returns True if host (str) responds to a ping request
    """

    # Option for the number of packets
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Build the command
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def light_on_ping(host, green_led, red_led):
    if ping(host):
        green_led.on()
        red_led.off()
    else:
        green_led.off()
        red_led.on()

host1 = '192.168.0.1'
led_green1 = LED(green1)
led_red1 = LED(red1)

host2 = '192.168.0.2'
led_green2 = LED(green2)
led_red2 = LED(red2)

host3 = '192.168.0.3'
led_green3 = LED(green3)
led_red3 = LED(red3)

while True:
    light_on_ping(host1, led_green1, led_red1)
    light_on_ping(host2, led_green2, led_red2)
    light_on_ping(host3, led_green3, led_red3)
    sleep(10)
