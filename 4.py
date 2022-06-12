import sympy as sy

sy.init_printing()

# For function plot
from sympy.plotting import plot

# %% Some common variables
x = sy.symbols('x')

y = sy.Function('y')
y1 = sy.Derivative(y(x), x)
y2 = sy.Derivative(y(x), x, x)

# %% General solution

# Definition
eqdiff =  2*(y(x)-4)*y1 - x
print("step1")
# Solution
sol = sy.dsolve(eqdiff, y(x))
print("step2")
# Print
sy.pprint(sol)

print(sy.latex(sol))

x0 = sy.pi/4
sol = sy.dsolve(eqdiff, y(x), ics={y(x0): 0, y(x).diff(x).subs(x, x0): 0})
sy.pprint(sol)

# %% Plot

#title = sy.latex(sol.rhs)
#xtol = 1e-3
#p1 = plot(sol.rhs, (x,sy.pi/4,2*sy.pi), line_color='C0', show=False, 
#          xlim=[sy.pi/4,2*sy.pi], ylim=[-5,5], title=f"${title}$", legend=True, xlabel="", ylabel="")
#p1[0].label = '$y$'
#p2 = plot(sy.diff(sol.rhs,x), (x,sy.pi/4,2*sy.pi), line_color='C1', show=False, 
#          xlim=[sy.pi/4,2*sy.pi], ylim=[-5,5])
#p2[0].label = "$y\,'$"
#p1.extend(p2)
#p1.show()
