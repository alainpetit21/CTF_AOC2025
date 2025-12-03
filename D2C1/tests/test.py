from D2C1.src.ChallengeDay2C1 import ChallengeDay2C1


def test_loading():
    chall = ChallengeDay2C1("./data/example.txt")

    assert chall.data[0][0] == '1'
    assert chall.data[0][1] == '1'


def test_interpret_data():
    chall = ChallengeDay2C1("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay2C1("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 1227775554


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
