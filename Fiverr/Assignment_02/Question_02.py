# importing library sympy
import sympy as sym
# defining symbols used in equations or unknown variables
t = sym.symbols('t')

val1 = int(input("Enter the base value: "))
val2 = int(input("Enter the exponential rate: "))
val3 = int(input("Enter the end value: "))


equation_1 = val1*t + val2*t**2
change = val3

# defining equations
eq_1 = sym.Eq(equation_1, change)
print("Equation 1: ", eq_1)

# solving the equation and printing the value of unknown variables
(a,b) = sym.solve(eq_1)
print("Value of t:", sym.solve(eq_1)) 
# plotting the graph for eq_1 and change
line = sym.plot(equation_1,  show=False)
parabola = sym.plot(change, show=False)
line.append(parabola[0])
line.show()