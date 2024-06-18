def exp(base,pow):
    i=1
    for j in range(pow):
        i=i*base
    return i
print(exp(int(input("Base: ")),int(input("Power: "))))