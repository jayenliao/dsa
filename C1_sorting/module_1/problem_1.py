### Problem 1

def findCrossoverIndexHelper(x, y, left, right):
    '''
    First, we create a "helper" function with two extra parameters
    left, right that describes the search region as shown below
    Note: Output index i such that
      left <= i <= right
      x[i] <= y[i]
    # First, Write down our  here
    '''
    # Invariant assertions
    assert(len(x) == len(y))
    assert(left >= 0)
    assert(left <= right-1)
    assert(right < len(x))

    # Key properties that we'd like to maintain.
    assert(x[left] > y[left])
    assert(x[right] < y[right])

    if x[left] >= y[left] and x[left+1] < y[left+1]:
        return left
    if x[right] < y[right] and x[right-1] >= y[right-1]:
        return right-1

    #
def findCrossoverIndex(x, y):
    '''
    Define the function findCrossoverIndex calling the helper function findCrossoverIndexHelper
    '''
    n = len(x)
    assert(n == len(y))
    assert(x[0] > y[0])
    assert(x[n-1] < y[n-1]) # Note: this automatically ensures n >= 2

    left = 0
    right = n - 1
    while (left < right):
        i = findCrossoverIndexHelper(x, y, left, right)
        if i is not None:
            return i
        left += 1
        right -= 1

if __name__ == '__main__':
    # BEGIN TEST CASES

    j1 = findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 5, 6, 7, 8, 9])
    print('j1 = %d' % j1)
    assert j1 == 1, "Test Case # 1 Failed"

    j2 = findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 4.2, 4.3, 4.5, 8, 9])
    print('j2 = %d' % j2)
    assert j2 == 1 or j2 == 5, "Test Case # 2 Failed"

    j3 = findCrossoverIndex([0, 1], [-10, 10])
    print('j3 = %d' % j3)
    assert j3 == 0, "Test Case # 3 failed"

    j4 = findCrossoverIndex([0,1, 2, 3], [-10, -9, -8, 5])
    print('j4 = %d' % j4)
    assert j4 == 2, "Test Case # 4 failed"

    print('All test cases passed')
    #END TEST CASES
