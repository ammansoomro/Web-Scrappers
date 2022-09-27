
from sympy import symbols, Eq, solve
import sympy as sym
import numpy as np

# defining symbols used in equations or unknown variables
x,y = symbols('x y')

#base = 15000 hr/years
#expo_rate = 0.9 per year
#end = 3000 hr/years

My_Initial_Equation = 15000*(0.9)**x
print("Machine Eq :", My_Initial_Equation)

eq_2 = solve([Eq(y, My_Initial_Equation), Eq(y, 3000)])
print("Machine will replace in :", eq_2[0][x], "years")

#1 Year have 8760hrs
eq_3 = solve([Eq(y, My_Initial_Equation), Eq(y, 8760)])
print("It can work more than 8760 until year", eq_3[0][x], '\n')

end_hour1 = (8760*eq_3[0][x])
print("End hour1 :", end_hour1, 'hours \n')
end_hour2 = sym.integrate(My_Initial_Equation, (x, eq_3[0][x], eq_2[0][x]))
print("End hour2 :", end_hour2, 'hours \n')
# Adding two hours together
total_end_hour = np.add(end_hour1, end_hour2)
print("It will need to work", total_end_hour, "hours until it will need to be replace.")

# Plotting the Bar Graph using Hours and Years
My_Graph = sym.plot(My_Initial_Equation, (x, 0, 17), show=False, markers = [{'args': [((total_end_hour/8760)), (3000), 'ro']}])
My_Graph.show() 