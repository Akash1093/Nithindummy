# Python function that prints a text

'''def greet():
    print("Hello")
    print("How do you do")
greet()
greet()
greet()
'''

#Python function that accepts two numbers as arguments and returns the sum

'''def addnumbers(x,y):
    sum=x+y
    return sum
output=addnumbers(12,9)
print(output)'''

#Python function that accepts different values as parameters and returns a list

'''def myfruits(f1,f2,f3,f4):
    fruitlist=[f1,f2,f3,f4]
    return fruitlist
output=myfruits("Apple","Bannana","Grapes","Orange")
print(output)'''


#Python function that returns a dictionary

'''def myanimals(a1,a2,a3):
    animalgroup={'kitchen':a1,'puppy':a2,'pup':a3}
    return animalgroup
output=myanimals("cat","dog","rat")
print(output)'''


# Python function that returns a tuple

'''def myveggies(v1,v2,v3):
    vegtuple=(v1,v2,v3)
    return vegtuple
output=myveggies("carrot","potato","tomato")
print(output)'''


#Python function that accepts a list as a parameter

'''def mychocolates(clist):
    for i in clist:
        print(i)
chocolatelist=["dairymilk","snickers","kitkat"]
mychocolates(chocolatelist)'''


#Python function that accepts a dictionary as a parameter

'''def myvechicles(vdict):
    print( vdict)
vechicledictionary={
    'tesla':'car',
    'royal enfield':'bike'
    }
myvechicles(vechicledictionary)'''


# Python function using positional arguments

'''def car(name,model):
    print(name)
    print(model)
car("Audi","Q7")'''


# Python function using keyword arguments

'''def car(name,model):
    print(name)
    print(model)
car(model="Q7",name="Audi")'''


# Python function using default arguments

'''def Car(name,model="Q7"):
    print(name)
    print(model)
    
Car("Audi")'''


# Python function using optional arguments

'''def calendar(year,month,date=''):
    print(year,month,date)

calendar(2023,2)'''



