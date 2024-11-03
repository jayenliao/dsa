import time

def selection_sort(A:list):
    N = len(A)
    for i in range(N-1): # Before iteration i, A[0:(i-1)] has been sorted.
        idx_min = i # Set up the index of the minimum element of A[i:(N-1)].
        for j in range(i+1, N):
            if A[j] < A[idx_min]: # If the coming element A[j] is smaller than the current minimum element,
                idx_min = j       # replace the index.
        A[i], A[idx_min] = A[idx_min], A[i] # Swab
    return A


def insertion_sort(A:list):
    N = len(A) # Number of elements
    for i in range(1, N): # Before iteration i, A[0:(i-1)] has been sorted.
        for j in range(i, 0, -1): # Iterate backwards from j to 0.
            if A[j-1] <= A[j]: # If the previous element is not larger than the current element,
                break          # meaning A[j] is loacted correctly, thus we break the nested loop.
            A[j], A[j-1] = A[j], A[j-1] # Otherwise, swap two elements.
    return A


def merge_sort(A:list):
    aux = [None] * len(A) # Set up an array with the same size as A

    def rsort(low, high):
        if high <= low: return # Basic condition
        mid = (low + high) // 2 # Recursion: sort the left and right sub-arrays and merge them.
        rsort(low, mid)
        rsort(mid+1, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        aux[low:(high+1)] = A[low:(high+1)] # Duplicate sorted sub-array to aux.
        left, right = low, mid+1 # Set up beginning indices for two sub-arrays.
        for i in range(low, high+1):
            if left > mid: # If the left sub-array has been empty, get a value from the right one.
                A[i] = aux[right]
                right += 1
            elif right > high: # If the right sub-array has been empty, get a value from the left one.
                A[i] = aux[left]
                left += 1
            elif aux[right] < aux[left]: # If the right value is smaller than the left one, get the right one.
                A[i] = aux[right]
                right += 1
            else:                        # If the left value is smaller than the left one, get the left one.
                A[i] = aux[left]
                left += 1

    rsort(0, len(A)-1)
    return A


if __name__ == "__main__":
    A = input("Enter an array sperating by spaces: ")
    A = [int(i) for i in A.split(" ")]
    print(f"Inputed array (size={len(A)}):")
    print(A)

    print("=== Selection sort ===")
    t0 = time.time()
    A_sorted = selection_sort(A)
    t1 = time.time()
    print("Sorted array:")
    print(A_sorted)
    print(f"Time cost: {t1 - t0} seconds")

    print("=== Insertion sort ===")
    t0 = time.time()
    A_sorted = insertion_sort(A)
    t1 = time.time()
    print("Sorted array:")
    print(A_sorted)
    print(f"Time cost: {t1 - t0} seconds")

    print("=== Merge sort ===")
    t0 = time.time()
    A_sorted = merge_sort(A)
    t1 = time.time()
    print("Sorted array:")
    print(A_sorted)
    print(f"Time cost: {t1 - t0} seconds")
