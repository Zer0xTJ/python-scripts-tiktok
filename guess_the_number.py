import random


max_tries = int(input("set the maximum tries: "))
# generate random number
rand_num = random.randint(1, 100)


def get_guess():
    try:
        return int(input("Guess the number: "))
    except ValueError:
        return get_guess()


# thios variable will hold the number of tries of the player
tries = 0
# loop whilte tries is less than max_tries
# when the triers reach max_tries , the loop will end
while tries < max_tries:
    # take the input from user, and convert it to integer
    user_num = get_guess()
    # tries += 1
    tries = tries + 1
    # 1 => user_num < rand_num => too low
    if (user_num < rand_num):
        print("Your guess is too low")
    # 2 => user_num > rand_num => too high
    elif (user_num > rand_num):
        print("Your guess is too high")
    # 3 => user_num == rand_num => you win
    else:
        # break the loop
        print(f"You win, with {tries} tries!")
        break

if tries == max_tries:
    # when loop end, this means the player is lost
    print(f"You lost, the number was: {rand_num}")

# = : x = 10, assign 10 to x
# == : x == 10 , is x equal to 10?
# pip install lib_name
