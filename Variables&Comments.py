Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num1,num2,num3=10,20,30
>>> print(num1)
10
>>> print(num2)
20
>>> print(num3)
30
>>> num1=num2=num3=10
>>> print(num1)
10
>>> print(num2,num3)
10 10
>>> print(id(num1))
140713391060376
>>> print(id(num2))
140713391060376
>>> a,b=10,20
>>> print(id(a),id(b))
140713391060376 140713391060696
>>> a,b=256,256
>>> print(id(a),id(b))
140713391068248 140713391068248
>>> a,b=257,257
>>> print(id(a),id(b))
2258010632624 2258010632624
>>> a,b=b,a
>>> print(id(a),id(b))
2258010632624 2258010632624
>>> a=10,b=20
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=10
>>> b=20
>>> a,b=b,a
>>> print(a)
20
>>> print(b)
10
