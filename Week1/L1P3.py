
PATH_TO_FILE = 'C:/Users/SSD_Ezreal/Desktop/P/6002x/Week1/julyTemps.txt'

import pylab
import numpy as np

def loadFile():
    inFile = open(PATH_TO_FILE)
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)
    
def producePlot(lowTemps, highTemps):
    diffTemps = list(np.array(highTemps) - np.array(lowTemps))
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()
    
        
(low, high) = loadFile()    
producePlot(low, high)