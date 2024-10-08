# create a list of 20 random numbers between -50 and 50
# print the list
# print each positive number of the list using for each
import random

# start
random_list: list[int] = []
for _ in range(20):
    random_list.append(random.randint(-50, 50))
print(random_list)
print()
positive_list: list[int] = []
for positive_number in random_list:
    if positive_number > 0:
        positive_list.append(positive_number)
print(positive_list)
