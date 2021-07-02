# write your code here
import random

try:
    num_friends = int(input("Enter the number of friends joining (including you):\n"))
    if num_friends < 1:
        raise ValueError
except ValueError:
    print("No one is joining for the party")
else:
    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(num_friends):
        friend = input()
        friends[friend] = 0
    bill_val = float(input("Enter the total bill value:\n"))

    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    lucky_person = ''
    lucky_enabled = False
    if lucky == 'Yes':
        lucky_person = random.choice(list(friends.keys()))
        lucky_enabled = True
        print(lucky_person + " is the lucky one!")
    elif lucky == 'No':
        print("No one is going to be lucky")

    num_payees = len(friends) - 1 if lucky_enabled else len(friends)
    split_val = bill_val / num_payees
    split_val = round(split_val, 2)

    for friend in friends:
        if lucky_enabled and friend == lucky_person:
            friends[friend] = 0
        else:
            friends[friend] = split_val

    print(friends)
