from octagon_insider import OctagonInsider
import time


def main():
    while True:
        _ = OctagonInsider()
        time.sleep(60 * 60)


if __name__ == "__main__":
    main()
