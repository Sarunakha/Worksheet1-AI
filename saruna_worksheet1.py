# -*- coding: utf-8 -*-
"""Saruna_Worksheet1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14s1OgmGx77d-b5NdumO9-3uPpR-m_UD0

Problem - 1: Array Creation:

Complete the following Tasks:
1. Initialize an empty array with size 2X2.
2. Initialize an all one array with size 4X2.
3. Return a new array of given shape and type, filled with fill value.{Hint: np.full}
4. Return a new array of zeros with same shape and type as a given array.{Hint: np.zeros like}
5. Return a new array of ones with same shape and type as a given array.{Hint: np.ones like}
6. For an existing list new_list = [1,2,3,4] convert to an numpy array.{Hint: np.array()}
"""

import numpy as np
empty_array = np.empty((2, 2));
print(empty_array)

import numpy as np
all_one_array = np.ones((4, 2));
print(all_one_array)

import numpy as np
new_array = np.full((2, 2), 5);
print(new_array)

import numpy as np
array = np.array([1, 2, 3, 4]);
new_array = np.zeros_like(array);
print(new_array)

import numpy as np
array = np.array([1, 2, 3, 4]);
new_array = np.ones_like(array);
print(new_array)

import numpy as np
list = [1, 2, 3, 4];
array = np.array(list);
print(array)

"""Problem - 2: Array Manipulation: Numerical Ranges and Array indexing:

Complete the following tasks:
1. Create an array with values ranging from 10 to 49. {Hint:np.arrange()}.
2. Create a 3X3 matrix with values ranging from 0 to 8.
{Hint:look for np.reshape()}
3. Create a 3X3 identity matrix.{Hint:np.eye()}
4. Create a random array of size 30 and find the mean of the array.
{Hint:check for np.random.random() and array.mean() function}
5. Create a 10X10 array with random values and find the minimum and maximum values.
6. Create a zero array of size 10 and replace 5th element with 1.
7. Reverse an array arr = [1,2,0,0,4,0].
8. Create a 2d array with 1 on border and 0 inside.
9. Create a 8X8 matrix and fill it with a checkerboard pattern.
"""

import numpy as np
array = np.arange(10, 50);
print(array)

import numpy as np
array = np.arange(0, 9).reshape(3, 3);
print(array)

import numpy as np
array = np.eye(3);
print(array)

import numpy as np
array = np.random.random(30);
mean = array.mean();
print(mean)

import numpy as np
array = np.random.random((10, 10));
min_value = array.min();
max_value = array.max();
print(min_value, max_value)

import numpy as np
array = np.zeros(10);
array[4] = 1;
print(array)

import numpy as np
arr = np.array([1, 2, 0, 0, 4, 0]);
non_zero_indices = np.nonzero(arr);
reversed_arr = arr[non_zero_indices[::-1]]
print(reversed_arr)

import numpy as np
array = np.ones((5, 5));
array[1:-1, 1:-1] = 0;
print(array)

import numpy as np
array = np.zeros((8, 8));
array[1::2, ::2] = 1;
array[::2, 1::2] = 1;
print(array)

"""Problem - 3: Array Operations:

For the following arrays:

x = np.array([[1,2],[3,5]]) and y = np.array([[5,6],[7,8]]);

v = np.array([9,10]) and w = np.array([11,12]);

Complete all the task using numpy:
1. Add the two array.
2. Subtract the two array.
3. Multiply the array with any integers of your choice.
4. Find the square of each element of the array.
5. Find the dot product between: v(and)w ; x(and)v ; x(and)y.
6. Concatenate x(and)y along row and Concatenate v(and)w along column.
{Hint:try np.concatenate() or np.vstack() functions.
7. Concatenate x(and)v; if you get an error, observe and explain why did you get the error?
"""

import numpy as np
x = np.array([[1, 2], [3, 5]]);
y = np.array([[5, 6], [7, 8]]);
add = np.add(x, y);
v = np.array([9,10]);
w = np.array([11,12]);
add1 = np.add(v, w);
print(add)
print(add1)

import numpy as np
x = np.array([[1, 2], [3, 5]]);
y = np.array([[5, 6], [7, 8]]);
subtract = np.subtract(x, y);
v = np.array([9,10]);
w = np.array([11,12]);
subtract1 = np.subtract(v, w);
print(subtract)
print(subtract1)

import numpy as np
x = np.array([[1, 2], [3, 5]]);
y = np.array([[5, 6], [7, 8]]);
multiply = np.multiply((x, y), 5);
v = np.array([9,10]);
w = np.array([11,12]);
multiply1 = np.multiply((v, w), 6);
print(multiply)
print(multiply1)

import numpy as np
x = np.array([[1, 2], [3, 5]]);
y = np.array([[5, 6], [7, 8]]);
square = np.square(x);
square1 = np.square(y);
v = np.array([9,10]);
w = np.array([11,12]);
square2 = np.square(v);
square3 = np.square(w);
print(square)
print(square1)
print(square2)
print(square3)

import numpy as np
x = np.array([[1, 2], [3, 5]]);
y = np.array([[5, 6], [7, 8]]);
dot_product = np.dot(x, y);
v = np.array([9,10]);
w = np.array([11,12]);
dot_product1 = np.dot(v, w);
x = np.array([[1, 2], [3, 5]]);
v = np.array([9,10]);
dot_product2 = np.dot(x, v);
print(dot_product)
print(dot_product1)
print(dot_product2)

