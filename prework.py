#question 1
def hello_name(user_name):
    print("hello_" + user_name)
user_name = input('Enter Username: ')
hello_name(user_name.upper())

#question 2
def first_odds():
    for num in range(1,101):
        if num % 2 != 0:
            print(num)
first_odds()

#question 3
def max_num_in_list(a_list):
    return max(a_list)
a_list = [15, 80, 140, 5, 60]
print(max_num_in_list(a_list))

#question 4
def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0):
        return True
    elif(a_year % 400 == 0 and a_year % 100 != 0):
        return True
    return False

print (is_leap_year(int(input("\nTell me a year and I'll tell you if it was a leap year: "))))


#question 5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [1,2,4,5]
print(is_consecutive(a_list))
a_list = [6, 12, 5, 3, 2]
print(is_consecutive(a_list))
