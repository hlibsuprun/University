letter = input('Enter letter:')

if len(letter) > 1:
    print('There is more than one letter')
    exit()

if 'a' <= letter <= 'z':
    print('Small letter')
elif 'A' <= letter <= 'Z':
    print('Capital letter')
else:
    print("It isn't letter")
