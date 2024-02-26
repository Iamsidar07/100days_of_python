import time
from instagram import InstagramBot


def main():
    _ = InstagramBot()
    # run every 4 hour
    time.sleep(60 * 60 * 4)


if __name__ == "__main__":
    main()
