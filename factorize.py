from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
import time


# декоратор для заміру часу виконання функції
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print(f"Time of execution: {time.time() - t}")
        return res

    return tmp

# функція розрахзунку без мультіпроцессінгу
@timer
def factorize(*number: int):
    res = []
    for num in number:
        time.sleep(0.3)
        res_list = [i for i in range(1, (num + 1)) if not (num % i)]
        res.append(res_list)

    return res

# функція розрахзунку з мультіпроцессінгом
def calculate(num):

        time.sleep(0.3)
        return [i for i in range(1, (num + 1)) if not (num % i)]


@timer
def factorize_multi(*number: int):
    with ThreadPoolExecutor(max_workers=cpu_count()) as executer:
        return executer.map(calculate, number)


# тести

print("*" * 50)
print("Function execution without multiprocessing")

a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
             1521580, 2130212, 2662765, 5325530, 10651060]

print("*" * 50)
print("Function execution with multiprocessing")

a, b, c, d = factorize_multi(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
             1521580, 2130212, 2662765, 5325530, 10651060]



