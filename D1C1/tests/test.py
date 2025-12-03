from D1C1.src.ChallengeDay1C1 import ChallengeDay1C1


def test_loading():
    chall = ChallengeDay1C1("./data/example.txt")

    assert chall.data[0][0] == 'L'
    assert chall.data[0][1] == '6'
    assert chall.data[1][0] == 'L'
    assert chall.data[1][1] == '3'


def test_interpret_data():
    chall = ChallengeDay1C1("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay1C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 3


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
