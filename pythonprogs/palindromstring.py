inn = input("Enter a string to check if it is plaindrome : ")
# instr=list(inn)
# instr_copy=instr[:]

#reverse a string in python txt = "Hello World"[::-1]
inn2=inn[::-1]

# instr_copy.reverse()
# rev = "".join(instr_copy)
# print(inn)
# print(rev)
if inn == inn2 : 
    print(f"{inn} is a palindrome")
else:
    print("not a palindrome")


