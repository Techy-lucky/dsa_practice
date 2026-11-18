#  Count Even and Odd Numbers: Write a program to accept N integers into an array and count and display the number of even and odd elements present in the array. 

Array = []
evencount = 0
oddcount = 0
oddarray = []
evenarray = []
newarr = Array
N = int(input("enter the N integer value : "))
for i in range(0,N):
    M = int(input("enter your integer value : "))
    Array.append(M)

for sum in Array:
    if sum%2==0 :
        evencount += 1
        evenarray.append(sum)
    else :
        oddcount += 1
        oddarray.append(sum)

print(Array)
print(f"odd value count : {oddcount}")
print(f"even value count : {evencount}")
print(f"odd  list : {oddarray}")
print(f"even list : {evenarray}")

