
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f" Current list items : {a} \n")
def lessthan():
    
    lessthannum = int(input("Enter a number, will give you list of items less than that : "))

    b =[]
    for num in a :
        if num < lessthannum :
            b.append(num)

    print(f"list of numbers less than {lessthannum} is {b} ")

    lessthan()

lessthan()