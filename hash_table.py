class Hash:
    def __init__(self):
        self.safe = []

    def hash_function(self, value):
        hash_code = 0
        for char in value:
            hash_code += ord(char)
        return hash_code % 10

if __name__ == "__main__":
    obj = Hash()
    print("{}".format(obj.hash_function("Bob")))