import numpy as np
x = np.array([[1, 2], [3, 5]]);
y = np.array([[5, 6], [7, 8]]);
concatenate = np.concatenate((x, y), axis=1);
v = np.array([9,10]);
w = np.array([11,12]);
concatenate1 = np.concatenate((v, w), axis = 0);
print(concatenate)
print(concatenate1)

import numpy as np
x = np.array([[1, 2], [3, 5]]);
v = np.array([9,10]);
concatenate = np.concatenate(x, v);
print(concatenate)
#

"""The error occurs because here the np.concatenate function requires matching dimensions but in the given question, x is a 2D array and v is a 1D array.

Problem - 4: Matrix Operations:

• For the following arrays:

A = np.array([[3,4],[7,8]]) and B = np.array([[5,3],[2,1]]);

Prove following with Numpy:
1. Prove A.A−1 = I.
2. Prove AB ≠ BA.
3. Prove (AB)
T = BTAT
.

• Solve the following system of Linear equation using Inverse Methods.

2x − 3y + z = −1

x − y + 2z = −3

3x + y − z = 9

{Hint: First use Numpy array to represent the equation in Matrix form. Then Solve for: AX = B}

• Now: solve the above equation using np.linalg.inv function.{Explore more about ”linalg” function
of Numpy}
"""

import numpy as np
A = np.array([[3, 4], [7, 8]]);
B = np.array([[5, 3], [2, 1]]);

A_inverse = np.linalg.inv(A)
identity_matrix = np.dot(A, A_inverse)
print("A * A^(-1):\n", identity_matrix)

import numpy as np
A = np.array([[3, 4], [7, 8]]);
B = np.array([[5, 3], [2, 1]]);
AB = np.dot(A, B)
BA = np.dot(B, A)
print("AB:\n", AB)
print("BA:\n", BA)

import numpy as np
A = np.array([[3, 4], [7, 8]]);
B = np.array([[5, 3], [2, 1]]);
AB = np.dot(A, B)
ABT = np.transpose(AB)
AT = np.transpose(A)
BT = np.transpose(B)
BTAT = np.dot(BT, AT)
print("(AB)^T:\n", ABT)
print("(B)^T(A)^T:\n", BTAT)

import numpy as np
A = np.array([[2, -3, 1], [1, -1, 2], [3, 1, -1]])
B = np.array([-1, -3, 9])
A_inverse = np.linalg.inv(A)
x = np.dot(A_inverse, B)
print("Solution:\n", x)

"""4.2 Experiment: How Fast is Numpy?
In this exercise, you will compare the performance and implementation of operations using plain Python
lists (arrays) and NumPy arrays. Follow the instructions:
1. Element-wise Addition:
• Using Python Lists, perform element-wise addition of two lists of size 1, 000, 000. Measure
and Print the time taken for this operation.
• Using Numpy Arrays, Repeat the calculation and measure and print the time taken for this
operation.
2. Element-wise Multiplication

• Using Python Lists, perform element-wise multiplication of two lists of size 1, 000, 000. Mea-
sure and Print the time taken for this operation.

• Using Numpy Arrays, Repeat the calculation and measure and print the time taken for this
operation.
3. Dot Product
• Using Python Lists, compute the dot product of two lists of size 1, 000, 000. Measure and
Print the time taken for this operation.
• Using Numpy Arrays, Repeat the calculation and measure and print the time taken for this
operation.
4. Matrix Multiplication
• Using Python lists, perform matrix multiplication of two matrices of size 1000x1000. Measure
and print the time taken for this operation.

• Using NumPy arrays, perform matrix multiplication of two matrices of size 1000x1000. Mea-
sure and print the time taken for this operation.
"""

import time

print("1. Element-wise Addition")

list1 = [i for i in range(1_000_000)]
list2 = [i for i in range(1_000_000)]

start_time = time.time()
result_list = [list1[i] + list2[i] for i in range(len(list1))]
end_time = time.time()
print(f"Time taken by Python Lists: {end_time - start_time:.5f} seconds")

array1 = np.array(list1)
array2 = np.array(list2)

start_time = time.time()
result_array = array1 + array2
end_time = time.time()
print(f"Time taken by numpy: {end_time - start_time:.5f} seconds\n")

print("2. Element-wise Multiplication")

start_time = time.time()
result_list = [list1[i] * list2[i] for i in range(len(list1))]
end_time = time.time()
print(f"Time taken by Python Lists: {end_time - start_time:.5f} seconds")

start_time = time.time()
result_array = array1 * array2
end_time = time.time()
print(f"Time taken by numpy: {end_time - start_time:.5f} seconds\n")

print("3. Dot Product")

start_time = time.time()
dot_product_list = sum(list1[i] * list2[i] for i in range(len(list1)))
end_time = time.time()
print(f"Time taken by Python Lists: {end_time - start_time:.5f} seconds")

start_time = time.time()
dot_product_array = np.dot(array1, array2)
end_time = time.time()
print(f"Time taken by numpy: {end_time - start_time:.5f} seconds\n")

print("4. Matrix Multiplication")
size = 100

matrix1 = [[i for i in range(size)] for _ in range(size)]
matrix2 = [[j for j in range(size)] for _ in range(size)]

start_time = time.time()
result_matrix = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
end_time = time.time()
print(f"Time taken by Python Lists: {end_time - start_time:.5f} seconds")

matrix1_np = np.array(matrix1)
matrix2_np = np.array(matrix2)

start_time = time.time()
result_matrix_np = np.dot(matrix1_np, matrix2_np)
end_time = time.time()
print(f"Time taken by numpy: {end_time - start_time:.5f} seconds")