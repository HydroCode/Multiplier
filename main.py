print("This is going to take some time...")
print('\n')

number = int(input("Enter a number of your choice: "))

count = 1

while True:
    product = number * count
    print(number, "×", count, "=", product)
    count = count + 1
