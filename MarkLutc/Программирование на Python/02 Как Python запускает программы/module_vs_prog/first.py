import time


def main(count):
    sum = 0
    for number in range(count):
        sum = +number
    return sum


if __name__ == "__main__":
    start_time = time.time()
    print(main(100000000))
    print("------ %s seconds ------" % (time.time()-start_time))
