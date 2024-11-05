# Algorithms for Searching, Sorting, and Indexing

## Chapter 1: Basics

- Basics of algorithms: correctness and running time complexity.
- Time Complexity: O, big-Omega and big-Theta Notations.
- Proving Correctness of Algorithms through Inductive Invariants.
- Merge Sort: Proving Correctness.

### Problem 1: Find Crossover Indices.

Data that consists of points
$(x_0, y_0), \ldots, (x_n, y_n)$, wherein $x_0 < x_1 < \ldots < x_n $, and  $y_0 < y_1 \ldots < y_n$ as well, is given.

Furthermore, it is given that $y_0 < x_0$ and $y_n > x_n$.

Find a "cross-over" index $i$ between $0$ and $n-1$ such that $y_i \leq x_i$ and $y_{i+1} > x_{i+1}$.

Note that such an index must always exist (convince yourself of this fact before we proceed).

__Example__

$$\begin{array}{c| c c c c c c c c c }
i & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
x_i & 0 & 2 & 4 & \color{red}{5} & \color{red}{6} & 7 & 8 & 10 \\
y_i & -2 & 0 & 2 & \color{red}{4} & \color{red}{7} & 8 & 10 & 12 \\
\end{array} $$

Your algorithm must find the index $i=3$ as the crossover point.

On the other hand, consider the data

$$\begin{array}{c| c c c c c c c c c }
i & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
x_i & \color{red}{0} & \color{red}{1} & 4 & \color{red}{5} & \color{red}{6} & 7 & 8 & 10 \\
y_i & \color{red}{-2} & \color{red}{1.5} & 2 & \color{red}{4} & \color{red}{7} & 8 & 10 & 12 \\
\end{array} $$

We have two cross over points. Your algorithm may output either $i=0$ or $i=3$.

### Problem 2: Find integer cube root.

The integer cube root of a positive number $n$ is the smallest number $i$ such that $i^3 \leq n$ but $(i+1)^3 > n$.

For instance, the integer cube root of $100$ is $4$ since $4^3 \leq 100$ but $5^3 > 100$. Likewise, the integer cube root of $1000$ is $10$.

Write a function `integerCubeRootHelper(n, left, right)` that searches for the integer cube-root of `n` between `left` and `right` given the following pre-conditions:
  - $n \geq 1$
  - $\text{left} < \text{right}$.
  - $\text{left}^3 < n$
  - $\text{right}^3 > n$.

### Problem 3: Develop Multiway Merge Algorithm

We studied the problem of merging 2 sorted lists `lst1` and `lst2` into a single sorted list in time $\Theta(m + n)$ where $m$ is the size of `lst1` and $n$ is the size of `lst2`.  Let `twoWayMerge(lst1, lst2)` represent the python function that returns the merged result using the approach presented in class.

In this problem, we will explore algorithms for merging `k` different sorted lists, usually represented as a list of sorted lists into a single list.

#### (A)

Suppose we have $k$ lists that we will represent as `lists[0]`, `lists[1]`, ..., `lists[k-1]` for convenience and the size of these lists are all assumed to be the same value $n$.

We wish to solve multiway merge by merging two lists at a time:

```
  mergedList = lists[0] # start with list 0
  for i = 1, ... k-1 do
      mergedList = twoWayMerge(mergedList, lists[i])
  return mergedList
```

Knowing the running time of the `twoWayMerge` algorithm as mentioned above, what is the overall running time of the algorithm in terms of $n, k$.

#### (B) Implement an algorithm that will implement the $k$ way merge by calling `twoWayMerge` repeatedly as follows:

1. Call `twoWayMerge` on consecutive pairs of lists `twoWayMerge(lists[0], lists[1])`, ... , `twoWayMerge(lists[k-2], lists[k-1])` (assume k is even).
2. Thus, we create a new list of lists of size `k/2`.
3. Repeat steps 1, 2 until we have a single list left.

## Chapter 2: Basic Data Structures and Heaps

### Problem 1: Least-k Elements Data Structure

We saw how min-heaps can efficiently allow us to query the least element in a heap (array). We would like to modify minheaps in this exercise to design a data structure to maintain the __least k__ elements for a  given $k \geq 1$ with $$k = 1$$ being the minheap data-structure.

Our design is to hold two arrays:
  - (a) a sorted array `A` of $k$ elements that forms our least k elements; and
  - (b) a minheap `H` with the remaining $n-k$ elements.

