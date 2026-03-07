def is_palindrome(n):
    num = n
    result = 0
    while num > 0:
        ld = num % 10
        result = (result * 10) + ld
        num = num // 10
    return n == result

# Example
n = int(input("Enter a number: "))
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")