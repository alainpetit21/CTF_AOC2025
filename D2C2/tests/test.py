from D2C2.src.ChallengeDay2C2 import ChallengeDay2C2


def test_loading():
    chall = ChallengeDay2C2("./data/example.txt")

    assert chall.data[0][0] == '1'
    assert chall.data[0][1] == '1'


def test_interpret_data():
    chall = ChallengeDay2C2("./data/example.txt")
    chall.interpret_data()


def test_result():
    chall = ChallengeDay2C2("./data/example.txt")
    chall.interpret_data()

    chall.run()
    assert chall.result == 4174379265


if __name__ == '__main__':
    test_loading()
    test_interpret_data()
    test_result()

    print("Passed all tests")
