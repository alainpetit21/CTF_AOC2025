from engine.Challenge import Challenge


class ChallengeDay2C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.invalid_ids = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)
        self.ranges = [r.split('-') for r in self.data[0].split(',')]


    def is_pattern_invalid(self, number:str) -> bool:
        len_str_num = len(number)
        if len_str_num % 2:
            return False

        left = number[0:len_str_num//2]
        right = number[len_str_num//2:]

        if left == right:
            print(f"Found one invalid {left}")
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
