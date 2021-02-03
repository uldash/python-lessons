import first
import time


if __name__ == "__main__":
    start_time = time.time()
    print(first.main(100000000))
    print("------ %s seconds ------" % (time.time()-start_time))
