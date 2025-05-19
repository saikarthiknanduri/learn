
def odd_even():
    print("Let's check odd or even number")
    num = int(input("Enter a number : "))
    if num%2 == 0 :
        print(f"{num} is a even number \n")
    else:
        print(f"{num} is an odd number \n")
    odd_even()

odd_even()
