i = 1

while i <= 3:
    print("Outer loop:", i)

    j = 1

    while j <= 3:
        if j == 2:
            break

        print("Inner loop:", j)
        j += 1

    i += 1

print("Program finished")

print(range(1,11))

number = list(range(11))
print(number)