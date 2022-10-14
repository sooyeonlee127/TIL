n = int(input())
result = 0

while n != 0:
    if n // 5 >= 1 :
        result += n//5
        n = n - (n // 5) * 5
        if n // 3 >= 1:
            result += n//3
            n = n - (n // 3) * 3
            break
        elif n == 0 :
            break
        else :
            result = -1
            break
    elif n // 3 >= 1 :
        result += n//3
        n = n - (n // 3) * 3
        if n == 0 :
            result = result + 0
            break
        else :
            result = -1
            break

print(result)