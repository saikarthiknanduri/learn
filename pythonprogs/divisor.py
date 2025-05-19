innum=int(input("enter a number to get all possible divisors : "))
x=list(range(2,int(innum/2)+1))
divisors=[]
for num in x :
    if innum%num == 0 :
        divisors.append(num)

print(f"divisors are {divisors}")

