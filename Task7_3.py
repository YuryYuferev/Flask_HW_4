# Напишите программу на Python, которая будет находить сумму элементов массива из 1000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100. Нужно вывести время выполнения вычислений.
# При решении задачи нужно использовать асинхронность.

import asyncio
import random
import time

async def calculate_sum(arr):
    return sum(arr)

async def main():
    arr = [random.randint(1, 100) for _ in range(1000)]
    start_time = time.time()
    result = await calculate_sum(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Сумма элементов массива: {result}")
    print(f"Время выполнения: {execution_time} секунд")

if __name__ == "__main__":
    asyncio.run(main())
