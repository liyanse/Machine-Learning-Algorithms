# In this example, I'll be using a nested for and while loop to make reservations for a train ticket
travel = input('Yes or No:')

while travel == 'yes':

    num = int(input('Number of people travelling'))
    for num in range(1, num + 1):
        name = input('Name:')
        age = input('Age:')
        sex = input("Male or female:")

        print(name)
        print(age)
        print(sex)

    travel = input("Oops!,forgot someone?")
