
# 2. [Graph Search Shortest Paths and Data Structures](https://www.coursera.org/learn/algorithms-graphs-data-structures)

## Week 1: [SCC](https://github.com/keithpink/algorithms_specialization/blob/main/Graph_Search_Shortest_Paths_and_Data_Structures/scc.py)

**Question**: compute the sizes of the 5 largest strongly conncected component(SCCs).

['scc.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Graph_Search_Shortest_Paths_and_Data_Structures/SCC.txt.zip) contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex)


## Week 2: [Dijkstra's Algorithm](https://github.com/keithpink/algorithms_specialization/blob/main/Graph_Search_Shortest_Paths_and_Data_Structures/dijkstra.py)

**Question**: compute the shortest-path distances.

['dijkstraData.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Graph_Search_Shortest_Paths_and_Data_Structures/dijkstraData.txt) contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200.  Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197.


## Week 3: [Median Maintenance](https://github.com/keithpink/algorithms_specialization/blob/main/Graph_Search_Shortest_Paths_and_Data_Structures/Median.py)

**Question**: maintain the median of a given list of numbers

['Median.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Graph_Search_Shortest_Paths_and_Data_Structures/Median.txt) a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Compute the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). 

## Week 4: [Prob-2Sum](https://github.com/keithpink/algorithms_specialization/blob/main/Graph_Search_Shortest_Paths_and_Data_Structures/prob-2sum.py)

**Question**: compute distinct 2sum combinations.

['Prob-2Sum.txt'](https://github.com/keithpink/algorithms_specialization/blob/main/Graph_Search_Shortest_Paths_and_Data_Structures/prob-2sum.txt) contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the i<sup>th</sup> row of the file specifying the i<sup>th</sup> entry of the array.

Your task is to compute the number of target values tt in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t.
