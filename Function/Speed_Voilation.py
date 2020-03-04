import os
import pandas as pd

def speed_violation(speed,GpsTime, Latitude,Longitude,Threshold_Speed):
	SPEED_VIOLATION = []
	GPS_TIME = []
	
	for i in speed.index:
		if speed[i]== '-' :
			speed[i]=0
		if (float(speed[i])>Threshold_Speed):
			SPEED_VIOLATION.append([Latitude[i],Longitude[i],GpsTime[i],speed[i],i])
	VIOLATION = pd.DataFrame(data=SPEED_VIOLATION, columns=['Latitude', 'Longitude','GPS_Time','Speed','Index'])
	return VIOLATION




