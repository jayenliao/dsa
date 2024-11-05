# Algorithms for Searching, Sorting, and Indexing

## Module 1: Basics

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

## Module 2: Basic Data Structures and Heaps

### Problem 1: Least-k Elements Data Structure

We saw how min-heaps can efficiently allow us to query the least element in a heap (array). We would like to modify minheaps in this exercise to design a data structure to maintain the __least k__ elements for a  given $k \geq 1$ with $$k = 1$$ being the minheap data-structure.

Our design is to hold two arrays:
  - (a) a sorted array `A` of $k$ elements that forms our least k elements and
  - (b) a minheap `H` with the remaining $n-k$ elements.

Our data structure will itself be a pair of arrays `(A,H)` with the following property:
 - `H` must be a minheap
 - `A` must be sorted of size $k$.
 - Every element of `A` must be smaller than every element of `H`.

The key operations to implement in this assignment include:
  - insert a new element into the data-structure
  - delete an existing element from the data-structure.

### (A) Design Insertion  Algorithm

Suppose we wish to insert a new element with key $j$ into this data structure. Describe the pseudocode. Your pseudocode must deal with two cases: when the inserted element $j$ would be one of the `least k` elements i.e, it belongs to the array `A` or when the inserted element belongs to the heap `H`. How would you distinguish between the two cases?

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

## Module 3

### Problem 1: Design a Correct Partition Algorithm

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

### Problem 2. Rapid Sorting of Arrays with Bounded Number of Elements.

Thus far, we have presented sorting algorithms that are comparison-based. Ie., they make no assumptions about the elements in the array just that we have a `<=` comparison operator. We now ask you to develop a rapid sorting algorithm for an array of size $n$ when it is given to you that all elements in the array are between $1, \ldots, k$ for a given $k$. Eg., consider an array with n = 100000 elements wherein all elements are between 1,..., k = 100.

Develop a sorting algorithm using partition that runs in $\Theta(n \times k)$ time for such arrays. __Hint__ You can choose your pivots in a simple manner each time.

Complete the implementation of a function `boundedSort(a, k)` by completing the `simplePatition` function. Given an array `a` and a fixed `pivot` element, it should partition the array "in-place" so that all elements `<= pivot` are on one side of the array and elements `> pivot` on the other.  You should not create a new array in your code.

```python
def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]

def simplePartition(a, pivot):
    ## To do: partition the array a according to pivot.
    # Your array must be partitioned into two regions - <= pivot followed by elements > pivot
    ## If an element at the beginning of the array is already <= pivot in the beginning of the array, it should not
    ## be moved by the algorithm.

    '''your code here'''

def boundedSort(a, k):
    for j in range(1, k):
        simplePartition(a, j)
```

### Problem 3: Design a Universal Family Hash Function

Suppose we are interested in hashing $n$ bit keys into $m$ bit hash values to hash into a table of size
$2^m$. We view our key  as a bit vector of $n$ bits in binary. Eg., for $n = 4$, the key $14 = \left(\begin{array}{c} 1\\ 1\\ 1\\ 0 \end{array} \right)$.

The hash family is defined by random boolean matrices $H$ with $m$ rows and $n$ columns. To compute the hash function, we perform a matrix multiplication. Eg., with $m = 3$ and $n= 4$, we can have a matrix $H$ such as

$$ H = \left[ \begin{array}{cccc} 0 & 1 & 0 & 1 \\
1 & 0 & 0 & 0 \\
1 & 0 & 1 & 1 \\
\end{array} \right]$$.


The value of the hash function $H(14)$ is now obtained by multiplying

$$ \left[ \begin{array}{cccc} 0 & 1 & 0 & 1 \\
1 & 0 & 0 & 0 \\
1 & 0 & 1 & 1 \\
\end{array} \right] \times \left( \begin{array}{c}
1\\
1\\
1\\
0
\end{array} \right) $$

The matrix multiplication is carried out using AND for multiplication and XOR instead of addition. For the example above, we compute the value of hash function as

$$\left( \begin{array}{c}
 0 \cdot 1 + 1 \cdot 1 + 0 \cdot 1 + 1 \cdot 0 \\
 1 \cdot 1 + 0 \cdot 1 + 0 \cdot 1 + 0 \cdot 0 \\
 1 \cdot 1 + 0 \cdot 1 + 1 \cdot 1 + 1 \cdot 0 \\
 \end{array} \right) = \left( \begin{array}{c} 1 \\ 1 \\ 0 \end{array} \right)$$

