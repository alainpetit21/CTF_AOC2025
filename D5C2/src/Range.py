class Range():
    def __init__(self, start_end):
        self.start = start_end[0]
        self.end = start_end[1]

    def is_overlap(self, other):
        if self.start <= other.start <= self.end:
            print(f"Found overlap between {self} and {other}")
            return True

        elif self.start <= other.end <= self.end:
            print(f"Found overlap between {self} and {other}")
            return True

        return False

    def merge(self, other):

        print(f"Merging... {self} ", end="")
        # Merge from the start
        if other.start <= self.start:
            self.start = other.start

        # Merge from the end
        if other.end >= self.end:
            self.end = other.end

        print(f"to -> {self} ")


    def __repr__(self):
        return f"Range({self.start}, {self.end})"