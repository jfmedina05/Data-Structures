# Data Structures

A collection of labs, homework assignments, programming exercises, and implementations developed for **A310: Problem Solving with Data** at Indiana University Bloomington.

This repository documents my progression through fundamental and intermediate data structures, algorithms, object-oriented programming, recursion, tree structures, numerical computing, and data-oriented problem solving using Python.

---

## Overview

The goal of this repository is to build a stronger understanding of how data structures and algorithms work internally rather than relying only on Python's built-in implementations.

Coursework includes both programming and handwritten exercises covering topics such as:

- Python programming
- Object-oriented programming
- Linked data structures
- Recursion
- Binary Search Trees
- AVL Trees
- Heaps
- Tree rotations
- Searching and traversal
- Array manipulation
- NumPy
- Multidimensional data
- Algorithmic problem solving
- Data organization and transformation

The repository contains a combination of:

- Jupyter Notebooks
- Python scripts
- Written data-structure exercises
- Visualizations
- In-class assignments
- Lab implementations
- Homework solutions

---

## Repository Structure

```text
Data-Structures/
│
├── Labs/
│   ├── Lab 01/
│   ├── ...
│   ├── Lab 04/
│   └── Lab 05/
│
├── Homeworks/
│   ├── Homework 01/
│   ├── Homework 02/
│   ├── Homework 03/
│   └── ...
│
├── Week 01/
│   ├── In-Class Assignment/
│   ├── Lab 1/
│   ├── Turtle_Drawing/
│   └── README.md
│
└── README.md
```

> The repository continues to grow as additional labs, homework assignments, and course exercises are completed.

---

# Coursework

## Week 01 — Python Review, Linked Structures, and File-Driven Programming

The first week focused on reviewing Python fundamentals while introducing linked data structures and file-driven programming.

### Linked List Practice

A simple linked structure was implemented using Python classes and object references.

Topics practiced include:

- Classes and objects
- Constructors
- Nodes
- Object references
- Recursive insertion
- Traversal of linked structures
- Visualizing memory relationships

A Python Tutor visualization was also used to examine how linked objects reference one another in memory.

### Turtle Drawing

The Turtle Drawing exercise uses external text instructions to control Python's `turtle` graphics library.

The program reads drawing commands from a file and translates them into Turtle operations such as:

```text
goto
circle
beginfill
endfill
penup
pendown
```

This exercise demonstrates how program logic can be separated from the data or instructions that drive the program.

---

# Labs

The `Labs` directory contains programming exercises that apply concepts introduced in lecture.

Labs emphasize implementation, experimentation, code tracing, and understanding how data structures behave.

---

## Lab 01 — Linked Structures

The first lab introduces linked nodes and recursive traversal using Python objects.

### Concepts

- Linked lists
- Nodes
- Object references
- Recursive methods
- Traversal
- Python object relationships

The implementation demonstrates how individual objects can be connected to construct a larger dynamic data structure.

---

## Lab 04 — Implementing a Binary Search Tree

Lab 04 focuses on implementing a **Binary Search Tree (BST) Abstract Data Type**.

The assignment extends a `BstNode` representation with core tree operations.

### Operations Implemented

```python
find()
insert()
remove()
```

### Concepts Practiced

- Binary Search Trees
- Recursive search
- Recursive insertion
- Tree traversal
- Pointer/reference manipulation
- BST ordering properties
- Node deletion
- Inorder successors

Deletion cases include:

- Removing a leaf node
- Removing a node with one child
- Removing a node with two children
- Removing the root

The lab also uses tree visualizations and printed structures to understand how references change as nodes are inserted and removed.

---

## Lab 05 — NumPy and Multidimensional Data

Lab 05 introduces **NumPy** and applies array operations commonly used in data science and numerical computing.

The lab builds familiarity with creating, inspecting, transforming, searching, and sorting NumPy arrays.

### Topics Covered

