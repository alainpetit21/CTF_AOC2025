
class JunctionBox:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.connect_to = set()

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return (
                isinstance(other, JunctionBox)
                and self.x == other.x
                and self.y == other.y
                and self.z == other.z
        )

    def __repr__(self):
        return f"JB {self.id}"
