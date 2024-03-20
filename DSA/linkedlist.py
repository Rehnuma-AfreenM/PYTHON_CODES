class node:
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

n1 = node(10)    
print(n1)