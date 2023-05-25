###..1..[“name512”, “same1example”, “joy18full”] replace the digits from string inside list
'''string_list= ["name512", "same1example", "joy18full"]
modified_list=[]
for string in string_list:
    modified_string=""
    for char in string:
        if char.isdigit():
            modified_string+="_"  # replacing digit with underscore "_"
        else:
            modified_string+=char
    modified_list.append(modified_string)
print(modified_list)
###..2..[1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt functions like map, filter or reduce
digits = list(filter(str.isdigit, map(str, [1, "a", 2, "b", 3, "c"])))
alphabets = list(filter(str.isalpha, map(str, [1, "a", 2, "b", 3, "c"])))

print(digits)
print(alphabets)
###..3..[1,2,3,1,3,4,6,5,3] get unique numbers from list with basic constructs
original_list = [1, 2, 3, 1, 3, 4, 6, 5, 3]
unique_list=[]
for number in original_list:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)  

###..4...Create function to generate data randomly with python standard library
import random

def generate_random_data(min_value, max_value, size):
  random_values = []
  for _ in range(size):
    random_value = random.randint(min_value, max_value)
    random_values.append(random_value)

  return random_values
random_data=generate_random_data(1,100,10)
print(random_data)'''

###..5..Create function to check if date is in given range

import datetime

def date_in_range(date, start_date, end_date):
  if start_date <= date <= end_date:
    return True
  else:
    return False
given_range=date_in_range(datetime.date(2023, 5, 25), datetime.date(2023, 5, 20), datetime.date(2023, 5, 27))
print(given_range)




