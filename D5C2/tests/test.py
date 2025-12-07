from D5C2.src.ChallengeDay5C2 import ChallengeDay5C2


def test_loading():
    chall = ChallengeDay5C2("./data/example.txt")

    assert chall.data[0][0] == '3'
    assert chall.data[1][0] == '1'


def test_interpret_data():
    chall = ChallengeDay5C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay5C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 14


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
