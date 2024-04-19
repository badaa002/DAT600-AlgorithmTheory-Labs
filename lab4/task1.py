# The pulp package needs to be installed before running the code, 
# this can be done through running pip install pulp in the terminal

# Imports the package
from pulp import *

# Call the model Task 1
model = LpProblem('Task 1', LpMaximize)

# Set the decision variables as x and y, where x has a lowbound of 10 due to the customers requirement
x = LpVariable('X', lowBound = 10, cat = 'Integer')
y = LpVariable('Y', lowBound = 0, cat = 'Integer')

# Objective function
model +=  168.4*x+257*y

# Constraints
model += 0.25*x+0.33*y <= 40
model += 0.33*x+0.5*y <= 35

# Solve the problem
model.solve()