import math

# Код к заданию
def LAB_2_VAR_4(a,b,c):
    'num_min_r - число, находящееся на минимальном расстоянии'
    num_min_r = 0
    'min_r - минимальное расстояние'
    min_r = 0
    avg = float((a+b+c)/3.)
    r_a = math.fabs(avg-a)
    r_b = math.fabs(avg-b)
    if r_a >= r_b:
        min_r = r_b
        num_min_r = b
    else:
        min_r = r_a
        num_min_r = a
    r_c = math.fabs(avg-c)
    if(min_r > r_c):
        min_r = r_c
        num_min_r = c
    
    return(num_min_r)

#test 1
def TEST1_LAB_2_VAR_4():
    success_result = 4.0
    result = LAB_2_VAR_4(4,7,4)
    
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
def TEST2_LAB_2_VAR_4():
    success_result = 7.0
    result = LAB_2_VAR_4(5,10,7)
    
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
def TEST3_LAB_2_VAR_4():
    success_result = 4.3
    result = LAB_2_VAR_4(4.3,2.2,7.5)
    
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
print('Lab 2\r\n')
print('Прогон тестовых сценариев...\r\n')
if TEST1_LAB_2_VAR_4() == False:
    exit()
if TEST2_LAB_2_VAR_4() == False:
    exit()
if TEST3_LAB_2_VAR_4() == False:
    exit()

print('Введите a\r\n')
a = float(input())
print('Введите b\r\n')
b = float(input())
print('Введите c\r\n')
c = float(input())
print('Число, находящееся на минимальном расстоянии от среднего: ', LAB_2_VAR_4(a,b,c))