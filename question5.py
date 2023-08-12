#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type
#function to check the lists [use randome number lists, range??]
#Check it, return true or false on it.


list_a=[1,2,3,4,5,6,7,8,9,10]
list_b=[1,2,5,7,8,4,0,84,3,6]

def is_consecutive(list_a):
    sorted_list = sorted(list_a)
    cons = all(sorted_list[i] == sorted_list[i-1] + 1 for i in range(1, len(sorted_list)))
    print(list_a)
    is_consecutive(list_a)
    