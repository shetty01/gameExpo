print(f"\n\n****************************************************")
print(f"*************    Welcome to Game Expo  *************")
print(f"****************************************************\n")
gender = input("Please enter your gender (B for Boy and G for Girl):")

age = input("Please enter your age:")

try:
    age = int(age)
except ValueError:
    print(f"Incorrect age. Please enter a number for age.")
    exit()

if( gender.upper() == 'B' or gender.upper() == 'BOY'):
    if(age < 6):
        print(f"\nCongratulations!! You have been enrolled to Rhyming\n\n")
    elif(age > 7 and age < 10):
        print(f"\nCongratulations!! You have been enrolled to Storytelling\n\n")
    elif(age > 11 and age < 15):
        print(f"\nCongratulations!! You have been enrolled to Quiz\n\n")
    elif(age > 20):
        print(f"\nCongratulations!! You have been enrolled to Poetry\n\n")
    else:
        print(f"\nSorry. You cannot enroll to any event.\n\n")
elif (gender.upper() == 'G' or gender.upper() == 'GIRL'):
    if(age < 6):
        print(f"\nCongratulations!! You have been enrolled to Rhyming\n\n")
    elif(age > 7 and age < 10):
        print(f"\nCongratulations!! You have been enrolled to Drawing\n\n")
    elif(age > 10 and age < 15):
        print(f"\nCongratulations!! You have been enrolled to Essay Writing\n\n")
    elif(age > 20):
        print(f"\nCongratulations!! You have been enrolled to Poetry\n\n")
    else:
        print(f"\nSorry. You cannot enroll to any event.\n\n")
else:
    print(f"\nYou have entered incorrect details.\n\n")