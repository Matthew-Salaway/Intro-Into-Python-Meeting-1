# This is a comment 


# This is how you print to the terminal 

print("Hello World") 

print(2020) 


""" 
# We can make create new lines with \n. Also we can use quotes by \". \ is an escape sequence 
print("This is \n a new line") 
print("Darth Vader said \"No. I am your father.\"") 
""" 

""" 
# Lets make a varible, a varible is a storage location that can hold data.  
car = "Tesla"             # String    - letters, numbers, characters 
miles = 47000             # Int       - whole numbers 
costPerTank = 15.29       # Double    - number with decimals 
isElectric = True         # Boolean   - True or False 
""" 

""" 
# We can make sure this variable holds the right value, but printing it to the terminal 
print(car) 
print(miles) 
print("The " + car + " has " + str(miles) + " miles.") 
""" 

""" 
# This is called string concatenation. We are "adding" strings together to form a new one. Since the miles variable is an int, we have to convert it to a string before we concatenate. We do this by str(). 
# Python is different from most other lanuages. It uses an interpreter, instead of a complier. This means syntax is easy and there are less rules, but the program is slower.  
# Lets say Tesla improves thier battery effiecency, therefor lowering the costPerTank by a dollar 
costPerTank = costPerTank - 1 
  
costPerTank -= 1 
costPerTank = 14.29 
  
print(costPerTank) 
# These are all valid ways of reducing the price by 1. There are multiple ways to code a certin action. Some are more effiecent than others 
""" 
