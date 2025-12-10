from itertools import combinations
from typing import List, Optional

from D8C1.src.Circuit import Circuit
from D8C1.src.JunctionBox import JunctionBox
from engine.Challenge import Challenge


def dist2(box1, box2):
    # squared distance to avoid sqrt (faster, same order)
    return ((box1.x - box2.x) ** 2 +
            (box1.y - box2.y) ** 2 +
            (box1.z - box2.z) ** 2)


class ChallengeDay8C1(Challenge):
    def __init__(self, nb_connections, filename=None):
        super().__init__(filename)
        self.result = 0
        self.boxes = []
        self.circuits = []
        self.nb_connections = nb_connections


    def interpret_data(self, data_inj: List[str] = None):
        super().interpret_data(self.data)

        for i, row in enumerate(self.data):
            x, y, z = row.split(",")
            self.boxes.append(JunctionBox(i, x, y, z))

    def run(self):
        distances = []  # will store: (distance², index_i, index_j)

        for (i, p), (j, q) in combinations(enumerate(self.boxes), 2):
            d2 = dist2(p, q)
            distances.append((d2, i, j))

        sorted_distances = sorted(distances, key=lambda item: item[0])

        for i in range(self.nb_connections):
            box1_idx = sorted_distances[i][1]
            box2_idx = sorted_distances[i][2]

            box1 = self.boxes[box1_idx]
            box2 = self.boxes[box2_idx]

            #check if already in a circuit
            found = False
            circuits_found= []
            for circuit in self.circuits:
                if box1 in circuit.connections:
                    found = True
                    circuits_found.append(circuit)
                if box2 in circuit.connections:
                    found = True
                    circuits_found.append(circuit)

            if not found:
                circuits_found.append(Circuit())
                self.circuits.append(circuits_found[0])

            # Merge the two circuit
            if len(circuits_found) > 1 and len(set(circuits_found)) > 1:
                merged_circuit = Circuit()

                for circuit in circuits_found:
                    for box in circuit.connections:
                        merged_circuit.connect(box)

                    self.circuits.remove(circuit)

                circuits_found.clear()
                circuits_found.append(merged_circuit)
                self.circuits.append(circuits_found[0])



            circuit = circuits_found[0]
            circuit.connect(box1)
            circuit.connect(box2)


        sorted_circuits = sorted(self.circuits, key=lambda item: item.get_length(), reverse=True)
        circuit1= sorted_circuits[0]
        circuit2= sorted_circuits[1]
        circuit3= sorted_circuits[2]

        size_c1 = circuit1.get_length()
        size_c2 = circuit2.get_length()
        size_c3 = circuit3.get_length()

        self.result = size_c1 * size_c2 * size_c3
        return self.result
