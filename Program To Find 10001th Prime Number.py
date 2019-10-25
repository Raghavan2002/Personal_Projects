"""Program To Find 10001th Prime Number"""
list_of_numbers = []
list_of_answers = []
a = 0
b = -1
"""while loop for 10001 prime numbers in list only"""
while len(list_of_answers) < 10001+1:
    a += 1
    b += 1
    """for loop to make a list of numbers from range 1-10000, 10001-20000,etc"""
    for value in range(b*10000+1, a*10000+1):
        list_of_numbers.append(value)
    """nested for loop to remove non-prime numbers from list(list_of_numbers)"""
    for check in range(b*10000+1, a*10000+1):
        for value in range(2, a*10000+1):
            if check % value == 0 and check // value != 1:
                list_of_numbers.remove(check)
                break
    """for loop to add the numbers remaining in list(list_of_numbers) to list(list_of_answers)"""
    for value in list_of_numbers:
        if len(list_of_answers) < 10001+1:
            list_of_answers.append(value)
    """resetting list is important coz we are checking for different ranges like 1-10000,10001-20000,etc and
       adding to list(list_of_answers) if we don't reset then same numbers will be added"""
    list_of_numbers = []
"""as the list has 10001 prime numbers the last term will give the answer but the list has 1 which 
   is co-prime so remove it"""
list_of_answers.remove(1)
print(list_of_answers[-1])
