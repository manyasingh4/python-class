def factorial(num):
    a = 1
    fac = num
    while(a<num):
        fac=fac*a
        a=a+1
    return(fac)
hello = factorial(8)
print(hello)
#fac = a*a

# make a function called search, which takes 2 parameters, a search_term and a list.
# the function should return index of the search_term within the list (if it is within the list)
# if it is not within the list, return -1.

def search(search_term, list):
    i=0
    while i<len(list):
        if(search_term == list[i]):
            return(i)
        i=i+1
    return(-1)

a = search(7, [4, 5, 8, 3, 2])
print(a)

#make a functino called whatever idk, which takes 1 parameter, which is a list containing only numbers 
#the function should return the biggest element in the list
b = [1,2,3,4,6,7,99,88,999]
max_num = 0
for i in b:
    if i > max_num:
        max_num = i
print(max_num)