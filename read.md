# Problem 0

Implement the Fibonacci sequence:
# Below is a Python implementation of the recursive Fibonacci function:

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# When I step through the execution of fib(5) in a debugger, here is the sequence of recursive calls I observe:

fib(5)
    -> fib(4) 
        -> fib(3)
            -> fib(2)
                -> fib(1)
                -> fib(0)
            -> fib(1)
        -> fib(2)
            -> fib(1) 
            -> fib(0)
    -> fib(3)
        -> fib(2)
            -> fib(1)
            -> fib(0)
        -> fib(1)
# So the full sequence of recursive calls for fib(5) is:

fib(5) 
-> fib(4)  
--> fib(3)
---> fib(2)
-----> fib(1)
-----> fib(0)  
---> fib(1)
--> fib(2)
----> fib(1)
----> fib(0)
-> fib(3)
--> fib(2)
-----> fib(1) 
-----> fib(0)
--> fib(1)

## PROBLEM 1:
1:Code uploaded in github as problem1.py

2: Time Complexity Analysis:
    
Initialize min heap with first element from each array:
Takes O(K) time where K is number of input arrays
Popping/pushing elements:
Each pop + push takes O(logK) time
Need to pop/push N*K elements in total
Adding to final result array:
O(1) per element
So overall time complexity:

Init min heap: O(K)
NK pop/push: O((NK) * logK)
Build result: O(N*K)
Total time = O(K + (NK)logK)= O(NKlogK)

3: Improvements:
     
1:Could use standard merge procedure instead of min heap:
2:Reduces overhead from logK to constant time per operation
3:Could multi-thread the merge process:
4:Each thread handles subset of arrays
5:Merge threads at end
6:Reduces time complexity to O(NKlog(K/p)) for p threads.

## PROBLEM 2
1: Code uploaded in github as problem2.py

2: Time Complexity Analysis:

The array is traversed only once using a for loop from index 1 till the end.
Each element is checked against the previous one for duplication in constant time.
No additional data structure like set is used.
So the overall time complexity is O(N) where N is the number of elements in the input array.

3:Improvements:

We could potentially skip entire sequences of duplicated numbers in O(1) extra time by checking nums[j] == nums[j-1] before doing the comparison with nums[i].
The algorithm can be parallelized by dividing the array into segments and having each thread remove duplicates in its segment separately. The results can then be merged.

### AUTHOR-PRIYANKA