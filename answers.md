# CMPS 6610 Problem Set 05
## Answers


**Name:**$\underline{\hspace{1in}\text{Rob Hartley}\hspace{1in}}$


## 1. Shortest shortest paths


**1b) (4 pts)** Work and span  

Initilizing the best dictionary requires: $O(|V|)$  
Initializing pq: $O(1)$  
Process vertices and edges in the nested While..For loop: $O(|V| + |E|)$  
Heap operations heappush() and heappop(): $O(\log|V|)$  
Return the dictionary: $O(1)$  

Because each edge processed in the While..For loop can potentially call a heappush() operation and each record pushed can potentially call a heappop() operation, there is a potential of $O(|V| + |E|)$ heap operations, each of which costs $O(\log|V|)$ under simple graph assumption: 

$W(|V|,|E|) = O((|V| + |E|)\log|V|) + O(|V|) + O(1) + O(|V| + |E|) + O(1)$

$\boxed{W(|V|,|E|) = O((|V| + |E|)\log|V|)}$  

Because there is no parallelism, span will equal work:  

$\boxed{S(|V|,|E|) = O((|V| + |E|)\log|V|)}$



## 2. Expression Trees


**2a) (3 pts)** Expression tree algorithm with work and span  

```python  
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_expression_tree(expression):
    operands = []
    operators = []

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    def apply_operator():
        operator = operators.pop()

        right = operands.pop()
        left = operands.pop()

        new_node = Node(operator, left, right)
        operands.append(new_node)

    for token in expression.split():

        # Step 1: Encounter a number
        if token.isdigit():
            operands.append(Node(int(token)))

        # Step 1.5: Encounter a variable
        elif token.isidentifier():
            operands.append(Node(token))

        # Step 2: Encounter an opening parenthesis
        elif token == '(':
            operators.append(token)

        # Step 3: Encounter a closing parenthesis
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator()

            operators.pop()  # Remove '('

        # Step 4: Encounter an operator
        elif token in precedence:

            while (operators and
                   operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[token]):
                apply_operator()

            operators.append(token)

    # Step 5: Apply remaining operators
    while operators:
        apply_operator()

    # Step 6: Return the root
    return operands.pop()
```
The work for most of the operations involved in $O(1)$. Although the algorithm does contain nested while loops, each operator is pushed and popped from its respective stack exactly once. The algorithm assumes non-negative integers; it can't process decimals or negative numbers.
expression.split() = $\Theta(n)$  
iterate through all the tokens =  $\Theta(n)$  
Apply remaining operators = $O(n)$  

$\boxed{W(n) = \Theta(n)}$  

The algorithm contains no parallelism, so span is the same as work.  

$\boxed{S(n) = \Theta(n)}$ 



**2b) (2 pts)** Corresponding arithmetic expression work and span?  

Tree $T_E$ can be evaluated recursively. Each leaf provides a value, and each internal node applies the operator it contains to the values returned by its two children. Every node is processed in $O(1)$ constant time, so we end up with the same work as before.  

$\boxed{W(n) = \Theta(n)}$   

The span is different, however. Because we're evaluating the left and right trees in parallel, but each parent node must wait for its children to process, the span will be based on the maxiumum depth of the tree, $d$.  

$\boxed{S(n) = \Theta(d)}$  

If the tree is balanced, this works out to:  

$\boxed{S(n) = \Theta(\log n)}$  

Worst case unbalanced tree can move the span up to:  

$\boxed{S(n) = \Theta(n)}$  



**2c) (2 pts)** work/span to update a previously computed value  

The asnwer is similar to 2b, in that the span wil be proportional to tree depth, but in this case because we're only updating one value the work is also proportional to tree depth (*assuming intermediate results are stored in the nodes and only one leaf is changing) we're only processing the change to variable and any required alterations along the affected path through the tree from the node change we're making to the root. For depth $d$, work and span are:  

$\boxed{W(n) = O(d)}$  

$\boxed{S(n) = O(d)}$

For a balanced tree, this works out to:  

$\boxed{W(n) = \Theta(\log n)}$  

$\boxed{S(n) = \Theta(\log n)}$  

Unbalanced tree in the worst case where we have an update path containing $\Theta(n)$ nodes:  

