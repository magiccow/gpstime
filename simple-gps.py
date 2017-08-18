import serial
import re


def nmea(line):
	parts = line.split(",")
	if parts[0]=='$GPGGA':
		gga(parts)
	

def gga(parts):
	# extract the time
	match = re.match('(\d\d)(\d\d)(\d\d)\.(\d\d\d)',parts[1])
	if match:
		h = match.group(1)
		m = match.group(2)
		s = match.group(3)
		print("Time is %s:%s:%s UTC" % (h,m,s))


ser = serial.Serial('/dev/rfcomm1', timeout=2) 
line = ""
while True:
	ch = ser.read()
	if ch=='\r':
		nmea(line)
		line = ""
		ch = ser.read()   # get the newline
	else:
		line = line + ch


