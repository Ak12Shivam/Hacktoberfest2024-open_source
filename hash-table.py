class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hash_index].append([key, value])

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def delete(self, key):
        hash_index = self._hash_function(key)
        for i, item in enumerate(self.table[hash_index]):
            if item[0] == key:
                del self.table[hash_index][i]
                return
        raise KeyError(key)

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

def main():
    ht = HashTable()
    
    while True:
        print("\n1. Insert\n2. Get\n3. Delete\n4. Display\n5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            ht.insert(key, value)
            print("Inserted successfully!")
        elif choice == '2':
            key = input("Enter key to retrieve: ")
            try:
                print(f"Value: {ht.get(key)}")
            except KeyError:
                print("Key not found!")
        elif choice == '3':
            key = input("Enter key to delete: ")
            try:
                ht.delete(key)
                print("Deleted successfully!")
            except KeyError:
                print("Key not found!")
        elif choice == '4':
            ht.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
