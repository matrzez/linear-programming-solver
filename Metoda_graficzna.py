import matplotlib.pyplot as plt
import numpy as np

# Dane z tabeli
points = {
    1: [(5, 0), (0, 20)],
    2: [(15, 0), (0, 5)],
    3: [(10, 0), (0, 10)],
    4: [(10, 0), (0, 6)]
}

# Równanie prostej
def line_equation(x):
    return -4 * x + 20


# Tworzenie wykresu
plt.figure()


# Zaznaczenie obszaru dopuszczalnego
x = np.linspace(0, 15, 400)
y1 = (9 - 0.6*x) / 1.8
y2 = (4 - 0.4*x) / 0.4
y3 = (5 - 1 * x) / 0.25

# Współrzędne wektora gradientu
gradient = [5, 7]

# Współrzędne punktu A
A = (7.5, 2.5)

# Rysowanie prostych
for i, (p1, p2) in points.items():
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], label=f'Warunek {i}')

plt.quiver(0, 0, gradient[0], gradient[1], angles='xy', scale_units='xy', scale=1, color='darkblue', label='Gradient funkcji g')
plt.scatter(*A, color='red', label='Punkt A')

# Zaznaczenie obszaru dopuszczalnego
plt.fill_between(x, np.maximum(np.maximum(y1, y2),y3), 20, color='purple', alpha=0.3, label='Zbiór dopuszczalny')

plt.xlabel('y1')
plt.ylabel('y2')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xticks(np.arange(0, 16, 2.5))
plt.yticks(np.arange(0, 21, 2.5))
plt.show()