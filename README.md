# gpstime
Python script to get NMEA GGA message from GPS and extract the time.

The example depends on PySerial, so install with

pip install pyserial

Uses port /dev/rfcomm1, which in my case was bound to a Bluetooth port and the BT-338 bluetooth GPS.

The example only processes the GPGGA stanza to extract the UTC time.


