A = str(input())
N = A.count(" ")
A = A.split(" ")
Ans = "NO"
for i in range (N+1):
    for j in range (i+1):
        if A[i] == A[j]:
            Ans = "YES"
print(Ans)