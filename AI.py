from NQueen import GeneticNQueen
from SalesMan import SalesMan
from MaximumFunction import Maximumfunction
import random
from math import exp
import matplotlib.pyplot as plt

def f(x, y):
  return 3 * (1-x)**2 * exp(-x**2 - (y+1)**2)\
     - 10*(x/5 - x**3 - y**5) * exp(-x**2 - y**2)\
        - 1/3 * exp(-(x+1)**2 - y**2)

max_nqueen = 15
max_salesman = 15
max_maxfunction = 10

with open('GA_report_nqueen.txt', 'w') as f:
  f.truncate(0)
with open('GA_report_salesman.txt', 'w') as f:
  f.truncate(0)
with open('GA_report_maxfunction.txt', 'w') as f:
  f.truncate(0)

for n in range(8, max_nqueen):
  nqueen = GeneticNQueen(n)
  nqueen.reportGASolverTime()

for n in range(10, max_salesman):
  m = 50
  salesman = SalesMan(1000, n, m, 0.3)
  salesman.calculate(3000)
for n in range(1, max_maxfunction):
  mx = Maximumfunction(f, iterations=n*100)
  mx.run()
print("--------------------")
x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []
with open('GA_report_nqueen.txt', 'r') as nq:
  with open('GA_report_salesman.txt', 'r') as sa:
    with open('GA_report_maxfunction.txt', 'r') as mf:
      for line in nq.readlines():
        x, y = line.split(' ')
        x = int(x)
        y = float(y)
        x1.append(x)
        y1.append(y)
      for line in sa.readlines():
        x, y = line.split(' ')
        x = int(x)
        y = float(y)
        x2.append(x)
        y2.append(y)
      for line in mf.readlines():
        x, y = line.split(' ')
        x = int(x)
        y = float(y)
        x3.append(x)
        y3.append(y)
      fig, axs = plt.subplots(3)
      axs[0].plot(x1, y1)
      axs[1].plot(x2, y2)
      axs[2].plot(x3, y3)
      plt.show()
