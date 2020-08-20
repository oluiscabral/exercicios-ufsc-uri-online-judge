for i in range(int(input())):
    total = 0
    fruits = {}
    for j in range(int(input())):
        name, price = [w for w in input().split()]
        fruits[name] = float(price)
    for j in range(int(input())):
        name, amount = [w for w in input().split()]
        total += fruits.get(name) * int(amount)
    print("R$ {0:.2f}".format(total))
