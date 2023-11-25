# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print("hello_USERNAME!")
hello_name("USERNAME")


# Write a python function, 
# first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    for x in range(1, 101, 2):
        print(x)
first_odds()



# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
        return max_num
numbers=[4, 16, 26, 32, 48, 60]
print(max_num_in_list(numbers))


    
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. 
#The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(2023))



# Write a function to check to see if all numbers in the list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    for is_consecutive in range(len(a_list)-1):
        if a_list[is_consecutive + 1] - a_list[is_consecutive] != 1:
            return False
        return True
numbers1 =[15, 16, 17, 18, 19, 20]
numbers2 =[8, 9, 10, 12, 13]
confused =[8, 9, 10, False, None]
print(is_consecutive(numbers1))
print(is_consecutive(numbers2))


