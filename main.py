import random


def check_for_int(input_str):
    try:
        man = type(int(input_str))
    except:
        return False
    else:
        return True


def play_again():
    while True:
        resposes = input("Wanna Play again??(y/n):").strip()
        if resposes == "y":
            return True
        elif resposes == "n":
            return False
        else:
            print("\nINVALID input ... ... \n")


print(f"Hello Welcome to my number guessing game!")


while True:
    lower_limit = input("The lower limit of the range:")
    is_valid_input = check_for_int(lower_limit)

    if not is_valid_input:
        print("\nINVALID Input!!\nEnter an integer.")
        continue

    if int(lower_limit) < 0 or int(lower_limit) > 1000:
        print("Insert something inside range[0,1000]")
        continue
    # global upper_limit
    while True:
        upper_limit = input("The upper limit of the range:")
        is_valid_input = check_for_int(upper_limit)

        if not is_valid_input:
            print("\nINVALID Input!!\nEnter an integer.")
            continue
        if int(upper_limit) < 0 or int(upper_limit) > 1000 or int(upper_limit) < int(lower_limit):
            print(
                "Insert something inside range[0,1000] and greater than the lower limit.")
            continue
        else:
            break

    random_number = random.randint(int(lower_limit), int(upper_limit))

    won = False
    for attempts in range(6):
        print(f"\n{attempts + 1}th attempt")
        input_num = input("Do your best guess :").strip()
        is_a_int = check_for_int(input_num)
        if is_a_int and int(input_num) == random_number:
            won = True
            break
        else:
            print("Try Again Bro...\n")

    if won:
        print(
            f"Congratulations!!You won!!\nThe number is in fact {random_number}")
    else:
        print(f"Oops!!Sorry that you lost.\nThe number is {random_number}\n")
    input("Press Enter to continue... ...")

    wanna_play = play_again()
    if wanna_play:
        print("\n")
        continue
    elif not wanna_play:
        break
