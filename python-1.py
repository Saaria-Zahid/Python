print("Hello")

a = 10
b= 12
c= 2.0

d = a*(b+c)
print(d)


typeOfC = type(c)
print(typeOfC)


e= int(a)
print(type(e), e)



# Paragraphs

myText = '''
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. Sed auctor,
nunc a pellentesque fermentum, lectus velit ullamcorper ipsum,
non volutpat velit nisi id nunc. Integer ac ipsum vel felis tincidunt scelerisque.
'''

print(myText)


# Inputs

name = input('Enter Name: ')
print(name)

age = int(input('Age: '))
print(age)


# If Else - Conditional Statements

if age >=18:
    print('You are an adult')
elif (age <18) and (age >= 10):
    print('You are a teenager')   
else:
    print('You are a kid')

 
