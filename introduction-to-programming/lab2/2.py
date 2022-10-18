letter = input('Wpisz jedną literę:')

if len(letter) > 1:
    print("Jest więcej niż jedna litera")
    exit()

if len(letter) == 0:
    print("Nie ma żadnej litery")
    exit()

if 'A' <= letter <= 'Z':
    print('Litera jest wielka')
elif 'a' <= letter <= 'z':
    print('Litera jest mała')
else:
    print("Nie ma litery")
