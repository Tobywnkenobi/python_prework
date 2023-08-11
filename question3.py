#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
# def max_num_in_list(a_list):
# Create a numerical list
# Sort the list in order to find the highest number - used "max" instead.
# return the highest number

def max_num_in_a_list():
    a_list=[2, 5, 97, 56, 25, 8964, 15, 89]
    print("Here are our numbers: ", a_list)
    print("Here is the highest number: ")
    max_num=max(a_list)
    print(max_num)
max_num_in_a_list()