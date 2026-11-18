# N = int(input("enter no of row : "))
# for i in range(N):
#     for j in range(i+1):
#         print(chr(65+i),end=" ")
#     print()

# N = int(input("enter no of row : "))
# for i in range(N):
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print()


# N = int(input("enter no of row : "))
# num=0
# for i in range(N):
#     for j in range(i+1):
#         print(chr(65+num),end=" ")
#         num+=1
#     print()

N = int(input("enter the row : "))
for i in range(N):
    print(" "*(N-i+1),end=" ")
    for j in range(2*i+1):
        print(chr(65+j),end=" ")
    print()