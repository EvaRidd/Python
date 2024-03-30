import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import perf_counter
import random
# Var3!
# Задание 1 (сравнение перемножения стандартных списков и массивов numpy)
list1 = [random.randint(1, 99) for i in range(1000000)] # миллион случайных чисел от 1 до 99
list2 = [random.randint(1, 99) for i in range(1000000)]

array1 = np.random.randint(1, 99, 1000000) # миллион случайных чисел от 1 до 99
array2 = np.random.randint(1, 99, 1000000)

start_time = perf_counter()
result_list = [a * b for a, b in zip(list1, list2)]
end_time = perf_counter()
list_time = end_time - start_time

start_time = perf_counter()
result_array = np.multiply(array1, array2)
end_time = perf_counter()
array_time = end_time - start_time

print("list time: ", list_time)
print("NumPy array time: ", array_time)
print("массивы NumPy считаются быстрее")

# задание 2 (графики 1 от 4 и 1 от 18)
def tableLoad():
    arr = np.genfromtxt('data1.csv', delimiter=';')
    time = arr[:100, 0]
    time = time[:, np.newaxis]
    position = arr[:100, 3]
    position = position[:, np.newaxis]
    cons = arr[:100, 17]
    cons = cons[:, np.newaxis]

    plt.plot(time, position * 50, 'b', time, cons, 'r')
    plt.show()

    # График корреляции между положением дроссельной заслонки(%) и расходом топлива:
    correlation = np.corrcoef(position.flatten(), cons.flatten())[0, 1]
    plt.scatter(position, cons)
    plt.xlabel('position * 50')
    plt.ylabel('Fuel Consumption')
    plt.title('График корреляции')
    plt.show()
if __name__ == '__main__':
    tableLoad()
# задание 3(трёхмерный график по формуле x∈(-5п;5п); y=cos(x); z=sin(x))
xs = np.linspace(-5*np.pi, 5*np.pi)
ys = np.cos(xs)
zs = np.sin(xs)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, marker='x', c='red')

ax.set_xlabel('x')
ax.set_ylabel('cos(X)')
ax.set_zlabel('sin(X)')

plt.show()