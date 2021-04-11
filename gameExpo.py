print(f"\n\n****************************************************")
print(f"*************    Welcome to Game Expo  *************")
print(f"****************************************************\n")

#Get Gender input from the user. 
gender = input("Please enter your gender (B for Boy and G for Girl):")

#Get Age as input from the user
age = input("Please enter your age:")

#Check if the age is integer. 
try:
    age = int(age)
except ValueError:
    print(f"Incorrect age. Please enter a number for age.")
    exit()

#Ensure case doesn't cause any issue. so compare after converting the input string to Upper case and compare with B or BOY 
#This is the predicate to compare the gender with Boy. 
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