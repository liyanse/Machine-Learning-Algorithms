# Writing a python program using the nested while loop to stimulate ATM Banking services
print('Welcome to our ATM Banking Systems')
restart = 'Y'
chances = 3
bank_balance = 10000
while chances >= 0:
    pin = int(input('Enter your pin number'))
    if pin == 2022:
        print("You've entered the correct pin")
        while restart not in ('n', 'no', 'N', 'NO'):
            print('Press 1 to check your account balance\n')
            print('Press 2 to withdraw money from your account\n')
            print('Press 3 to deposit money to your account\n')
            print('Press 4 to remove card\n')

            option = int(input('What Option would you like to chose?'))
            if option == 1:
                print("Your account balance is: ", bank_balance)
                restart = input('Go back?')
                if restart in ('n', 'no', 'N', 'NO'):
                    print('Thank you')
                    break

            elif option == 2:
                withdrawal = int(input('How much money would you like to withdraw? \n 1000/750/500/250/125'))
                if withdrawal in [1000, 750, 500, 250, 125]:
                    bank_balance = bank_balance - withdrawal
                    print('Your new bank balance is: ', bank_balance)
                    restart = input('Go back?')
                    if restart in ('n', 'N', 'NO', 'no,'):
                        print('Thank you')
                        break

            elif option == 3:
                deposit = float(input('How much money would you like to deposit?'))
                bank_balance = bank_balance + deposit
                print("Your new bank balance is: ", bank_balance)
                restart = input('Go back?')
                if restart in ('n', 'no', 'N', 'NO'):
                    print('Thank you')
                    break
            elif option == 4:
                print('Please wait as we process your card')
                print('Thank you for your services')
                break

            else:
                print('Enter the correct number')


    elif pin != 2022:
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('No more tries, Try again later')
            break
