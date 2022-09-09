class Hash:
    def __init__(self):
        self.hash_table = []

    def hash_function(self, value):
        hash_code = 0
        for char in value:
            hash_code += ord(char)
        return hash_code % 10

    def insert(self, value):
        try:
            index = self.hash_function(value)
            self.hash_table.insert(index, value)
        except TypeError:
            print("invalid type, inform a str value")

if __name__ == "__main__":
    obj = Hash()
