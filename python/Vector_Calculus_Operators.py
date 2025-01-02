#Import sympy to perform symbolic mathematics.
import sympy as sym

#Create cartesian nabla function taking 3 parameters x, y and z.
def nabla_3d_cartesian(x_argument, y_argument, z_argument):
    #Perfom symbolic differentiation.
    x_1=sym.diff(x_argument, x)
    y_1=sym.diff(y_argument, y)
    z_1=sym.diff(z_argument, z)
    return x_1, y_1, z_1

#Create cylindrical nabla function taking 3 parameters p, theta and z.
def nabla_3d_cylindrical(rho_argument, theta_argument, z_argument):
    #Perfom symbolic differentiation.
    rho_1=sym.diff(rho_argument, rho)
    theta_1=(1/rho)*sym.diff(theta_argument, theta)
    z_1=sym.diff(z_argument, z)
    return rho_1, theta_1, z_1

#Create spherical nabla function taking 3 parameters p, theta and phi.
def nabla_3d_spherical(r_argument, theta_argument, phi_argument):
    #Perfom symbolic differentiation.
    r_1=sym.diff(r_argument, r)
    theta_1=(1/rho)*sym.diff(theta_argument, theta)
    phi_1=(1/(r*sym.sin(theta)))*sym.diff(phi_argument, phi)
    return r_1, theta_1, phi_1

#Create cartesian laplacian function taking 3 parameters x, y and z.
def laplacian_3d_cartesian(x_argument, y_argument, z_argument):
    #Perfom symbolic differentiation.
    x_2=sym.diff(x_argument, x, 2)
    y_2=sym.diff(y_argument, y, 2)
    z_2=sym.diff(z_argument, z ,2)
    return x_2, y_2, z_2

#Create cylindrical laplacian function taking 3 parameters rho, theta and z.
def laplacian_3d_cylindrical(rho_argument, theta_argument, z_argument):
    #Perfom symbolic differentiation.
    rho_2=(1/rho)*sym.diff(rho*sym.diff(rho_argument, rho), rho)
    theta_2=(1/(rho**2))*sym.diff(theta_argument, theta, 2)
    z_2=sym.diff(z_argument, z ,2)
    return rho_2, theta_2, z_2

#Create spherical laplacian function taking 3 parameters r, theta and phi.
def laplacian_3d_spherical(r_argument, theta_argument, phi_argument):
    #Perfom symbolic differentiation.
    r_2=(1/r**2)*sym.diff(r**2*sym.diff(r_argument, r), r)
    theta_2=(1/((r**2)*sym.sin(theta)))*sym.diff(sym.sin(theta)*sym.diff(theta_argument, theta), theta)
    phi_2=(1/(r**2*sym.sin(theta)**2))*sym.diff(phi_argument, phi ,2)
    s=r_2+theta_2+phi_2
    return r_2, theta_2, phi_2

#Define Symbols /!\ Caution these are not variables in a Python sense but in a mathematical one hence the use of Symbol() function !
x=sym.Symbol('x')
y=sym.Symbol('y')
z=sym.Symbol('z')
rho=sym.Symbol('rho')
theta=sym.Symbol('theta')
r=sym.Symbol('r')
phi=sym.Symbol('phi')
