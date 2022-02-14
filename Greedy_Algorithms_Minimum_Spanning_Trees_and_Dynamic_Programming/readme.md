# 3. [Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming](https://www.coursera.org/learn/algorithms-greedy?specialization=algorithms)

## Week 1: [Greedy Algorithms](https://github.com/keithpink/algorithms_specialization/blob/main/Greedy_Algorithms_Minimum_Spanning_Trees_and_Dynamic_Programming/greedy.py)

1. **Question: minimize the weighted sum of job completion times**

['jobs.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Greedy_Algorithms_Minimum_Spanning_Trees_and_Dynamic_Programming/jobs.txt) describes a set of jobs with positive and integral weights and lengths.For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.

  - run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). 
  - run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length)

2. **Question: minimum spanning tree**

['edges.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Greedy_Algorithms_Minimum_Spanning_Trees_and_Dynamic_Programming/edges.txt) describes an undirected graph with integer edge costs. For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874. You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph.

## Week 2: [K-clustering](https://github.com/keithpink/algorithms_specialization/blob/main/Greedy_Algorithms_Minimum_Spanning_Trees_and_Dynamic_Programming/greedy.py)

1. **Question: what is the maximum spacing of a 4-clustering?**

['clustering1.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Greedy_Algorithms_Minimum_Spanning_Trees_and_Dynamic_Programming/clustering1.txt) file describes a distance function (equivalently, a complete graph with edge costs). For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250.  You can assume that distances are positive, but you should NOT assume that they are distinct.

2. **Question: what is the largest value of kk such that there is a kk-clustering with spacing at least 3?**

['clustering2.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Greedy_Algorithms_Minimum_Spanning_Trees_and_Dynamic_Programming/clustering2.txt) is a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list. The distance between two nodes u and v in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

## Week 3

## Week 4
