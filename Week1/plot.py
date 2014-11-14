import pylab
pylab.figure(1)
pylab.plot([1,2,3,4],[1,2,3,4])
pylab.figure(2)
pylab.plot([1,2,3,4],[1,2,3,4])
pylab.savefig('Figure-Eric')
pylab.plot([5,6,10,3])
pylab.savefig('Figure-Grimson')


principal = 10000
interestRate = 0.05
years = 20
values = []
for i in range(years +1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(range(years+1),values,'ro')
pylab.title('5% Growth, Compounded Annual Interest',fontsize=6)
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')
pylab.show()