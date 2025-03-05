from array import *

LIST = array('i',[])

NUMBER_OF_THE_LIST = int(input("How many things are in the list? " ))

for i in range(NUMBER_OF_THE_LIST):
    THE_QUESTION = int(input("Enter the value: "))
    LIST.append(THE_QUESTION)

print(LIST)

SEARCH= int(input("What number do you want to search "))

FOUND = (LIST.index(SEARCH))
print(F"The number you search is {FOUND} in the list")

MAX= (max(LIST))
print(f"The biggest number is {MAX}")

LOW= (min(LIST))
print(f"The smallest number is {LOW}")

ADD= (sum(LIST))
print(f"The sum of the list is {ADD}")
