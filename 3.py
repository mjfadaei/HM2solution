c = 0
n = 2
sum = 0
while c <= 1000:
    for i in range(2,n):

        if(n%i==0):
            n+=1
            break

    else:
        sum = sum + n
        print(n)
        n+=1
        c+=1
print(sum)        
