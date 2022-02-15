# 4. [Shortest Paths Revisited, NP-Complete Problems](https://www.coursera.org/learn/algorithms-npcomplete)

## Week 1: [Shortest Path]()

**Question: compute the "shortest shortest path"**

['g1.txt'](), ['g2.txt']() and ['g3.txt']() describe three graphs. Question 1
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem.  Here are data files describing three graphs: The first line indicates the number of vertices and edges, respectively.  Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number).  NOTE: some of the edge lengths are negative.  NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path".  Precisely, you must first identify which, if any, of the three graphs have no negative cycles.  For each such graph, you should compute all-pairs shortest paths and remember the smallest one.

## Week 2: [TSP]()

**Question: solve the traveling salesman problem**

['tsp.txt']() is a data file describing a TSP instance. The first line indicates the number of cities.  Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city. The distance between two cities is defined as the Euclidean distance. Compute the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.

## Week 3: [Heuristic for TSP]()

**Question: implement a heuristic for the TSP**

['nn.txt']() describes a TSP instance. The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city. The distance between two cities is defined as the Euclidean distance You should implement the nearest neighbor heuristic:

1. Start the tour at the first city.

2. Repeatedly visit the closest city that the tour hasn't visited yet.  In case of a tie, go to the closest city with the lowest index.  For example, if both the third and fifth cities have the same distance from the first city (and are closer than any other city), then the tour should begin by going from the first city to the third city.

3. Once every city has been visited exactly once, return to the first city to complete the tour.

## Week 4: [2SAT]()

**Question: solve the 2SAT problem**

'2sat1'~'2sat6' are 6 different 2SAT instances. In each instance, the number of variables and the number of clauses is the same, and this number is specified on the first line of the file.  Each subsequent line specifies a clause via its two literals, with a number denoting the variable and a "-" sign denoting logical "not".  For example, the second line of the first data file is "-16808 75250", which indicates the clause NOT x<sub>16808</sub> OR x<sub>75250</sub>.

Your task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable.  
