# Using flask to make an api 
# import necessary libraries and functions 

import math
from flask import Flask

#initializing variable num
num = 1

# code to check if any number is prime
def isPrime(n):
	if n<= 1:
		return False
	
	for i in range(2,n):
		if n % i == 0 :
			return False
	return True


#creating a Flask application object
app = Flask(__name__)

#mapping URL to functions
@app.route('/BothSidePrime/<int:num>', methods = ['GET'])
def BothSidePrime(num):
	num_of_digits=int(math.log10(num))
	for i in range(1, num_of_digits+1):
		a=num%pow(10,i)
		b=num//pow(10,i)
		if isPrime(a)==False or isPrime(b)==False :
			return {"is Prime": False}
	return {"isPrime": True}

# driver function 
if __name__ == '__main__': 
    app.run(debug = True) 