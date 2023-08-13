#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type
#function to check the lists [use randome number lists, range??]
#Check it, return true or false on it.

#a_list = [1,2,3,4,5]
a_list = [1,2,5,7,84]

def is_consecutive(a_list):
    #sorted(a_list) == a_list(range(min(a_list), max(a_list)+1))
    a_list.sort()
for i in a_list:
        if ((a_list[0]) < (a_list[1 - 0]) < (a_list[2 - 1]) < (a_list[3 - 2]) < (a_list[4 - 3])):
              print(True)
        else: print(False)
is_consecutive(a_list)



