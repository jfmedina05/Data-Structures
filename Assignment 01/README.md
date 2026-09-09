# Week 01

This folder contains my coursework, labs, and programming exercises from **Week 01** of Data Structures. The work focuses on reviewing Python fundamentals, introducing linked data structures, and practicing file-driven programming using Python's Turtle graphics library.

## Contents

### Lab 1

The first lab introduces the basic structure and behavior of a **linked list** in Python.

**Files:**

* `Lab 01.py` — Implements a simple linked list using a `LinkedList` class.
* `Python Tutor Visualization.png` — Visualization of the linked list and its references using Python Tutor.

**Concepts practiced:**

* Classes and objects
* Constructors (`__init__`)
* Object references
* Linked nodes
* Recursive insertion
* Traversing linked structures

The program begins with two connected nodes and uses a recursive `insert()` method to append an additional node to the end of the list.

---

### Turtle Drawing

This exercise uses Python's `turtle` module to create a drawing from commands stored in an external text file.

**Files:**

* `Instructions.py` — Reads and interprets drawing commands from a text file.
* `PatrickStar.txt` — Contains the commands used to draw Patrick Star.

The Python program reads the text file line-by-line and converts each command into a corresponding Turtle operation.

Supported commands include:

* `goto`
* `circle`
* `beginfill`
* `endfill`
* `penup`
* `pendown`

This exercise demonstrates how a program can separate **data/instructions** from the code responsible for interpreting them.

## Concepts Covered

Week 01 introduced and reinforced several important programming concepts:

* Python classes and objects
* Linked lists
* References between objects
* Recursion
* File input
* String parsing
* Conditional logic
* Turtle graphics
* Translating stored commands into program behavior

## Folder Structure

```text
Week 01/
│
├── Lab 1/
│   ├── Lab 01.py
│   └── Python Tutor Visualization.png
│
└── Turtle_Drawing/
    ├── Instructions.py
    └── PatrickStar.txt
```

## Running the Programs

### Lab 1

```bash
python "Lab 1/Lab 01.py"
```

### Turtle Drawing

Navigate into the `Turtle_Drawing` directory:

```bash
cd Turtle_Drawing
python Instructions.py
```

When prompted for a filename, enter:

```text
PatrickStar.txt
```

The program will interpret the commands in the file and render the drawing using Python Turtle.

---

This folder will continue to contain any additional assignments, exercises, and in-class work completed during Week 01.