$\boxed{W(n) = \Theta(n)}$  

$\boxed{S(n) = \Theta(n)}$

## 3. Improving Dijkstra


**3a) (2 pts)** Maximum depth of a $d$-ary heap  

The maxiumn depth of a d-ary heap is $\Theta(\log_d n)$, where $d$ = the maxiumum number of children per node and $n$ = the number of nodes. The heap's shape property ensures that all levels except the bottom are completely filled, with the bottom level being filled from the left to the right. The height of the tree grows logarithmically with $n$, using base $d$.



**3b) (3 pts)** Work done by `delete-min` and `insert` operations in a $d$-ary heap.

Delete-min requires at most $O(d \cdot log_d n)$ work. The new root will travel downward through the heap by at most $log_d n$ levels, and it must examine up to $d$ children at each level in order to find the smallest child node to swap positions with.  

Insert requires at most $O(log_d n)$ work because it only has to compare the inserted value with one parent node per level to check for a potential position swap with that parent node as it moves up the tree.

**3c) (3 pts)** New bound on the work for Dijkstra's using $d$-ary heap 

Dijkstra's algorithm performs at most $O(|V|)$ delete-min operations. Because each delete-min operation costs at most $O(d \cdot log_d n)$ work and Dijkstra's algoritm will do at most $O(|V|)$ of them, total work for delete-min operations is $O(d|V|\log_d |V|)$.  

The algorithm will also process up to $O(|E|)$ priority queue insertions or updates. Each of those operatiosn is going to require at most $O(log_d n)$ work, which gives us a maximum total work of $O(|E|\log_d |V|)$ for the insertions and updates.  

Therefore, the maximum total work for Dijkstra's algorithm is:  

$\boxed{O((d|V| + |E|)(\log_d |V|))}$.


**3d) (3 pts)** What value of $d$ yields an overall running time of $O(|E|)$?  

 We start with the work equation from 3c, $W \in O((d|V| + |E|)(\log_d |V|))$.  
 Set $d|V| = |E|$, so that the delete-min work has the same asymptotic bound as the insertion and update work.  
 $d = \frac{|E|}{|V|}$  
 substitute target edge value: $d = \frac{|V|^{1 + \epsilon}}{|V|}$  
 $d = |V|^{\epsilon}$  
 substitute into main equation: $W = O((|V|^{\epsilon}|V| + |E|)(\log_{|V|^{\epsilon}} |V|))$  
 $W = O((|V|^{1 + \epsilon} + |E|)(\frac{1}{\epsilon}))$  
$W = O((2|E|)(\frac{1}{\epsilon}))$  
Constants absorbed by Big-O notation $|E|$.  

$\boxed{W \in O(|E|)}$


## 4. All-pairs shortest paths using Dynamic Programming

**4a) (2 pts)** Consider the following graph with 3 vertices.

![apsp_example.jpg](apsp_example.jpg)

Compute $\mathit{APSP}(i, j, k)$ for all $i, j, k$.  

There are three vertices, 0, 1, 2.
With $i$ representing the starting vertex by row, $j$ representing the destination vertex by column, the value at $(i, j)$ representing the minimum total weight of a walk from $i$ to $j$ using at most $k$ edges, and $k$ representing the maximum number of edges allowed on the path from $i$ to $j$, the three matrices below show the minimum total path weight for $0 \leq k \leq 2$ edges where walks are allowed to revisit vertices. The graph contains a negative cycle, so allowing additional edges can produce progressively smaller path weights, which is why it's important to limit the amount of edges used in order to prevent the path weights from decreasing without bound.

$
APSP(i,j,0) =
\begin{bmatrix}
0 & \infty & \infty \\
\infty & 0 & \infty \\
\infty & \infty & 0
\end{bmatrix}
$  

$
APSP(i,j,1) =
\begin{bmatrix}
0 & -2 & 2 \\
-2 & 0 & 1 \\
2 & 1 & 0
\end{bmatrix}
$  

$
APSP(i,j,2) =
\begin{bmatrix}
-4 & -2 & -1 \\
-2 & -4 & 0 \\
-1 & 0 & 0
\end{bmatrix}
$  

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


