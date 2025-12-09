from typing import List, Tuple, Set

from engine.Challenge import Challenge


class ChallengeDay7C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0

    def load_data(self, name_input: str = None) -> List[List[str]]:
        with open(name_input, "r") as file:
            self.data = [list(r) for r in file.readlines()]

            return self.data

    def interpret_data(self, data_inj: List[str] = None):
        return self.data

    def run(self):

        return self.result
