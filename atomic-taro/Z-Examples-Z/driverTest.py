import matplotlib.pyplot as pyplot
import numpy as np
import math


def distance(x0, y0, x1, y1):
	return math.sqrt((x1-x0)**2 + (y1-y0)**2)

def computeAngle (p1, p2):
	dot = 0
	if computeNorm(p2[0], p2[1]) == 0 or computeNorm(p1[0], p1[1])==0:
		dot = 0
	else:
		dot = (p2[0]*p1[0]+p2[1]*p1[1])/float(computeNorm(p1[0], p1[1])*computeNorm(p2[0], p2[1]))
	if dot > 1:
		dot = 1
	elif dot < -1:
		dot = -1
	return math.acos(dot)*180/math.pi

def compute_AllAngles (trip):
	dV =  np.diff(trip, axis = 0) #x1-x0 and y1-y0
	angles = np.empty(shape = dV.shape[0])
	for i in range(1, trip.shape[0] - 1):
		ang = computeAngle(dV[i-1], dV[i])
		np.append(angles, [ang, dV[i][2]]) #append angle with timepoint
	return angles

def findStops(speeds):
	stops = [] #stops are a start and end time pair
	start = -1
	end = -1
	for i in range(1, len(speeds)):
		advS = (speeds[i] + speeds[i-1])/2 #smooth out noise in stop duration
		if speeds[i] == 0: #start of stop
			end = i
			if start == -1:
				start = i
		elif (start > -1) and (advS > 1):
			stops.append([start,end])
			start = -1
			end = -1
	if start > -1:
		stops.append([start, len(speeds)])
	return stops



def printHist_Feature(hist):
	h = ""
	for i in range(len(hist)-1):
		h += str(hist[i])+","
	#to avoid final comma (will mess up input)
	h += str(hist[len(hist)-1])
	return h


def computeNorm(p1, p2):
	return p1/(p1 + p2)


print "54.0421"
