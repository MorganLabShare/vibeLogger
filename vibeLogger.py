import time
import matplotlib.pyplot as plt

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import datetime

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

#set up the plot values
#~ curVals=range(1024)
#~ curVals=curVals[-200:]
curVals=[]

#set plot to interactive
#~ plt.ion()

#Get the current time at the beginning of the log
startTime = datetime.datetime.now()

#Make a file name for the log file
logFilename=startTime.strftime("/home/pi/MorganLab/%Y-%m-%d_%H-%M-%S.txt")
print(logFilename)

#open a log file for writing data
vibeLog = open(logFilename, "w")

vibeLog.write("Log Start: "+logFilename+"\n")

#Set up the plot
#~ ax1=plt.axes()
#~ plot1,=plt.plot(curVals)

#~ iterator=1
startClock=time.time()

# Main loop
while True:
	if time.time() - startClock > 60:
		nowTime=datetime.datetime.now()
		#~ vibeLog.write(curVals)
		for Val in curVals:
			vibeLog.write("%s\n" % Val)
		vibeLog.write(nowTime.strftime("%Y-%m-%d_%H:%M:%S")+"\n")
		vibeVal=mcp.read_adc(0)
		#~ noiseVal=mcp.read_adc(7)
		#~ curVals=curVals[1:]
		curVals=[]
		curVals.append(vibeVal)
		#~ plt.cla()
		#~ plot1,=plt.plot(curVals)
		#~ plt.draw()
		startClock=time.time()
	else:
		vibeVal=mcp.read_adc(0)
		#~ noiseVal=mcp.read_adc(7)
		#~ curVals=curVals[1:]
		curVals.append(vibeVal)
		#~ plot1.set_ydata(curVals)
		#~ plt.draw()
	time.sleep(0.1)
	#~ iterator += 1

