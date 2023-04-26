# names = ['Michael', 'Bob', 'Tracy']
# random_name = random.choice(names)
import random

max_tries = int(input("set the maximum tries: "))
names = [l.strip() for l in open("names.txt").readlines() if l.strip()]
# 3 names
# 0, 1, 2
rand_name_index = random.randint(0, len(names) - 1)


def get_guess():
    try:
        return int(input("Guess the winner index: "))
    except ValueError:
        return get_guess()


# thios variable will hold the number of tries of the player
tries = 0
# loop whilte tries is less than max_tries
# when the triers reach max_tries , the loop will end
while tries < max_tries:
    # print names
    for index, name in enumerate(names):
        print(f"{index} - {name}")
    # take the input from user, and convert it to integer
    user_num = get_guess()
    # tries += 1
    tries = tries + 1
    # 1 => user_num < rand_name_index => too low
    if (user_num < rand_name_index):
        print("Your guess is too low")
    # 2 => user_num > rand_name_index => too high
    elif (user_num > rand_name_index):
        print("Your guess is too high")
    # 3 => user_num == rand_name_index => you win
    else:
        # break the loop
        print(f"You win, with {tries} tries!")
        break

if tries == max_tries:
    # when loop end, this means the player is lost
    print(f"You lost, the index was: {rand_name_index} - {names[rand_name_index]}")
