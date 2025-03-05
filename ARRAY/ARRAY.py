from array import *

LIST = array('i',[])

NUMBER_OF_THE_LIST = int(input("How many things are in the list? " ))

for i in range(NUMBER_OF_THE_LIST):
    THE_QUESTION = int(input("Enter the value: "))
    LIST.append(THE_QUESTION)

print(LIST)

SEARCH= int(input("What number do you want to search "))

print(LIST.index(SEARCH))