(A) For a given matrix $H$ and two  keys $x, y$ that differ only in their $i^{th}$ bits, provide a condition for
$Hx = Hy$ holding. (**Hint** It may help to play with examples where you have two numbers $x, y$ that just differ at a particular bit position. Figure out which entries in the matrix are multiplied with these bits that differ).

(B) Prove that the probability that two keys $x, y$ such that $x \not= y$ collide under the random choice of a matrix $x, y$ is at most $\frac{1}{2^m}$.

```python
from random import random

def dot_product(lst_a, lst_b):
    and_list = [elt_a * elt_b for (elt_a, elt_b) in zip(lst_a, lst_b)]
    return 0 if sum(and_list)% 2 == 0 else 1

# encode a matrix as a list of lists with each row as a list.
# for instance, the example above is written as the matrix
# H = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]
# encode column vectors simply as a list of elements.
# you can use the dot_product function provided to you.
def matrix_multiplication(H, lst):
    '''your code here'''

# Generate a random m \times n matrix
# see the comment next to matrix_multiplication for how your matrix must be returned.
def return_random_hash_function(m, n):
    # return a random hash function wherein each entry is chosen as 1 with probability >= 1/2 and 0 with probability < 1/2
    '''your code here'''
```

## Module 4

In this assignment, we will explore countmin sketches and bloom filters. We will use two text files `great-gatsby-fitzgerald.txt` and `war-and-peace-tolstoy.txt` to load up the text of two famous novels courtesy of Project Guttenberg.

We will explore two tasks:
  - Counting the frequency of words of length 5 or more in both novels using a count-min sketch
  - Using a bloom filter to approximately count how many words in the War and Peace novel already appears in the Great Gatsby.

### Step 1:  Making a Universal Hash Family

We will use a family of hash function that first starts by (a) generating a random prime number $p$ (we will use the Miller-Rabin primality test for this purpopse) (b) generating random numbers a, b between 2 and p-1.

The hash function $h_{a,b,p} (n) = (an + b) \mod p$.

Note that this function will be between 0 and p-1. We will need to also make sure to take the hash value modulo $m$ where $m$ is the size of the hashtable.

To hash strings, we will first use python's inbuilt hash function and then use $h_{a,b,p}$ on the result.

As a first step, we will generate a random prime number.

#### (A) Generate Random Prime Numbers

```python
# Python3 program Miller-Rabin randomized primality test
# Copied from geeksforgeeks: https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
import random

# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):

  # Initialize result
  res = 1

  # Update x if it is more than or
  # equal to p
  x = x % p
  while (y > 0):

    # If y is odd, multiply
    # x with result
    if (y & 1):
      res = (res * x) % p

    # y must be even now
    y = y>>1 # y = y/2
    x = (x * x) % p

  return res

def miillerTest(d, n):
  '''
  This function is called for all k trials.
  It returns false if n is composite and returns false if n is probably prime.
  d is an odd number such that d*2<sup>r</sup> = n-1 for some r >= 1
  '''
  # Pick a random number in [2..n-2]
  # Corner cases make sure that n > 4
  a = 2 + random.randint(1, n - 4)

  # Compute a^d % n
  x = power(a, d, n)

  if (x == 1 or x == n - 1):
    return True

  # Keep squaring x while one
  # of the following doesn't
  # happen
  # (i) d does not reach n-1
  # (ii) (x^2) % n is not 1
  # (iii) (x^2) % n is not n-1
  while (d != n - 1):
    x = (x * x) % n
    d *= 2

    if (x == 1):
      return False
    if (x == n - 1):
      return True

  # Return composite
  return False

def isPrime( n, k):
  '''
  It returns false if n is composite and returns true if n is probably prime.
  k is an input parameter that determines accuracy level.
  Higher value of k indicates more accuracy.
  '''
  # Corner cases
  if (n <= 1 or n == 4):
    return False
  if (n <= 3):
    return True

  # Find r such that n =
  # 2^d * r + 1 for some r >= 1
  d = n - 1
  while (d % 2 == 0):
    d //= 2

  # Iterate given nber of 'k' times
  for i in range(k):
    if (miillerTest(d, n) == False):
      return False

  return True

# Driver Code
# Number of iterations
k = 4

print("All primes smaller than 100: ")
for n in range(1,100):
  if (isPrime(n, k)):
    print(n , end=" ")
# This code is contributed by mits (see citation above)
```

### Step 2: Universal Hash Families

We provide three useful functions for you:

