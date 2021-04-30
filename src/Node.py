class Node:
    def __init__(self, data, info, next=None):
        self.data = data
        self.info = info
        self.next = next

    def __str__(self):
        return str(self.data)