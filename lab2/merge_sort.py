import math
def merge_sort(A, p, r):
    if p<r:
        q = math.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = A[p:q+1]
    R = A[q+1:r+1]

    L.append(float("inf"))
    R.append(float("inf"))

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1