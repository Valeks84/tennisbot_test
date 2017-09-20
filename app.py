import time

def main():

    n = 0
    while True:
        print("Helloe ", n)
        n += 1
        time.sleep(5)
        if n == 3: break


if __name__ == '__main__':
    main()
