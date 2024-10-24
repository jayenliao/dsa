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
