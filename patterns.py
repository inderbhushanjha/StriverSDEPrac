
k = 4
print("pattern 1 : ")
print()
for i in range(k):
    for i in range(k):
        print("* ", end = "")
    print()

print()
print("pattern 2 : ")
print()
for i in range(k):
    for j in range(i+1):
        print("* ", end = "")
    print()

print()
print("pattern 3 : ")
print()
for i in range(k):
    for j in range(i+1):
        print(j+1, end="")
    print()

print()
print("pattern 4 : ")
print()
for i in range(k):
    for j in range(i+1):
        print(i+1, end="")
    print()

print()
print("pattern 5 : ")
print()
for i in range(k):
    for j in range(k-i):
        print("*", end="")
    print()

print()
print("pattern 6 : ")
print()
for i in range(k):
    for j in range(k-i):
        print(j+1, end="")
    print()

print()
print("pattern 7 : ")
print()
for i in range(k): # 0 : 3 
    for j in range(k-i):
        print(" ",end="")
    for z in range(2*i+1):
        print("*", end="")
    print()

print()
print("pattern 8 : ")
print()
for i in range(k):
    for j in range(i+1):
        print(" ", end="")
    for z in range((2*k) - (2*i+1)):
        print("*",end="")
    print()

print()
print("pattern 9 : ")
print()
for i in range(k):
    for j in range(k-i):
        print(" ", end="")
    for z in range(2*i +1):
        print("*", end="")
    print()
for i in range(k):
    for j in range(i+1):
        print(" ", end="")
    for z in range((2*k) - (2*i+1)):
        print("*",end="")
    print()

print()
print("pattern 10 : ")
print()
for i in range(k):
    for j in range(i+1):
        print("*", end="")
    print()
for i in range(k):
    for j in range(k-i-1):
        print("*", end="")
    print()

print()
print("pattern 11 : ")
print()
for i in range(k):
    switch = 1 if(i%2 == 0) else 0
    for j in range(i+1):
        print(switch, end="")
        switch = 1 - switch
    print()


print()
print("pattern 12 : ")
print()
for i in range(k):
    start = 1
    for j in range(i+1):
        print(start,end="")
        start+=1
    for j in range(2 * (k-i-1)):
        print(" ", end="")
    
    for z in range(i+1):
        print(start-1,end="")
        start-=1
    print()


print()
print("pattern 13 : ")
print()
ini = 1
for i in range(k):
    for j in range(i+1):
        print(ini, end=" ")
        ini+=1
    print()

print()
print("patter 14 : ")
print()
for i in range(k):
    ch = 65
    for j in range(i+1):
        print(chr(ch), end="")
        ch+= 1
    print()


print()
print("pattern 15 : ")
print()
for i in range(k):
    ch = 65
    for j in range(k - i):
        print(chr(ch),end="")
        ch+=1
    print()

print()
print("pattern 16 : ")
print()
ch = 65
for i in range(k):
    for j in range(i+1):
        print(chr(ch),end="")
    ch+=1
    print()


print()
print("pattern 17 : ")
print()
for i in range(k):
    ch = 65
    for j in range(k-i):
        print(" ", end="")
    for z in range(2*i+1):
        print(chr(ch),end="")
        if(i <= z):
            ch-=1
        else:
            ch += 1
    print()

print()
print("pattern 18 : ")
print()
ch = 65
for i in range(k):
    ch = ch+k-i
    for j in range(i+1): 
        print(chr(ch - 1),end="")
        ch -= 1
    print()


print()
print("pattern 19 : ")
print()
for i in range(k):
    for j in range(k-i):
        print("*",end="")
    for j in range(2*i):
        print(" ",end="")
    for j in range(k-i):
        print("*", end="")
    print()
for i in range(k):
    for j in range(i+1):
        print("*", end="")
    for j in range(2*(k-i-1)):
        print(" ",end="")
    for j in range(i+1):
        print("*", end="")
    print()


print()
print("pattern 20 : ")
print()
for i in range(k):
    for j in range(i+1):
        print("*",end="")
    for j in range(2*(k-i-1)):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()
for i in range(k):
    for j in range(k-i-1):
        print("*", end="")
    for j in range(2*(i+1)):
        print(" ",end="")
    for j in range(k-i-1):
        print("*", end="")
    print()

print()
print("pattern 21 : ")
print()
for i in range(k):
    for j in range(k):
        if(i == 0 or j == 0 or i == k-1 or j == k-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()


print()
print("pattern 22 : ")
print()
for i in range(2*k-1):
    for j in range(2*k-1):
        top = i
        left = j
        bottom = (2*k) - 2 - i
        right = 2*k - 2 - j
        val = min(min(top, left), min(bottom, right))

        print(k - val,end="")
    print()


