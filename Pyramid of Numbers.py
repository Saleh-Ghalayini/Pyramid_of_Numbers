x = int(input("please enter your number to generate the Pyramid of Numbers: "))

#outer loop for # of rows and the inner one is to print each row
for i in range(x):
    for j in range(i + 1):
        print(f"{j + 1} ",end="")
    print("\n", end="")