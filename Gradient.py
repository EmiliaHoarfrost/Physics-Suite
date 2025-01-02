#Import sympy to perform symbolic mathematics.
import sympy as sym

#Create cartesian gradient function taking 3 parameters x, y and z.
def gradient_3d_cartesian(x_argument, y_argument, z_argument):
    #Perfom symbolic differentiation.
    x_1=sym.diff(x_argument, x)
    y_1=sym.diff(y_argument, y)
    z_1=sym.diff(z_argument, z)
    return x_1, y_1, z_1

#Create cylindrical gradient function taking 3 parameters p, theta and z.
def gradient_3d_cylindrical(rho_argument, theta_argument, z_argument):
    #Perfom symbolic differentiation.
    rho_1=sym.diff(rho_argument, rho)
    theta_1=(1/rho)*sym.diff(theta_argument, theta)
    z_1=sym.diff(z_argument, z)
    return rho_1, theta_1, z_1

#Create cylindrical gradient function taking 3 parameters p, theta and z.
def gradient_3d_spherical(r_argument, theta_argument, phi_argument):
    #Perfom symbolic differentiation.
    r_1=sym.diff(r_argument, r)
    theta_1=(1/rho)*sym.diff(theta_argument, theta)
    phi_1=(1/(r*sym.sin(theta)))*sym.diff(phi_argument, phi)
    return r_1, theta_1, phi_1

#Define Symbols /!\ Caution these are not variables in a Python sense but in a mathematical one hence the use of Symbol() function !
x=sym.Symbol('x')
y=sym.Symbol('y')
z=sym.Symbol('z')
rho=sym.Symbol('rho')
theta=sym.Symbol('theta')
r=sym.Symbol('r')
phi=sym.Symbol('phi')

#Gradient calculated here using parsed data form user :
