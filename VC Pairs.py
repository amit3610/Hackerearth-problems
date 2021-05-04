t=int(input())

for i in range (t):
    n = int(input())
    s=input()[:n]
    count = 0

    for j in range(n-1):
            if (s[j]  not in "aeiou") and (s[j+1] in "aeiou"):
                    count+=1
    print(count)
