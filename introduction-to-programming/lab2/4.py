letter = input('Wpisz jedną literę:')

if len(letter) > 1:
    print("Jest więcej niż jedna litera")
    exit()

if len(letter) == 0:
    print("Nie ma żadnej litery")
    exit()

if 'A' <= letter <= 'Z':
    print(letter.lower())
elif 'a' <= letter <= 'z':
    print(letter.upper())
else:
    print("Nie ma litery")
