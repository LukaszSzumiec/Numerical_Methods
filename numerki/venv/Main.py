import conjugate_gradient_method
import chebyszev_iteration
import numpy as np

# Z = [[2, -1, 0],
#      [1, 2, -1],
#      [0, -1, 2]]
A = np.array([
    [4, 1],
    [1, 3]])

b = np.array([[1],
            [2]])

x0 = np.array([[0],
            [0]])

print(conjugate_gradient_method.solve_CG(A,b,x0))
print(chebyszev_iteration.solve_chebyshev(A, b, x0, 500, 0.58578643962, 3.41421356237))
