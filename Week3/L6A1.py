import random
import pylab
def makeNormal(mean,sd,numSamples):
    samples = []
    for i in range(numSamples):
        samples.append(random.gauss(mean,sd))
    pylab.hist(samples, bins =101)
  
def clear(n,clearProb,steps):
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-clearProb)**t))
    pylab.plot(numRemaining, label='Exponential Decay')


def clearSim(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numLeft = numRemaining[-1]
        for m in range(numRemaining[-1]):
            if random.random() <= clearProb: 
                numLeft -= 1
        numRemaining.append(numLeft)
    pylab.plot(numRemaining, 'ro', label = 'Simulation')

clear(10000, 0.01, 1000)
clearSim(10000, 0.01, 1000)
pylab.xlabel('Number of Steps')
pylab.ylabel('Number of Molecules')
pylab.legend()
pylab.show()


#clear(1000,0.01,1000)
#pylab.xlabel('Number of Steps')
#pylab.ylabel('Number of Molecules')
#pylab.title('Clearance of Molecules')
#pylab.semilogy() # log y
#pylab.show()

#makeNormal(0.0,1.0,100000)
#pylab.show()