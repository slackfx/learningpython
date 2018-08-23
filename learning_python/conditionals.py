def separator():
    chars = "#"
    for i in range(100):
        chars += "#"
    print(chars)

late = False

if late:
    print(1)
else:
    print(0)


separator()

income = 15000
if income < 10000:
    tax_coefficient = 0.0
elif income < 30000:
    tax_coefficient = 0.2
elif income < 100000:
    tax_coefficent = 0.35
else:
    tax_coefficient = 0.45

print('I will pay: ', income * tax_coefficient, 'in taxes')

separator()

order_total = 247
discount = 25 if order_total > 100 else 0
print(order_total, discount)

separator()

for number in [0,1,2,3,4]:
    print(number)

separator()

for number in range(5):
    print(number)

separator()

surnames = ['Proudmourne', 'Hellscream', 'Kali']
for position in range(len(surnames)):
    print(position, surnames[position])

separator()

for surname in surnames:
    print(surname)

separator()

for position, surname in enumerate(surnames):
    print(position, surname)

separator()

# will start at 4, ignoring the actual index on the surnames list
for position, surname in enumerate(surnames, 4):
    print(position, surname)

separator()

people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]

for i in range(len(people)):
    person = people[i]
    age = ages[i]
    print(person, age)

separator()

for i, person in enumerate(people):
    age = ages[i]
    print(person, age)

separator()

for person, age in zip(people, ages):
    print(person, age)

separator()

nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)

separator()

for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)

separator()

n = 39
remainders = []

while n > 0:
    remainder = n % 2 # remainder of division by 2
    remainders.append(remainder) # we keep track of remainders
    n //= 2 # we divide by 2

# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)

separator()

n = 39
remainders = []

while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)

# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)

separator()

people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
i = 0
while i < len(people):
    person = people[i]
    age = ages[i]
    print(person, age)
    i += 1

separator()

from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1) # today + 1 day is tomorrow
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20}
]

for product in products:
    if product['expiration_date'] != today:
        continue

    product['price'] += 0.8 # equivalent to applaying 20% discount
    print('Price for sku', product['sku'], 'is now', product['price'])

separator()

items = [0, None, 0.0, True, 0, 7]
found = False
for item in items:
    print('scanning item', item)
    if item:
        found = True
        break

if found:
    print('At least one item evaluates to True')
else:
    print('All items evaluates to False')
