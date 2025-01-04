#Import sympy to perform symbolic mathematics.
import sympy as sym

#Define Symbols /!\ Caution these are not variables in a Python sense but in a mathematical one hence the use of Symbol() function !
x, y, z, rho, theta, r, phi, i = sym.symbols('x, y, z, rho, theta, r, phi, i')

Metri_Cartesian=sym.Matrix([1,1,1])
Metric_Cartesian=sym.Matrix([[1,0,0], [0,1,0], [0,0,1]])
Metric_Cylindrical=sym.Matrix([[1,0,0], [0,rho,0], [0,0,1]])
Metric_Spherical=sym.Matrix([[1,0,0], [0,r,0], [0,0,r*sym.sin(theta)]])

def gradient(x_arg,y_arg,z_arg, dim, mode):
    var = sym.Matrix([x_arg,y_arg,z_arg])
    dvar_0 = sym.Matrix([x, y, z])
    dvar_1 = sym.Matrix([rho, theta, z])
    dvar_2 = sym.Matrix([r, theta, phi])
    Grad=sym.zeros(3,1)
    if mode==0:
        for k in range(dim):
            Grad[k,0]=1/Metric_Cartesian[k,k]*sym.diff(var[k,0], dvar_0[k,0])
    if mode==1:
        for k in range(dim):
            Grad[k,0]=1/Metric_Cylindrical[k,k]*sym.diff(var[k,0], dvar_1[k,0])
    if mode==2:
        for k in range(dim):
            Grad[k,0]=1/Metric_Spherical[k,k]*sym.diff(var[k,0], dvar_2[k,0])
    return sym.simplify(Grad)

def divergence(x_arg,y_arg,z_arg, dim, mode):
    Grad=sym.zeros(3,1)
    var = sym.Matrix([x_arg,y_arg,z_arg])
    dvar_0 = sym.Matrix([x, y, z])
    dvar_1 = sym.Matrix([rho, theta, z])
    dvar_2 = sym.Matrix([r,theta, phi])
    if mode==0:
        for k in range(dim):
            Grad[k,0]=1/Metric_Cartesian.det()*sym.diff(Metric_Cartesian.det()*(var[k,0]*Metric_Cartesian[k,k]**(-1)), dvar_0[k,0])
    if mode==1:
        for k in range(dim):
            Grad[k,0]=1/Metric_Cylindrical.det()*sym.diff(Metric_Cylindrical.det()*(var[k,0]*Metric_Cylindrical[k,k]**(-1)), dvar_1[k,0])
    if mode==2:
        for k in range(dim):
            Grad[k,0]=1/Metric_Spherical.det()*sym.diff(Metric_Spherical.det()*(var[k,0]*Metric_Spherical[k,k]**(-1)), dvar_2[k,0])
    return sym.simplify(Grad[0,0]+Grad[1,0]+Grad[2,0])

def divergence_spherical(x_arg,y_arg,z_arg):
    Div=(1/r**2)*sym.diff(r**2*x_arg, r)+(1/r*sym.sin(y_arg))*sym.diff(sym.sin(theta)*y_arg)+(1/r*sym.sin(y_arg))*sym.diff(z_arg)
    return sym.simplify(Div)

X=rho**2
Y=theta**2
Z=z**2


print(divergence(X,Y,Z,3,1))