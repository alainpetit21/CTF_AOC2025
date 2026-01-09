from ChallengeD9C1 import ChallengeD9C1


def main():
    chall = ChallengeD9C1("./data/input.txt")
    chall.interpret_data()

    print(chall.run())


if __name__ == '__main__':
    main()
