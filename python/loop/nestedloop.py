# for i in range(3):
#     for j in range(3):
#         print("*", end=" ")
#     print()
# output
# * * * 
# * * * 
# * * *

n=5
for i in range(n):
    print(" "*(n-i-1),end=" ")
    print("s"*(2*i+1))
    


