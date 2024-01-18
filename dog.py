class Dog:
    name : str
    no_legs : int
    breed : str
    barking_ability : bool

    def __init__(self, pname, pnumberlegs): #constructor init is required for object initialisation (in this case Bill)
        self.name = pname
        self.no_legs = pnumberlegs

    def sleep(self, time : int):
        print(self.name, 'slept for', time, 'hours')

    def bark(self):
        print('raughr')

    def shit(self):
        print('I am not writing a sound effect for this')

def add(a, b):
    sum = a + b
    return(sum)

def hello_manya():
    print('hello')
    return 0
#without return it would output 'None'

plop = add(5, 6)
plop = add(5, plop)
print(plop)

if  __name__ == '__main__':
    bill = Dog('bill', 4)
    bill.name = 'bill' #not required if you have the parameter for name in your constructor (init) as done in line above
    bill.sleep(5)
    bill.shit()

    manya = hello_manya() + 500
    print(manya)

        
    
#hello manya function returns value 0 after running the code and 0 basically replaced hello manya at line 24 and so the output becomes 0 + 50 = 50
#hello manya fn transfers control to print function to print hello
#return returns control to main function

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

#another way to do it:
#def is_even(num):
#   if num % 2 == 0:
#       return True
#   else:
#       return False

#if is_even(7) == True: <-- redundant because if only runs True statements
#    print("even")
#else:
#    print("odd")

g = [1, 2, 3, 4]
g.append(5)
print(g[0]) #prints element with index 0

i=0
while i<4:
    print(g[i])
    i=i+1

for element in g:
    print(element) #for and while loop do the same thing here

len(g) #length of a list


def main():
    #write all zour code
    pass