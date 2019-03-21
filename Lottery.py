chosen_number = input("Enter Any Number Between 0 to 9 ")
print("You Have Chosen {} ".format(chosen_number))
import random
magic_number = random.randint(0, 9)
print("The Lucky Number For Current Draw is {}".format(magic_number))
if int(chosen_number) == int(magic_number):
    print("You Have Won")
else:
    print("You Lose")