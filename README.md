
# Data Structures & Algorithms | Python

### Indiana University Bloomington — A310: Problem Solving with Data

A collection of Python programming exercises, coursework, and implementations developed while studying data structures and algorithms at Indiana University Bloomington.

This repository documents my progress in understanding how data structures work, implementing algorithms, and applying computational problem-solving techniques. The focus is on building a strong foundation in Python, object-oriented programming, recursion, and efficient data organization.

---

## Overview

Data structures and algorithms are fundamental to software engineering because they determine how information is organized, accessed, and manipulated.

Through this coursework, I am developing a deeper understanding of the internal behavior of data structures, the algorithms used to operate on them, and the tradeoffs involved in different implementations.

The repository is intended to serve as both an academic record and a reference for future software engineering and technical projects.

### Learning Objectives

- Implement and understand fundamental data structures.
- Develop proficiency in Python programming.
- Apply object-oriented programming principles.
- Understand references, nodes, and linked structures.
- Practice recursion and algorithmic thinking.
- Improve debugging and code-tracing skills.
- Analyze the efficiency of different computational approaches.
- Strengthen technical problem-solving skills.

---

## Repository Structure

The repository is organized by coursework and weekly assignments.

```text
Data-Structures/
│
├── Week 01/
│   └── Introductory Python exercises
│       and programming assignments
│
└── README.md
```

Additional coursework will be documented as the repository expands.

---

## Coursework

### Week 01 — Python Fundamentals & Linked Structures

The introductory coursework focuses on reviewing Python programming fundamentals and understanding how objects can be used to construct linked data structures.

**Topics explored:**

- Python classes and objects
- Constructors and instance attributes
- Object references
- Nodes and linked structures
- Recursive operations
- Traversal of connected objects
- File input and processing
- Data-driven programming
- Python Turtle graphics

#### Linked Structures

The linked-structure exercises introduce the concept of connecting objects through references.

Rather than storing all elements in a contiguous array, linked structures organize information using individual nodes that reference other nodes.

Key concepts include:

- Creating nodes using Python classes
- Connecting nodes through object references
- Traversing linked objects
- Understanding recursive insertion
- Visualizing relationships between objects in memory

These concepts provide a foundation for implementing linked lists, trees, and other dynamic data structures.

#### File-Driven Turtle Graphics

The Turtle Drawing exercise explores how a Python program can interpret instructions stored in an external file and translate them into graphical commands.

The exercise introduces operations such as:

- `goto()`
- `circle()`
- `begin_fill()`
- `end_fill()`
- `penup()`
- `pendown()`

This activity demonstrates the relationship between program logic, external data, and graphical output.

It also reinforces file handling, command interpretation, and sequential execution.

**Coursework:** [Explore Week 01](./Week%2001)

---

## Data Structures & Algorithms

The coursework develops foundational knowledge in the following areas.

| Concept | Description |
|---------|-------------|
| Python Classes | Creating reusable objects with attributes and methods |
| Linked Structures | Connecting nodes through references |
| Recursion | Solving problems through smaller instances of the same problem |
| Traversal | Visiting and processing elements in a connected structure |
| File Processing | Reading external data and interpreting instructions |
| Algorithm Design | Developing step-by-step computational solutions |
| Object-Oriented Programming | Organizing programs using classes, objects, and methods |

### Linked Data Structure Example

A basic node can be represented in Python as follows:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
first = Node(10)
second = Node(20)
third = Node(30)

# Connect nodes
first.next = second
second.next = third

# Traverse linked structure
current = first

while current is not None:
    print(current.data)
    current = current.next
```

**Output:**

```text
10
20
30
```

This example illustrates how individual objects can be connected to form a linked data structure and traversed without relying on array indexing.

---

## Technical Skills

### Programming Languages
- Python

### Programming Concepts
- Object-Oriented Programming
- Classes and Objects
- Recursive Functions
- Data Structures
- Algorithmic Problem Solving
- File Input/Output
- Debugging and Code Tracing

### Tools & Development Environments
- Python 3
- Jupyter Notebook
- Google Colab
- Visual Studio Code
- Git & GitHub
- Python Tutor

---

## Getting Started

### Prerequisites

Install Python 3 from the [official Python website](https://www.python.org/downloads/).

Depending on the assignment, you may also use Jupyter Notebook or Google Colab.

### Clone the Repository

```bash
git clone https://github.com/jfmedina05/Data-Structures.git
```

Navigate into the repository:

```bash
cd Data-Structures
```

### Explore the Coursework

Open the appropriate weekly directory and locate the assignment you want to examine.

For Python scripts, run:

```bash
python filename.py
```

For Jupyter Notebook files, open them in Jupyter Notebook, Visual Studio Code, or Google Colab.

Some exercises may require additional input files or a graphical environment, such as those using Python Turtle.

---

## Academic Context

**Course:** A310 — Problem Solving with Data  
**Institution:** Indiana University Bloomington  
**School:** Luddy School of Informatics, Computing, and Engineering  
**Language:** Python  
**Academic Term:** Fall 2026

This repository contains coursework and programming exercises completed as part of my undergraduate Computer Engineering studies.

The goal is to connect theoretical computer science concepts with practical implementation and strengthen my understanding of computational problem solving.

---

## Future Development

As I progress through the course, I plan to expand the repository with additional coursework and implementations involving:

- Linked lists and recursive algorithms
- Binary Search Trees
- AVL Trees and tree rotations
- Heaps and priority queues
- Searching and sorting algorithms
- Numerical computing with NumPy
- Algorithm analysis and computational complexity

These topics will be documented as new assignments and implementations are added.

---

## Author

**Jaiden Medina**  
B.S. Computer Engineering | Indiana University Bloomington  
Accelerated M.S. Intelligent Systems Engineering | Indiana University

- **GitHub:** [jfmedina05](https://github.com/jfmedina05)
- **LinkedIn:** [Jaiden Medina](https://www.linkedin.com/in/jaiden-medina/)
- **Portfolio:** [jaidenmedina.com](https://www.jaidenmedina.com/)

---

## Academic Integrity

This repository is intended to document my academic progress and programming experience.

All materials are shared for educational and portfolio purposes. Students referencing this repository should follow their institution's academic integrity policies and complete their own coursework independently.
