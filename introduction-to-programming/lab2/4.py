letter = input('Enter one letter:')

if len(letter) > 1:
    print('There is more than one letter')
    exit()

if len(letter) == 0:
    print('There is no letter')
    exit()

if 'A' <= letter <= 'Z':
    print(letter.lower())
elif 'a' <= letter <= 'z':
    print(letter.upper())
else:
    print('There is no letter')
