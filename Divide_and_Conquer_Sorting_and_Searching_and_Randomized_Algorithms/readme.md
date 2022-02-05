## 1. [Divide and Conquer Sorting and Searching and Randomized Algorithms](https://www.coursera.org/learn/algorithms-divide-conquer/home/welcome)


### Week 1: [Karatsuba Multiplication](https://github.com/keithpink/algorithms_specialization/blob/main/Divide_and_Conquer_Sorting_and_Searching_and_Randomized_Algorithms/KM.py)

**Question**: what's the product of the following two 64-digit numbers?

- 3141592653589793238462643383279502884197169399375105820974944592

- 2718281828459045235360287471352662497757247093699959574966967627

To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers


---
### Week 2: [Inversion Compution](https://github.com/keithpink/algorithms_specialization/blob/main/Divide_and_Conquer_Sorting_and_Searching_and_Randomized_Algorithms/IntegerArray.py)

**Question**: compute the number of inversions in the file given.

['Integer.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Divide_and_Conquer_Sorting_and_Searching_and_Randomized_Algorithms/IntegerArray.txt) contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated. The i<sup>th</sup> row of the file indicates the i<sup>th</sup> entry of an array.


---
### Week 3: [QuickSort](https://github.com/keithpink/algorithms_specialization/blob/main/Divide_and_Conquer_Sorting_and_Searching_and_Randomized_Algorithms/QuickSort.py)

**Question**: compute the total number of comparisons used to sort the given input file by QuickSort.

['QuickSort.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Divide_and_Conquer_Sorting_and_Searching_and_Randomized_Algorithms/QuickSort.txt)
contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the i<sup>th</sup> row of the file gives you the i<sup>th</sup> entry of an input array. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules:

* first element as the pivot
* last element as the pivot
* "median of the three" as the pivot 

You should not count comparisons one-by-one.  Rather, when there is a recursive call on a subarray of length mm, you should simply add 
*m−1* to your running total of comparisons.  (This is because the pivot element is compared to each of the other *m−1* elements in the subarray in this recursive call.)


---
### Week 4:[Min Cut](https://github.com/keithpink/algorithms_specialization/blob/main/Divide_and_Conquer_Sorting_and_Searching_and_Randomized_Algorithms/kargerMinCut.py)

**Question**: compute the min cut of the given graph.

['kargerMinCut.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Divide_and_Conquer_Sorting_and_Searching_and_Randomized_Algorithms/kargerMinCut.txt) contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. 

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut.



