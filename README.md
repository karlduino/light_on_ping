## Ping servers

I'm using a raspberry pi to monitor 3 routers:

- Simply ping them at some interval and light up green or red LEDs
  according to whether successful or not

- I'm using an old Raspberry Pi Model B revision 2011.12. 
  The GPIO is 13x2

  - pins numbered (1,2),(3,4), ... going down
  - 3.3 power at pins 1 and 17
  - ground at pins 6, 9, 14, 20, 25
  - pin 7 = GPIO4
  - pin 13 = GPIO27
  - pin 15 = GPIO22
  - pin 16 = GPIO23
  - pin 18 = GPIO24
  - pin 22 = GPIO25
  - also a bunch more but they double for I2C, SPI, and UART

![old pi pinout](https://howto8165.files.wordpress.com/2014/08/rpi-pinout.png)
