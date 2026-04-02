#  NumPy Attributes and Functions Used in This Code

This file demonstrates basic NumPy operations along with important attributes and pre-built functions. Below is a clear explanation of all attributes and functions used in this code.

##  1. np.array()

Definition:  
np.array() is used to convert a Python list (or tuple) into a NumPy array.

Explanation: 
It creates a homogeneous array where all elements have the same data type and allows faster mathematical operations.

## 2. shape

Definition:  
shape is an attribute that returns a tuple representing the dimensions of the array.

Explanation:  
It tells how many rows and columns are present in the array.

Example:
(3, 3) → 3 rows and 3 columns


## 3. size

Definition:  
size is an attribute that returns the total number of elements in the array.

Explanation:  
It counts all elements in the array regardless of dimensions.

## 4. ndim

Definition: 
`ndim` is an attribute that returns the number of dimensions (axes) of the array.

Explanation:  
It tells whether the array is 1D, 2D, or multi-dimensional.


## 5. np.zeros()

Definition: 
`np.zeros()` is a pre-built NumPy function that creates an array filled with zeros.

Explanation: 
It can create both one-dimensional and multi-dimensional arrays with all values equal to 0.

Example:  
np.zeros(3) → [0. 0. 0.]

## 6. np.ones()

Definition:  
`np.ones()` is a pre-built NumPy function that creates an array filled with ones.

Explanation:
It returns an array where all elements are 1, in any dimension.

Example:  
np.ones((2,3)) → 2 rows and 3 columns filled with 1


## 7. Array Multiplication (* operator)

Definition: 
The `*' operator performs element-wise multiplication in NumPy arrays.

Explanation: 
Each element of the array is multiplied individually.

Example:  
[1,2,3] * 3 → [3,6,9]


## 8. List Multiplication (* operator)

Definition:  
When used with Python lists, the `*` operator repeats the list.

Explanation:  
It does not perform mathematical multiplication, instead it duplicates the elements.

Example: 
[1,2,3] * 3 → [1,2,3,1,2,3,1,2,3]
