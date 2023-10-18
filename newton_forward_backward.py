# NEWTON'S FORWARD INTERPOLATION

import matplotlib.pyplot as plt
from sympy import *
import numpy as np

def createTable(x, y, n, table):
  for col in range(1, n):
      for row in range(n-col):
          table[row][col] = round(table[row+1][col-1]-table[row][col-1], 2)
  return table

def calculate(u, n):
  temp = u
  for i in range(1, n):
  	temp = temp*(u-i)
  print(temp)
  return temp

def fact(n):
    f = 1
    for i in range(2, n+1):
    	f *= i
    return f

#xVal = list(map(float, input("Enter x values : ").split()))
#yVal = list(map(float, input("Enter y values : ").split()))
xVal = [0.96, 0.98, 1.00, 1.02, 1.04]
yVal = [0.7825, 0.7739, 0.7651, 0.7563, 0.7473]
x, y = symbols('x y')
n = len(xVal)

table = [[0.0 for i in range(n)] for i in range(n)]
for i in range(n):
	table[i][0] = yVal[i]

table = createTable(xVal, yVal, n, table)
for row in table:
	print(row)

inp1 = float(input("Value to interpolate at (first) : "))
inp2 = float(input("Value to interpolate at (second) : "))

y = table[0][0]
u = (x-xVal[0])/(xVal[1]-xVal[0])

for i in range(1, n):
	y += (((calculate(u, i))*(table[0][i])) / fact(i));

pol = simplify(y)
print("Polynomial : ", pol)
res1 = pol.subs(x, inp1)
print("Result 1 : ", res1)

res2 = pol.subs(x, inp2)
print("Result 2 : ", res2)

xPts = np.linspace(min(xVal), max(xVal), 100)
yPts = []

for p in xPts:
  yPts.append(pol.subs(x, p))

xVal.extend((inp1, inp2))
yVal.extend((res1, res2))
ax, fig = plt.subplots()
plt.plot(xPts, yPts)
plt.scatter(xVal, yVal, color='red')

firstDiff = diff(pol)
secondDiff = diff(firstDiff)

print("First Derivative : ", firstDiff)
print("Second Derivative : ", secondDiff)

print("At point ", inp1)
res1 = firstDiff.subs(x, inp1)
print("Result - 1 : ", res1)

res2 = secondDiff.subs(x, inp1)
print("Result - 2 : ", res2)

print("\nAt point ", inp2)
res1 = firstDiff.subs(x, inp2)
print("Result - 1 : ", res1)

res2 = secondDiff.subs(x, inp2)
print("Result - 2 : ", res2)



'''
# NEWTON'S BACKWARD INTERPOLATION
import matplotlib.pyplot as plt
from sympy import *
import numpy as np


def creatreTable(x, y, n, table):
	for i in range(1, n):
  	for j in range(n-1, i-1, -1):
    	table[j][i] = table[j][i-1] - table[j-1][i-1]
	return table


def calculate(u, n):
	temp = u
	for i in range(1, n):
    	temp = temp * (u + i)
	return temp


def fact(n):
	f = 1
	for i in range(2, n+1):
    	f *= i
	return f


xVal = list(map(float, input("x values : ").split()))
yVal = list(map(float, input("y values : ").split()))
x, y = symbols('x y')
n = len(xVal)


table = [[0.0 for i in range(n)] for i in range(n)]
for i in range(n):
	table[i][0] = yVal[i]


table = createTable(xVal, yVal, n, table)


for row in table:
	print(row)


inp = float(input("Value to interpolate at : "))
y = table[n-1][0]
u = (x - xVal[n-1]) / (xVal[1] - xVal[0])


for i in range(1, n):
	y += (((calculate(u, i)) *(table[n-1][i])) / fact(i))


pol = simplify(y)
res = pol.subs(x, inp)
print("Result : ", res)


xPts = np.linspace(min(xVal), max(xVal), 100)
yPts = []


for pt in x_pts:
	yPts.append(pol.subs(x, pt))


xVal.append(inp)
yVal.append(res)


fig, ax = plt.subplots()
plt.plot(xPts, yPts)
plt.scatter(xVal, yVal, color='red')


firstDiff = diff(pol)
res1 = firstDiff.subs(x, inp)
print(" Result - 1 : ", res1)


secondDiff = diff(firstDiff)
res2 = secondDiff.subs(x, inp)
print("Result - 2 : ", res2)

'''
