# Write a program to accept N integers into an array and calculate and display the sum of all the elements.

New_arr = []
total = 0
N = int(input("enter how many number you want in your array list : "))
for i in range(0,N):
    M = int(input("enter the number : "))
    New_arr.append(M)
# total = sum(New_arr)
    total += M
print(f"list of array is : {New_arr}")
print(f"sum of array is : {total}")

