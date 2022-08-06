print("'A' -Add 'S' -Subtract 'M' -Multiply 'D' -Divide")
while True:
    a=int(input("Buhel too oruul "))
    b=int(input("2dahi buhel toog oruul "))
    c=input("A, S, M, Dgiin ali negiig oruul ")
    if c == 'a' or c == 'A':
        print("Niilber= ", a + b)
    if c == 's' or c == 'S':
        print("Yalgavar= ", a - b)
    if c == 'm' or c == 'M':
        print("Urjver= ", a * b)
    if c == 'd' or c == 'D':
        print("Nogdvor= ", a / b)

