from D7C1.src.ChallengeDay7C1 import ChallengeDay7C1


def test_loading():
    chall = ChallengeDay7C1("./data/example.txt")

    assert chall.data[0][0] == '.'
    assert chall.data[1][0] == '.'


def test_interpret_data():
    chall = ChallengeDay7C1("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay7C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 21


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
