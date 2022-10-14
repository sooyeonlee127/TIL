n = int(input())


def sugar(n) :
    n2 = n
    cnt = 0
    while n >= 5:
        n -= 5
        cnt += 1
    if n == 0 :
        return cnt
    elif n % 3 == 0 :
        cnt += n//3
        return cnt
    else:
        cnt = 0
        n = n2
        n -= 10
        cnt += 2
        if n % 3 == 0 and n >= 3 :
            cnt += n//3
            return cnt
        else:         
            cnt = 0
            n = n2
            n -= 5
            cnt += 1
            if n % 3 == 0 :
                cnt += n//3
                return cnt
            else:
                cnt = 0
                if n2 % 3 == 0:
                    cnt += n2 // 3
                    return cnt
                else :
                    return -1
            
print(sugar(n))
            
            

        