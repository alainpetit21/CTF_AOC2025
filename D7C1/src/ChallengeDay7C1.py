from typing import List, Tuple, Set

from engine.Challenge import Challenge


class ChallengeDay7C1(Challenge):
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
        cpt_split = 0

        for y in range(len(self.data) -1):

            row = self.data[y]
            for x in range(len(row)):
                c = row[x]

                # If found a S, put a | underneath
                if c == 'S':
                    self.data[y+1][x]= '|'

                #If you find a |, check next row for a possible splitter
                elif c == '|':
                    if self.data[y+1][x] == '^':
                        self.data[y + 1][x-1]= '|'
                        self.data[y + 1][x+1]= '|'
                        cpt_split+= 1
                    elif self.data[y+1][x] == '.':
                        self.data[y + 1][x]= '|'

        self.result = cpt_split
        return self.result
