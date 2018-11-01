# Let's explore some functions and how to write them
# and also what they do


def greeting():
	#say hello
	print("Hello from your first function!")


#this is how you call or invoke a function
greeting()


def greetings(msg="Hello, there!",num=0): #equals sign adds default if no args passed
	print("Our function says...", msg, "The second argument is...",num)


greetings()
greetings("This is an argument",6)
greetings("Why are we arguing?",9)

myVarNum = 0;


def someMath(num1=2,num2=5):
	global myVarNum #makes a connection to the scope outside

	myVarNum = num1+num2
	return num1+num2


sum = someMath();
print("Our sum variable =", sum, "myVarNum is also", sum)