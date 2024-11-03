def selection_sort(A:list):
    N = len(A)
    for i in range(N-1): # Before iteration i, A[0:(i-1)] has been sorted.
        idx_min = i # Set up the index of the minimum element of A[i:(N-1)].
        for j in range(i+1, N):
            if A[j] < A[idx_min]: # If the coming element A[j] is smaller than the current minimum element,
                idx_min = j       # replace the index.
        A[i], A[idx_min] = A[idx_min], A[i] # Swab



