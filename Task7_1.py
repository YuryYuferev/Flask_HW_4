# Напишите программу на Python, которая будет находить сумму элементов массива из 1000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100. Нужно вывести время выполнения вычислений.
# При решении задачи нужно использовать многопоточность.

import random
import threading
import time

# Функция для вычисления суммы элементов массива в отдельном потоке
def calculate_sum(arr, start, end, result):
    partial_sum = sum(arr[start:end])  # Вычисляем сумму элементов в диапазоне
    result.append(partial_sum)  # Добавляем результат в общий список

if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(1000)]  # Создаем массив из 1000 случайных чисел

    num_threads = 4  # Количество потоков

    chunk_size = len(arr) // num_threads  # Размер части массива для каждого потока

    start_time = time.time()  # Засекаем начальное время

    threads = []
    results = []

    # Создаем и запускаем потоки
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(arr)
        thread = threading.Thread(target=calculate_sum, args=(arr, start, end, results))
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    total_sum = sum(results)  # Суммируем все частичные суммы

    end_time = time.time()  # Засекаем конечное время

    print(f"Сумма элементов массива: {total_sum}")
    print(f"Время выполнения: {end_time - start_time} секунд")