- `get_random_hash_function`: Generate triple of numbers `(p, a, b)` at random, where p is  prime, a and b are numbers between 2 and p-1. The hash function $h_{p,a,b}(n)$ is given by $ (an + b) \mod p$.

- `hashfun`: apply the random hash function on a number `num`.

 - `hash_string`: apply the hash function on a string `hstr`. Note that the result is between 0 and p-1. If your hash table has size `m`, you should take a `mod m` on this result where you call `hash_string`.

Please use these functions in your code below.

```python
# Get a random triple (p, a, b) where p is prime and a,b are numbers betweeen 2 and p-1
def get_random_hash_function():
    n = random.getrandbits(64)
    if n < 0:
        n = -n
    if n % 2 == 0:
        n = n + 1
    while not isPrime(n, 20):
        n = n + 1
    a = random.randint(2, n-1)
    b = random.randint(2, n-1)
    return (n, a, b)

# hash function fora number
def hashfun(hfun_rep, num):
    (p, a, b) = hfun_rep
    return (a * num + b) % p

# hash function for a string.
def hash_string(hfun_rep, hstr):
    n = hash(hstr)
    return hashfun(hfun_rep, n)

def get_random_hash_function():
    n = random.getrandbits(32)
    if n < 0:
        n = -n
    if n % 2 == 0:
        n = n + 1
    while not isPrime(n, 20):
        n = n + 1
    a = random.randint(2, n-1)
    b = random.randint(2, n-1)
    return (n, a, b)
```

### Step 3: Loading Data

We are going to load two files `great-gatsby-fitzgerald.txt` and `war-and-peace-tolstoy.txt` to load up the text of two famous novels courtesy of Project Guttenberg. We will filter all wordsd of length >= 5 and also count the frequency of each word in a dictionary. This will be fast because it is going to use highly optimized hashtable (dictionaries) built into python.

```python
# Let us load the "Great Gatsby" novel and extract all words of length 5 or more
filename = 'great-gatsby-fitzgerald.txt'
file = open (filename,'r')
txt = file.read()
txt = txt.replace('\n',' ')
words= txt.split(' ')
longer_words_gg = list(filter(lambda s: len(s) >= 5, words))
print(len(longer_words_gg))
# Let us count the precise word frequencies
word_freq_gg = {}
for elt in longer_words_gg:
    if elt in word_freq_gg:
        word_freq_gg[elt] += 1
    else:
        word_freq_gg[elt] = 1
print(len(word_freq_gg))

# Let us load the "War and Peace" novel by Tolstoy translation and extract all words of length 5 or more
filename = 'war-and-peace-tolstoy.txt'
file = open (filename,'r')
txt = file.read()
txt = txt.replace('\n',' ')
words= txt.split(' ')
longer_words_wp = list(filter(lambda s: len(s) >= 5, words))
print(len(longer_words_wp))
word_freq_wp = {}
for elt in longer_words_wp:
    if elt in word_freq_wp:
        word_freq_wp[elt] += 1
    else:
        word_freq_wp[elt] = 1
print(len(word_freq_wp))
```

### Problem 1: Implement count-min sketch

Implement `CountMinSketch` class below where `num_counters` is the number of counters.  You are given the constructor that already generates a random representative of a hash function family. Implement the functions:
  - `increment`
  - `approximateCount`.

Please read the constructor carefully: it initializes the counters and generates the hash function for you.
Also, when you call `hash_string` function defined previously, do not forget to take result modulo m.

```python
# Class for implementing a count min sketch "single bank" of counters
class CountMinSketch:
    # Initialize with `num_counters`
    def __init__ (self, num_counters):
        self.m = num_counters
        self.hash_fun_rep = get_random_hash_function()
        self.counters = [0]*self.m

    # function: increment
    # given a word, increment its count in the countmin sketch
    def increment(self, word):
        '''your code here'''

    # function: approximateCount
    # Given a word, get its approximate count
    def approximateCount(self, word):
        '''your code here'''

# We will now implement the algorithm for a bank of k counters

# Initialize k different counters
def initialize_k_counters(k, m):
    return [CountMinSketch(m) for i in range(k)]

# Function increment_counters
# increment each of the individual counters with the word
def increment_counters(count_min_sketches, word):
    '''your code here'''

# Function: approximate_count
# Get the approximate count by querying each counter bank and taking the minimum
def approximate_count(count_min_sketches, word):
    return min([cms.approximateCount(word) for cms in count_min_sketches])
```
