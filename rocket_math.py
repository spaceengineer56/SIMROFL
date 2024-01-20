import math
import matplotlib.pyplot as h_t
import matplotlib.pyplot as v_t

h_list = list()
flag = True
time_1 = 0
s_rocket = 0
s_list = list()
tick = 0
x_list = list()
flag_up = True
v_list = list()
p_engine = float(input("Полный импульс ТТРД: "))
m_rocket = float(input("Масса ракеты, кг: "))
p_engine = 129.5
v_rocket = p_engine / m_rocket
print("max скорость:", v_rocket, "м/с")
h_rocket = (v_rocket ** 2) / (2 * 9.81)
print("Апогей:", h_rocket, "м")
t_rocket = math.sqrt(2 * h_rocket / 9.81)
print("Время до апогея: ", t_rocket, "с")
v = -v_rocket
while flag:
    tick += 0.1
    if s_rocket < h_rocket and flag_up:
        s_bit_up = 0.1 * v_rocket
        s_rocket += s_bit_up
        s_list.append(s_rocket)
        v_rocket -= 0.981
    else:
        if s_rocket < 0:
            flag = False
        flag_up = False
        s_bit_up = 0.1 * v_rocket
        s_rocket += s_bit_up
        s_list.append(s_rocket)
        v_rocket = -5
    x_list.append(tick)
    v_list.append(v_rocket)
print("Общее время:", tick / 60, "мин")
h_t.title('Высота от времени')
h_t.plot(x_list, s_list)
h_t.show()
h_t.title('Скорость от времени')
v_t.plot(x_list, v_list)
v_t.show()