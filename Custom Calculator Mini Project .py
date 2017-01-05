#calculator mini projects

#Calc. 1, Temp. converter

Farenheit= input("Please type in a temperature in Farenheit: ")
F= float(Farenheit)

Celsius= F - 32 * 1.8

print("The temperature in Celsius is: ", Celsius)

#Calc. 2, Original problem?

#Username generator, Takes first three letters of name, last name and age to
#Generate username

print("Username Generator")

FirstInput = input("Please type in your First name: ")
First = FirstInput[0,1,2]

LastInput= input("Please type in your Last name: ")
Last = LastInput[0,1,2]

AgeInput= input("Please input your age: ")
Age= float(AgeInput)

print("Your generated username is ", First + Last + Age)

#Come back to this
'''
In the end the program should display the following
print("HenRam17")
'''
