import numpy as np
import matplotlib.pyplot as plt

# Код к заданию
def LAB_7_VAR_4(x0,x1,count):
    # функция tan
    y_tan = lambda x: np.tan(x)
    # функция cotan
    y_cotan = lambda x: (1/np.tan(x))
    # создаём рисунок с координатную плоскость
    plt.subplots()
    # создаём область, в которой будет
    # - отображаться график
    x = np.linspace(x0,x1,count)
    # значения x, которые будут отображены
    # количество элементов в созданном массиве
    # - качество прорисовки графика 
    # рисуем график тангенса
    plt.plot(x, y_tan(x))
    # показываем график
    plt.show()
    # рисуем график котангенса
    plt.plot(x, y_cotan(x))
    # показываем график
    plt.show()

#program
print('Lab 7\r\n')
LAB_7_VAR_4(-3.13, 3.13, 100)