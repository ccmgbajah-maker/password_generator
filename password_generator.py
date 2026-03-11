import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
generating = True
while generating == True:
    # Get user input for password length and character types
    try:
       password_length = int(input("Enter the desired password length (6-32): "))
       if 6<= password_length <= 32:
          pass
       else:
          print("Invalid input. Please enter a number between 6 and 32.")
          continue
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    # Get user input for including numbers and symbols
    while True:
      numbers_included = input("Include numbers? (yes/no): ").lower()
      if numbers_included not in ["yes", "no"]:
        print("Invalid input. Please enter yes or no.")
        continue
      else:
        break
    while True:
      symbols_included = input("Include symbols? (yes/no): ").lower()
      if symbols_included not in ["yes", "no"]:
        print("Invalid input. Please enter yes or no.")
        continue
      else:
         break
    # Generate the password based on user preferences
    if numbers_included == "yes" and symbols_included == "yes":
        characters = letters + numbers + symbols
    elif numbers_included == "yes" and symbols_included == "no":
        characters = letters + numbers
    elif numbers_included == "no" and symbols_included == "yes":
        characters = letters + symbols
    else:
        characters = letters
    # Generate a random password using the specified character set and length
    random_length = password_length
    if numbers_included == "yes":
        random_length -= 1
    if symbols_included == "yes":
        random_length -= 1
    random_part = random.sample(characters, random_length)
    password_list = random_part
    if numbers_included == "yes":
        password_list.append(random.choice(numbers))
    if symbols_included == "yes":
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Generated password: {password}")
    break

