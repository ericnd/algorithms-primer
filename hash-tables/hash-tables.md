## Hash Tables

A commonly desired abstraction in computer science and the real world is the ability to map a type of data to another. 
In other words, mapping keys to values.

Examples of this include:
words -> definitions
student_id -> names
people -> favourite fruits


An association array is an abstract data type that stores key value pairs where keys are unique.
It supports the following operations

When Unsorted:
Insert: Inserting a key-value pair     O(n)
Lookup: Accessing a value given a key  O(n)
Deletion: Deleting a key-value pair    O(n)

When Sorted:
Insert: Inserting a key-value pair     O(n)
Lookup: Accessing a value given a key  O(log n)
Deletion: Deleting a key-value pair    O(n)

In comparison here's the following operations within a Balanced Binary Search Tree:
Insert: Inserting a node               O(log n)
Lookup: Accessing a node               O(log n)
Deletion: Deleting a node              O(log n)

Hash Tables are a data structure that uses an associative array in combination with a hashing function.
It uses the array to store the key-value pair and a hash function to determine the index to insert the key-value pair into.
A good hashtable should have an average O(1) time complexity for the operations of insertion, lookup and delete.


In this example, the key is a word and the value is the definition

```
Key = "Food"
Hash = h(Key)
Value = "Something Edible"

Arr[h(Key)] = "Something Edible"
```

They aren't perfect though, hashing collisions can occur

## Hash Collisions

A hash collision can occur when two keys x and y are not equal but their hashing function outputs are.
```
Example:
x != y
h(x) == h(y)
```

