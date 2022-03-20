highway_number = int(input())

''' Type your code here. '''
div_remainder = highway_number % 2
primary = highway_number % 100
if 0 < highway_number < 100:
    if div_remainder == 0:
        print(f'I-{highway_number}', "is primary, going east/west.")
    else:
        print(f'I-{highway_number}', "is primary, going north/south.") 
elif highway_number == 200:
    print(highway_number, "is not a valid interstate highway number.")
elif 99 < highway_number <1000:
    if div_remainder == 0:
        print(f'I-{highway_number}', "is auxiliary, serving", f'I-{primary}, going east/west.')
    else:
        print(f'I-{highway_number}', "is auxiliary, serving", f'I-{primary}, going north/south.')
else:
    print(highway_number, "is not a valid interstate highway number.")