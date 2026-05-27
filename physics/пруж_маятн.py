import math

print("=" * 50)
print("Задача 1. Пружинный маятник")
print("=" * 50)


m = 0.2
k = 50.0
A = 0.05


T = 2 * math.pi * math.sqrt(m / k)

nu = 1 / T

omega = math.sqrt(k / m)

E_max = (k * A ** 2) / 2

E_kin_max = E_max
E_pot_max = E_max

print("\nДано:")
print(f"  m = {m} кг")
print(f"  k = {k} Н/м")
print(f"  A = {A} м")
print("\nНайти: T, ν, ω, E_kin_max, E_pot_max\n")

print("Решение:")
print(f"  1) Период T = 2π·√(m/k) = 2·3.1416·√({m}/{k}) ≈ {T:.4f} с")
print(f"  2) Частота ν = 1/T = {nu:.4f} Гц")
print(f"  3) Циклическая частота ω = √(k/m) = √({k}/{m}) ≈ {omega:.4f} рад/с")
print(f"  4) Максимальная энергия: E_max = k·A²/2 = {k}·({A})²/2 = {E_max:.6f} Дж")
print(f"     → E_kin_max = {E_kin_max:.6f} Дж")
print(f"     → E_pot_max = {E_pot_max:.6f} Дж")



print("\n" + "=" * 50)
print("Задача 2. Математический маятник")
print("=" * 50)

L1 = 1.0
g = 9.81

T1 = 2 * math.pi * math.sqrt(L1 / g)

print("\nЧасть А. Расчёт периода для заданного маятника:")
print(f"Дано: L = {L1} м, g = {g} м/с²")
print(f"Найти: период T")
print(f"\nT = 2π·√(L/g) = 2·3.1416·√({L1}/{g}) ≈ {T1:.4f} с\n")

T_measured = 2.0
L_measured = 0.99

g_calc = (4 * math.pi ** 2 * L_measured) / (T_measured ** 2)

print("Часть Б. Определение ускорения свободного падения по эксперименту:")
print(f"Дано: T_измер = {T_measured} с, L_измер = {L_measured} м")
print(f"Найти: g")
print(f"\nФормула: T = 2π·√(L/g)  →  g = 4π²·L / T²")
print(f"g = (4·π²·{L_measured}) / ({T_measured})² = {g_calc:.4f} м/с²")
print(f"(Теоретическое значение g = {g:.2f} м/с²)")