#Solution for possibility restaurant
# import pulp
import pulp as p 

import numpy as np
import matplotlib.pyplot as plt
  
# Create the Maximization problem 
Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
  
# Variables  
x = p.LpVariable("x", lowBound = 0)  #beef
y = p.LpVariable("y", lowBound = 0)  #fish
  
# Objective Function 
Lp_prob += 16 * x + 12 * y    #profit
  
# Constraints: 
Lp_prob += x + y <= 60                                              # total amount of dish they can prepare
Lp_prob += 15 * y + 30 * x <= 1200                                  # time they have to prepapare dishes in terms of minute
Lp_prob += 2 * y - 3 * x >= 0                                       # 3 fish dishes for 2 beef dishes 
Lp_prob += 9 * x - y >= 0                                           # t least 10 percent beef dishes

# Display 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 
  
# Printing the final solution 
print(p.value(x), p.value(y), p.value(Lp_prob.objective))
print("\n") #a line gap
# Printing the final solution, cool and stuff
print("Number of beef dishes that will be prepared is: ",int(p.value(x)))
print("Number of fish dishes that will be prepared is: ",int(p.value(y)))
print("Overall profit is: ",int(p.value(Lp_prob.objective)),"$")

#to plot the graph
x = np.linspace(0, 200, 200)
y1 = 60 - x                         # total amount of dish they can prepare
y2 = (1200 - 30 * x)/15             # time they have to prepapre dishes in terms of minute
y3 =  (3/2) * x                     # 3 fish dishes for 2 beef dishes 
y4 =  9 * x                         # t least 10 percent beef dishes
 
plt.plot(x, y1, label=r'$y\leq60-x$')
plt.plot(x, y2, label=r'$y\leq80-2x$')
plt.plot(x, y3, label=r'$y\geq 1.5x$')
plt.plot(x, y4, label=r'$y\leq 9x$')
plt.xlim((0, 80))
plt.ylim((0, 80))
plt.xlabel(r'$beef$')
plt.ylabel(r'$fish$')
# Fill feasible region           
y5 = np.minimum(y1, y2) 
y6 = y3
plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)