- Creating NumPy arrays
- One-dimensional arrays
- Two-dimensional arrays
- Three-dimensional arrays
- `ndim`
- `shape`
- Indexing
- Negative indexing
- Array slicing
- Slice steps
- NumPy data types
- `dtype`
- `astype()`
- Copies and views
- `base`
- Reshaping arrays
- Flattening arrays
- Concatenating arrays
- Stacking arrays
- Searching with `np.where()`
- Selective Boolean indexing
- Sorting
- Operations along different axes
- `np.average()`
- `np.sort()`

### Example

```python
import numpy as np

a = np.array([1, 2, 3, 4])

b = a.reshape(2, 2)

print(b)
```

Output:

```text
[[1 2]
 [3 4]]
```

The lab also applies NumPy to a small data-analysis problem involving salaries, tax rates, Boolean indexing, and finding a maximum after-tax income.

---

# Homeworks

The `Homeworks` directory contains larger exercises that combine conceptual data-structure work with Python programming.

---

## Homework 02 — Object-Oriented Programming and Binary Search Trees

Homework 02 combines Python object-oriented programming with handwritten Binary Search Tree operations.

### Complex Number Class

A custom `Complex` class practices Python operator overloading.

Implemented functionality includes:

```python
__init__()
__add__()
__mul__()
__str__()
```

This exercise demonstrates how Python operators can be customized for user-defined objects.

### Inheritance

A class hierarchy involving:

```text
Creature
├── Dog
└── Cow
```

demonstrates:

- Inheritance
- Method overriding
- Parent and child classes
- Polymorphic behavior

Each subclass provides its own implementation of behaviors such as `speak()`.

### Binary Search Tree Operations

The BST portion uses the insertion sequence:

```text
9, 2, 1, 10, 8, 3, 7, 4, 6, 5
```

The exercise then explores:

1. Building the BST through sequential insertion
2. Removing the root
3. Reinserting the removed value
4. Removing the root two additional times
5. Tracking structural changes after each operation

This work develops a stronger understanding of how BST deletion can reorganize a tree.

---

## Homework 03 — AVL Trees and Heaps

Homework 03 focuses on two important tree-based Abstract Data Types:

- **AVL Trees**
- **Heaps**

The same sequence of values is inserted into each structure so their behaviors can be compared.

```text
9, 2, 1, 10, 8, 3, 7, 4, 6, 5
```

---

### AVL Trees

The AVL portion tracks the tree after every insertion and identifies when rebalancing is required.

Concepts include:

- Binary Search Tree ordering
- Balance factors
- Tree height
- Detecting imbalance
- Left rotation
- Right rotation
- Left-right rotation
- Right-left rotation
- Rebalancing after insertion
- Rebalancing after deletion

Each insertion and rotation is treated as a separate structural step in order to clearly show how an AVL tree maintains balance.

---

### Heaps

The Heap portion examines how the same values behave in a heap-based structure.

Topics include:

- Complete binary trees
- Heap ordering
- Insertion
- Percolation
- Root removal
- Reorganization after deletion
- Maintaining the heap property

The assignment helps illustrate an important distinction:

> A Binary Search Tree organizes values according to relationships between left and right children, while a Heap organizes values according to priority and the heap property.

---

# Major Data Structures Covered

| Data Structure / Concept | Topics Practiced |
|---|---|
| Linked Lists | Nodes, references, insertion, traversal |
| Binary Search Trees | Search, insertion, removal, inorder successor |
| AVL Trees | Balance factors, rotations, self-balancing |
| Heaps | Priority ordering, insertion, deletion, percolation |
| NumPy Arrays | Indexing, slicing, reshaping, sorting, axes |
| Python Classes | Constructors, methods, inheritance |
| Recursive Structures | Recursive traversal, insertion, and searching |

---

# Python Concepts Practiced

Throughout the repository, the coursework reinforces core Python programming skills.

### Object-Oriented Programming

```text
Classes
Objects
Constructors
Inheritance
Method overriding
Operator overloading
```

### Data Manipulation

```text
Lists
Arrays
NumPy arrays
Indexing
Slicing
Sorting
Searching
Reshaping
```

### Algorithms

