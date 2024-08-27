"""
Implementation of a Hash Table from scratch in Python
"""
class HashTable:
    def __init__(self, size):
        """Initialise the hash table with a given size"""
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_elements = 0

    def hash(self, key):
        """Compute the hash of a key"""
        return hash(key) % self.size

    def resize(self):
        """Double the size of the hash table and rehash all elements"""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.num_elements = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table"""

        #  Resize the table if the number of elements is greater than or equal to the size
        if self.num_elements >= self.size:
            self.resize()
        
        # Compute the index of the key
        index = self.hash(key)

        # Check if the key already exists in the table
        for kv_pair in self.table[index]:
            if kv_pair[0] == key:
                kv_pair[1] = value
                return
        
        # Insert the key-value pair
        self.table[index].append([key, value])
        self.num_elements += 1
    
    def delete(self, key):
        """Delete a key-value pair from the hash table"""
        index = self.hash(key)

        for i, kv_pair in enumerate(self.table[index]):
            if kv_pair[0] == key:
                self.table[index].pop(i)
                self.num_elements -= 1
                return
            
        return False # Key not found
        