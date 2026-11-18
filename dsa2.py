# find the smallest and the largest element
# Write a program to accept N integers into an array and find and display the largest element, second largest element, smallest element, second smallest element present in the array.
array = []
N = int(input("enter how many number of list you want : "))
for i in range(0,N):
    M = int(input("enter your number : "))
    array.append(M)
print(array)
data = array
data.sort(reverse=True)
print(data)
print(f"largest element {data[0]}")
print(f"second largest element {data[1]}")
print(f"smallest element {data[-1]}")
print(f"second smallest element {data[-2]}")
