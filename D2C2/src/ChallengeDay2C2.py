from engine.Challenge import Challenge


class ChallengeDay2C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.invalid_ids = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)
        self.ranges = [r.split('-') for r in self.data[0].split(',')]


    def is_pattern_invalid(self, number:str) -> bool:
        len_greatest_pattern = len(number)//2

        #try all pattern lenght from 1 to len_greatest_pattern
        for size in range(1, len_greatest_pattern+1):
            parts = [number[i:i+size] for i in range(0, len(number), size)]
            set_parts = set(parts)

            if len(set_parts) == 1:
                print(f"Found pattern {set_parts.pop()} in {number}")
                return True

        return False

    def run(self):

        for r in self.ranges:
            start, finish = int(r[0]), int(r[1])
            for i in range(start, finish + 1):
                if self.is_pattern_invalid(str(i)):
                    self.invalid_ids.append(i)


        self.result = sum(self.invalid_ids)
        return self.result
