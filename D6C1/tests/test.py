from D6C1.src.ChallengeDay6C1 import ChallengeDay6C1


def test_loading():
    chall = ChallengeDay6C1("./data/example.txt")

    assert chall.data[0][0] == '1'
    assert chall.data[1][0] == '4'


def test_interpret_data():
    chall = ChallengeDay6C1("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay6C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 4277556


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
