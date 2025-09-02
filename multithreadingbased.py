import threading
import time


def addition(x, y):
    time.sleep(5)
    result = x + y
    print(result)


def multiplication(x, y):
    time.sleep(5)
    result = x * y
    print(result)


def subtraction(x, y):
    time.sleep(5)
    result = x - y
    print(result)


def division(x, y):
    time.sleep(5)
    if y == 0:
        print("Division by zero not allowed")
    else:
        print(x / y)


def main():
    thread1 = threading.Thread(target=addition, args=(500, 300))
    thread2 = threading.Thread(target=multiplication, args=(500, 300))
    thread3 = threading.Thread(target=subtraction, args=(500, 300))
    thread4 = threading.Thread(target=division, args=(500, 300))

    start_time = time.time()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f'the total time taken to complete all the task is {total_time}')


if __name__ == "__main__":
    main()



