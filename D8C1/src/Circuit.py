
class Circuit:
    def __init__(self):
        self.connections = set()

    def connect(self, box):
        self.connections.add(box)

    def get_length(self):
        return len(self.connections)

    def __repr__(self):
        ret:str="Circuit: "

        for box in self.connections:
            ret+= f"{box};"

        return ret
