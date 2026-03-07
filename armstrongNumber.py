def is_armstrong(n):
    num = n
    total = 0
    nod = len(str(n))
    while num > 0:
        ld=num%10
        total =  total + (ld ** nod)
        num = num//10
    return total == n
n = int(input("Enter the number: "))
if is_armstrong(n):
    print("armstrong")
else:
    print("not armstrong")
    
    