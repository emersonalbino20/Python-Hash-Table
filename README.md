**This project has been created as part of my journing in python learning by emerson albino**

## Description

This repository contains a simple educational implementation of a Hash Table built from scratch using Python, without relying on dictionaries.

A hash table works by:

1. Receiving a value

2. Passing it through a hash function

3. Transforming it into an index

4. Storing the value at that index inside an internal array

This allows average-case time complexity of:

- O(1) for insertion

- O(1) for lookup

In this implementation:

- The internal structure is a fixed-size list

- The hash function is based on ASCII character summation

- Only string values are supported

## Key Features

### Insert

- Computes the index using the hash function

- Inserts the value at the calculated index

### Contains

- Computes the index for the given value

- Checks if the value stored at that index matches the searched value

- Returns True or False

Includes a doctest example for quick validation.

## Instalation & Setup

### Requirements

Before running this project, make sure you have:

- Python 3.8+ installed

- Git installed (to clone the repository)

### Clone the Repository

Clone the project using Git:

```
git clone https://github.com/emersonalbino20/Python-Hash-Table.git
```

Then navigate into the project folder:

```
cd Python-Hash-Table/
```

### Run Doctests

To validate the **contains** method using doctest:

```
python3 -m doctest hash_table.py -v
```

## Limitations

This implementation is intentionally simple for learning purposes.

It does NOT include:

- Collision handling

- Dynamic resizing

- Load factor management

- Deletion method

Because of that, performance may degrade if collisions occur.

## Relevance

- Understanding hash tables internally helps you:

- Understand how Python dictionaries work

- Analyze algorithmic complexity

- Compare performance against lists

- Prepare for technical interviews

- Build deeper data structure knowledge

This project is part of a broader study comparing:

- Arrays

- Linked Lists

- Hash Tables

## Contribution

This project is educational, but suggestions and improvements are welcome.

If you'd like to:

- Improve the hash function

- Add collision handling

- Implement dynamic resizing

- Optimize performance

Feel free to fork and experiment.

## Resources

- [DigitakOcean](https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3)

- [Big-O Notation](https://youtu.be/BgLTDT03QtU?si=9pyjc6gAXJGXZnUQ)

- [W3School](https://www.w3schools.com/python/python_dsa_hashtables.asp#gsc.tab=0&gsc.q=bubble%20sort%20in%20python)
