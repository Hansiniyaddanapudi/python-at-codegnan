# importing module
# by importing the file
import addition
# importing function from module
from subtraction import sub 
# importing module with alias name
import multiplication as Mul 
# importing function with alias name
from division import div as DIVISION
print(addition.add(x=10, y=20))
print(sub(x=10, y=20))
print(Mul.mul)(x = 10, y = 20))
print(DIVISION(10,5))