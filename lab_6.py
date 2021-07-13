import numpy
# Код к заданию
def LAB_7_VAR_4(x):
    yy = numpy.tan(2*(x - numpy.pi/2))
    threshold = 10000
    yy[yy>threshold] = numpy.inf
    yy[yy<-threshold] = numpy.inf
    ax.plot(x, yy, linewidth=1.2, color="black")

#test 1
def TEST1_LAB_7_VAR_4():
    success_result = [0,4,6,8]
    result = LAB_7_VAR_4([4,8,6,0])
    
    print ('test_1...')
    
    if success_result != result:
        print('Тест не успешен')
        print('Ожидаемый результат:', success_result)
        print('Полученный результат:', result, '\n')
        return False
    else:
        print('Тест успешен')
        print('Ожидаемый результат:', success_result)
        print('Полученный результат:', result, '\n')
        return True
        
#test 2
def TEST2_LAB_7_VAR_4():
    success_result = [2,7,16,32,68]
    result = LAB_7_VAR_4([7,2,16,68,32])
    
    print ('test_2...')
    if success_result != result:
        print('Тест не успешен')
        print('ожидаемый результат:', success_result)
        print('полученный результат:', result, '\n')
        return False
    else:
        print('Тест успешен')
        print('ожидаемый результат:', success_result)
        print('полученный результат:', result, '\n')
        return True

#test 3        
def TEST3_LAB_7_VAR_4():
    success_result = [2.2, 8.5, 14.89, 65.34, 76.4]
    result = LAB_7_VAR_4([76.4, 8.5, 2.2, 14.89, 65.34])
    
    print ('test_3...')
    
    if success_result != result:
        print('Тест не успешен')
        print('ожидаемый результат:', success_result)
        print('полученный результат:', result, '\n')
        return False
    else:
        print('Тест успешен')
        print('ожидаемый результат:', success_result)
        print('полученный результат:', result, '\n')
        return True

#program
print('Lab 6\r\n')

k = 0
x = [];
while k < 100:
    x.append(float(k/100.))
LAB_7_VAR_4(x)

print('Программа работает успешно')