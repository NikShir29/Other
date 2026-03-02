L_pl = 100
L_train = 150
V_human = 1
V_train = 10

def task():
    print("=" * 50)
    print("РЕШЕНИЕ ЗАДАЧИ 1.1 ПО ФИЗИКЕ")
    print("=" * 50)
    print("ДАНО:")
    print(f"Длина платформы: {L_pl}м")
    print(f"Длина поезда: {L_train}м")
    print(f"Скорость человека: {V_human}м/с")
    print(f"Скорость поезда: {V_train}м/с")
    print("Человек и поезд движутся навстречу друг другу.")
    print("=" * 50)
    print("СИСТЕМА ОТСЧЕТА 'ЗЕМЛЯ':")
    t_earth = L_train / V_train
    print(f"Время прохождения = {L_train} / {V_train} = {t_earth} с.")
    print()
    print("СИСТЕМА ОТСЧЕТА 'ЧЕЛОВЕК':")
    v_rel = V_human + V_train
    print(f"Относительная скорость = {V_human} + {V_train} = {v_rel}м/с.")
    t_travel = L_train / v_rel
    print(f"Время прохождения = {L_train} / {v_rel} = {round(t_travel, 2)} с.")
    print("=" * 50)
    print("ПРОВЕРКА ПРИНЦИПА ОТНОСИТЕЛЬНОСТИ:")
    t_diff = t_earth - t_travel
    print(f"Время в разных СО разное: {t_earth} с. != {round(t_travel, 2)} с."
          "\nЭто нормально! Время зависит от выбора системы отсчета."
          f"\nРазница: {round(t_diff, 2)} с.")
    print("=" * 50)

task()