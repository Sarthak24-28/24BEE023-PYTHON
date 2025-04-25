while True:
    try:
        user_input = input("Please enter an integer: ")
        number = int(user_input)
        print("Success! You entered the integer:",number)
        break
    except ValueError:
        print("Error: That's not an integer. Please try again.")
