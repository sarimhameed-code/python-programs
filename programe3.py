# 1. Armstrong Number
def is_armstrong(n):
    power = len(str(n))
    return n == sum(int(d)**power for d in str(n))

print("Armstrong:", is_armstrong(153))  # True


# 2. Happy Number
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

print("Happy:", is_happy(19))  # True


# 3. Magic Number
def is_magic(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n == 1

print("Magic:", is_magic(19))  # True


# 4. Disarium Number
def is_disarium(n):
    return n == sum(int(d)**(i+1) for i, d in enumerate(str(n)))

print("Disarium:", is_disarium(135))  # True


# 5. Neon Number (sum of digits of square == number)
def is_neon(n):
    sq = n*n
    return n == sum(int(d) for d in str(sq))

print("Neon:", is_neon(9))  # True


# 6. Automorphic Number (number’s square ends with the number itself)
def is_automorphic(n):
    return str(n*n).endswith(str(n))

print("Automorphic:", is_automorphic(25))  # True


# 7. Harshad (Niven) Number (divisible by sum of digits)
def is_harshad(n):
    return n % sum(int(d) for d in str(n)) == 0

print("Harshad:", is_harshad(18))  # True


# 8. Strong Number (sum of factorial of digits == number)
import math
def is_strong(n):
    return n == sum(math.factorial(int(d)) for d in str(n))

print("Strong:", is_strong(145))  # True


# 9. Spy Number (sum of digits == product of digits)
def is_spy(n):
    digits = [int(d) for d in str(n)]
    return sum(digits) == math.prod(digits)

print("Spy:", is_spy(1124))  # True


# 10. Palindrome Number
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print("Palindrome:", is_palindrome(121))  # True