Our data structure will itself be a pair of arrays `(A,H)` with the following property:
 - `H` must be a minheap
 - `A` must be sorted of size $k$.
 - Every element of `A` must be smaller than every element of `H`.

The key operations to implement in this assignment include:
  - insert a new element into the data-structure
  - delete an existing element from the data-structure.

### (A) Design Insertion  Algorithm

Suppose we wish to insert a new element with key $j$ into this data structure. Describe the pseudocode. Your pseudocode must deal with two cases: when the inserted element $j$ would be one of the `least k` elements i.e, it belongs to the array `A`; or when the inserted element belongs to the heap `H`. How would you distinguish between the two cases?

- You can assume that heap operations such as `insert(H, key)` and `delete(H, index)` are defined.
- Assume that the heap is indexed as  `H[1]`,...,`H[n -k]` with `H[0]` being unused.
- Assume $ n > k$, i.e, there are already more than $k$ elements in the data structure.

### (B) Design Deletion Algorithm

Suppose we wish to delete an index $j$ from the top-k array $A$. Design an algorithm to perform this deletion. Assume that the heap is not empty, in which case you can assume that the deletion fails.

- You can assume that heap operations such as `insert(H, key)` and `delete(H, index)` are defined.
- Assume that the heap is indexed as  `H[1]`,...,`H[n -k]` with `H[0]` being unused.
- Assume $ n > k$, i.e, there are already more than $k$ elements in the data structure.

### Problem 2: MaxHeap

### Problem 3: Heap data structure to mantain/extract median (instead of minimum/maximum key)

We have seen how min-heaps can efficiently extract the smallest element efficiently and maintain the least element as we insert/delete elements. Similarly, max-heaps can maintain the largest element. In this exercise, we combine both to maintain the "median" element.

The median is the middle element of a list of numbers.
- If the list has size $n$ where $n$ is odd, the median is the $(n-1)/2^{th}$ element where $0^{th}$ is least and $(n-1)^{th}$ is the maximum.
- If $n$ is even, then we designate the median the average of the $(n/2-1)^{th}$ and $(n/2)^{th}$ elements.

__Example__

- List is $[-1, 5, 4, 2, 3]$ has size $5$, the median is the $2^{nd}$ element (remember again least element is designated as $0^{th}$) which is $3$.
- List is $[-1, 3, 2, 1 ]$ has size $4$. The median element is the average of  $1^{st}$ element (1) and $2^{nd}$ element (2) which is  $1.5$.

#### Maintaining median using two heaps.

The data will be maintained as the union of the elements in two heaps $H_{\min}$ and $H_{\max}$, wherein $H_{\min}$ is a min-heap and $H_{\max}$ is a max-heap.  We will maintain the following invariant:
  - The max element of  $H_{\max}$ will be less than or equal to the min element of  $H_{\min}$.
  - The sizes of $H_{max}$ and $H_{min}$ are equal (if number of elements in the data structure is even) or $H_{max}$ may have one less element than $H_{min}$ (if the number of elements in the data structure is odd).

#### (A)  Design algorithm for insertion.

Suppose, we have the current data split between $H_{max}$ and $H_{min}$ and we wish to insert an element $e$ into the data structure, describe the algorithm you will use to insert. Your algorithm must decide which of the two heaps will $e$ be inserted into and how to maintain the size balance condition.

Describe the algorithm below and the overall complexity of an insert operation. This part will not be graded.

## Chapter 3

## Problem 1: Design a Correct Partition Algorithm

You are given code below for an incorrect partition algorithm that fails to partition arrays wrongly or cause out of bounds access in arrays.  The comments include the invariants the algorithm wishes to maintain and will help you debug.

Your goal is to write test cases that demonstrate that the partitioning will fail in various ways.

```python
def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]

def tryPartition(a):
    # implementation of Lomuto partitioning algorithm
    n = len(a)
    pivot = a[n-1] # choose last element as the pivot.
    i,j = 0,0 # initialize i and j both to be 0
    for j in range(n-1): # j = 0 to n-2 (inclusive)
        # Invariant: a[0] .. a[i] are <= pivot
        #            a[i+1]...a[j-1] are > pivot
        if a[j] <= pivot:
            swap(a, i+1, j)
            i = i + 1
    swap(a, i+1, n-1) # place pivot in its correct place.
    return i+1 # return the index where we placed the pivot
```
