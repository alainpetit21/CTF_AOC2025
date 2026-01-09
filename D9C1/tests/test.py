from D9C1.src.ChallengeD9C1 import ChallengeD9C1


def test_loading():
    chall = ChallengeD9C1("./data/example.txt")

    assert chall.data[0][0] == '7'
    assert chall.data[1][0] == '1'


def test_interpret_data():
    chall = ChallengeD9C1("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeD9C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 50


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
