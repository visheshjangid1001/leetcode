def division(num):
    result = []
    for i in range(1,num+1):
        if num%i == 0:
            result.append(i)
    return result
num = int(input("Enter the number: "))
factors = division(num)
print(f"Factors of {num} are:", factors)
