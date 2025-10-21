import numpy as np
import sympy as sp

''' EJERCICIO 1 '''
# Definición de matrices
A = np.array([[1, 0, 2],
              [2, 1, 1],
              [3, 2, 0]])

B = np.array([[0, 1, 1],
              [1, 2, 0],
              [2, 1, 3]])


# Parte 1:
# Producto cruz
producto = np.cross(A, B)


# Parte 2:
# Traspuesta y determinante de A
traspuesta_A = A.T
determinante_A = np.linalg.det(A)


print("A × B =\n", producto)
print("\nTraspuesta de A =\n", traspuesta_A)
print("\nDeterminante de A =", determinante_A)




''' Ejercicio 2 '''
# Definición de vectores
u = np.array([2, -1, 3])
v = np.array([1, 4, -2])

# Parte 1:
# Producto interno
producto_interno = np.dot(u, v)

# Normas de los vectores
norma_u = np.linalg.norm(u)
norma_v = np.linalg.norm(v)

# Verificación de ortogonalidad
ortogonales = producto_interno == 0


# Parte 2:
# Ángulo entre u y v (en radianes y grados)
angulo_rad = np.arccos(producto_interno / (norma_u * norma_v))
angulo_deg = np.degrees(angulo_rad)


print("u · v =", producto_interno)
print("¿Son ortogonales?", ortogonales)
print("Ángulo entre u y v =", angulo_rad, "rad =", angulo_deg, "°")




''' Ejercicio 3 '''
# Definición de variables simbólicas
x, y = sp.symbols('x y')

# Función g(x, y)
g = x**2 * y + sp.sin(x*y)


# Parte 1:
# Derivadas parciales
dg_dx = sp.diff(g, x)
dg_dy = sp.diff(g, y)


# Parte 2:
# Evaluación en (x=1, y=π/2)
punto = {x: 1, y: sp.pi/2}
valor_dx = dg_dx.evalf(subs=punto)
valor_dy = dg_dy.evalf(subs=punto)


print("∂g/∂x =", dg_dx)
print("∂g/∂y =", dg_dy)
print("\nEvaluación en (1, π/2):")
print("∂g/∂x =", valor_dx)
print("∂g/∂y =", valor_dy)
