# CMPS 6610 Problem Set 05
## Answers


**Name:**_________________________


## 1. Shortest shortest paths


**1b) (4 pts)** Work and span 



## 2. Expression Trees


**2a) (3 pts)** Expression tree algorithm with work and span



**2b) (2 pts)** Corresponding arithmetic expression work and span?



**2c) (2 pts)** work/span to update a previously computed value



## 3. Improving Dijkstra


**3a) (2 pts)** Maximum depth of a $d$-ary heap



**3b) (3 pts)** Work done by `delete-min` and `insert` operations in a $d$-ary heap.



**3c) (3 pts)** New bound on the work for Dijkstra's using $d$-ary heap 



**3d) (3 pts)** What value of $d$ yields an overall running time of $O(|E|)$?
 


## 4. All-pairs shortest paths using Dynamic Programming

**4a) (2 pts)** Consider the following graph with 3 vertices.

![apsp_example.jpg](apsp_example.jpg)

Compute $\mathit{APSP}(i, j, k)$ for all $i, j, k$.



**4b) (3 pts)** Relationship between $\mathit{APSP}(i, j, 1)$ and
$\mathit{APSP}(i, j, 2)$. Can you write $\mathit{APSP}(i, j, 2)$ in
terms of $\mathit{APSP}(i, j, 0)$ and $\mathit{APSP}(i, j, 1)$ only?



**4c) (3 pts)** Generalize your observation from b) above to give an optimal substructure property for $\mathit{APSP}(i, j, k).$



**4d) (3 pts)** How many distinct subproblems will be computed from scratch, and
what is the resulting work of this dynamic programming algorithm?



**4e) (3 pts)** Compare the work of this algorithm against that of just running
Dijkstra $n$ times. Is our dynamic programming algorithm better than this?



## 5. Spanning trees

**5a) (3 pts)** Is a solution to MST guaranteed to be a solution to MMET? Why or why not?



**5b) (2 pts)** Suppose that the optimal solution to MST is impossible to use for some reason. Describe an algorithm to instead find the next best tree (pseudo-code or English is fine). That is, return the tree with the next lowest weight. 



**5c) (2 pts)** What is the work of your algorithm?


