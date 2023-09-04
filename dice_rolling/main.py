import random
# number_of_sides = int(input("how many sides on your dice? "))
number_of_sides = 6

sum_of_results = 0.0

trials = 0

while trials < 10**2:
    random_number = random.random()
    sum_of_results = int(random_number * number_of_sides +1)
    list_random_numbers = []
    list_random_numbers = list_random_numbers.append(random_number)
    trials += 1
    print(f'trials= {trials}:   {random_number}   {sum_of_results}')

print(list_random_numbers)

print("Average result of rolling one dice is about {0}".format(sum_of_results/trials))