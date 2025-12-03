from D1C2.src.ChallengeDay1C2 import ChallengeDay1C2


def test_loading():
    chall = ChallengeDay1C2("./data/example.txt")

    assert chall.data[0][0] == 'L'
    assert chall.data[0][1] == '6'
    assert chall.data[1][0] == 'L'
    assert chall.data[1][1] == '3'


def test_interpret_data():
    chall = ChallengeDay1C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay1C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 6


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