```text
Recursion
Tree traversal
BST search
BST insertion
BST deletion
AVL balancing
Heap operations
Boolean indexing
```

### Program Design

```text
File input
Command parsing
Data-driven behavior
Testing
Visualization
Debugging
Incremental implementation
```

---

# NumPy Skills

Later coursework expands beyond traditional data structures into numerical and multidimensional data processing.

Examples include:

```python
a.ndim
a.shape
a.dtype

a[0]
a[-1]
a[1:4]
a[::2]

a.reshape(2, 2)
a.copy()
a.view()

np.concatenate(...)
np.stack(...)
np.where(...)
np.sort(...)
np.average(...)
```

Understanding these operations is useful for future coursework in:

- Data science
- Machine learning
- Numerical computing
- Engineering analysis
- Scientific programming

---

# Tree Concepts

Tree-based assignments make up an important part of the repository.

## Binary Search Tree

A BST maintains the relationship:

```text
left subtree < node < right subtree
```

This makes structured searching, insertion, and deletion possible.

---

## AVL Tree

An AVL tree extends a BST by maintaining a balanced tree after operations.

Typical rotations include:

```text
LL → Right Rotation
RR → Left Rotation
LR → Left Rotation + Right Rotation
RL → Right Rotation + Left Rotation
```

Balancing prevents the tree from becoming excessively skewed.

---

## Heap

A heap is a complete binary tree commonly used to implement priority queues.

Depending on the implementation, the structure maintains either:

```text
Min Heap:
parent <= children
```

or:

```text
Max Heap:
parent >= children
```

Unlike a BST, a heap does not completely sort its left and right subtrees.

---

# Tools and Technologies

## Languages

- Python

## Libraries

- NumPy
- Turtle

## Development Environments

- Jupyter Notebook
- Google Colab
- Visual Studio Code
- Python Tutor

## Version Control

- Git
- GitHub

---

# Running the Coursework

Clone the repository:

```bash
git clone https://github.com/jfmedina05/Data-Structures.git
cd Data-Structures
```

Python scripts can generally be executed with:

```bash
python filename.py
```

Jupyter Notebook files can be opened using:

```bash
jupyter notebook
```

or uploaded to **Google Colab**.

---

# Learning Objectives

Through this repository, I am developing the ability to:

- Implement fundamental data structures from scratch
- Understand relationships between nodes and references
- Apply recursion to structured problems
- Analyze how tree structures change during insertion and deletion
- Understand and implement self-balancing trees
- Work with heap-based priority structures
- Use NumPy for multidimensional numerical data
- Apply indexing and slicing effectively
- Trace algorithms step-by-step
- Compare different approaches to organizing data
- Write clearer and more maintainable Python
- Strengthen algorithmic problem-solving skills

---

# Why Data Structures Matter

Choosing the correct data structure can significantly affect the clarity, efficiency, and performance of a program.

Different structures are designed for different problems:

```text
Linked List → dynamic sequential data

BST → ordered searching and updates

AVL Tree → balanced searching and updates

Heap → priority-based access

NumPy Array → efficient numerical and multidimensional data
```

Understanding how these structures work internally makes it easier to select the appropriate tool for larger software, data, machine-learning, and engineering problems.

---

# Repository Status

This repository is **actively being updated throughout Fall 2026** as additional A310 labs, homework assignments, and exercises are completed.

Future work will continue expanding the repository's coverage of data structures, algorithms, and data-oriented problem solving.

---

# Author

**Jaiden Medina**

B.S. Computer Engineering  
Indiana University Bloomington

Accelerated M.S. Intelligent Systems Engineering  
Indiana University

### Links

- GitHub: [jfmedina05](https://github.com/jfmedina05)
- LinkedIn: [Jaiden Medina](https://www.linkedin.com/in/jaiden-medina/)
- Portfolio: [jaidenmedina.com](https://www.jaidenmedina.com/)

---

## Academic Note

This repository documents coursework and personal learning from Indiana University.

The material is provided as a portfolio of my work and learning progression. Current students should complete course assignments independently and follow Indiana University's academic integrity policies.
