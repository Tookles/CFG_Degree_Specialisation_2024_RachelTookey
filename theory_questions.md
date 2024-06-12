**1.1 The deque module is part of which python library?** 

Collections 

**1.2 What are 2 differences that distinguish a tree from a graph?** 

A tree is acyclic, whereas graphs can be both acyclic and cyclic. 

A tree has a unique node known as the root. A graph does not have this. 

**1.3 Give the definitions of time complexity and space complexity**

Time complexity quantifies the amount time / how fast an algorithm runs in relation to the length of the input. 

Space complexity quantifies how much auxiliary memory an algorithm takes up in relation to the length of the input. 

**1.4 Describe the bubble sort algorithm and its complexity. What is guaranteed at the end of the first pass?**

The bubble sort algorithm begins at the start of an iterable input, and while traversing up it, repeatedly swaps the adjacent elements if they are in the wrong order.

It repeatedly passes through the unsorted parts of the algorithm until the list is sorted. 

At the end of the first pass, the highest or largest item in the iterable will be sorted, or in other words, placed at the top /end of the list

As, it repeatedly passes through the unsorted part of the list, this is the equivalent of a nested loop so the time complexity is O(n^2).

The space complexity is 0(1) as it needs a constant amount of additional temporary space to store variables with the sorting process. 
The amount of space does not depend on the input size. 

**1.5 Explain what LIFO and FIFO are and how each works in practice with a named data structure**

LIFO: 

LIFO stands for "Last in First out". 
It is when insertion and deletion into a linear data structure happen at the same end, known as the top. 
So the item that is inserted last is deleted first. 
It is represented by a stack data structure and can be visualised like this: 

![Last in First out.png](Last%20in%20First%20out.png)

A stack can be implemented using a list/array or a linked list via a custom class. 
An example of a stack in action would be the previous page history on your browser - every time you click on a new page, that page is added to the top of the stack. 
Any time you click 'back', that page is removed and the item before it is now at the top of the stack. 

FIFO: 

FIFO stands for "First in First Out". 
It is when insertion and deletion into a linear data structure happen at opposite ends. 
It is represented by using a queue data structure and can be visualised like this: 

![First in First Out.png](First%20in%20First%20Out.png)

New data items are added to the rear of the queue - known as to enqueue. 
Data items are removed from the front of the queue - known as to dequeue. These will be the oldest items in the queue. 
It can be implemented using a list, the deque module from the collections library, or the queue.Queue module.  
Among a myriad of uses, Queues are used in algorithms like breadth first search. 

**1.6 What is a Balanced Binary Tree and what would be the best root? Walkthrough how you search using this structure**

A balanced binary tree is a binary tree where the height of the left and right subtrees of every node differs by no more than 1.

The best root of a balanced binary tree is the middle value of the data. This would ensure the data is evenly spaced between both sides. 

You would search this structure by traversing down from the root and at each step, choosing between the left or right child node. 
At each step, the left node will be a smaller value to the parent node, and the right node will be a greater value.
If searching for a given input, you will compare each node to the input and select left or right based on whether that node is greater than or smaller than your input. 
You do this until you find the correct value or the final node selected does not have a right or left child. 