import math

# Код к заданию
def LAB_1_VAR_4(x,y,z):
    return((math.sqrt(x+y)/math.fabs(z)) + math.exp(x))
    
#test 1
def TEST1_LAB_1_VAR_4():
    success_result = 3.295632097648671
    result = LAB_1_VAR_4(1,2,3)
    
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
def TEST2_LAB_1_VAR_4():
    success_result = 20.458214919437633
    result = LAB_1_VAR_4(3,2,6)
    
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
def TEST3_LAB_1_VAR_4():
    success_result = 150.07314571564177
    result = LAB_1_VAR_4(5,1.2,1.5)
    
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
print('Lab 1\r\n')
print('Прогон тестовых сценариев...\r\n')
if TEST1_LAB_1_VAR_4() == False:
    exit()
if TEST2_LAB_1_VAR_4() == False:
    exit()
if TEST3_LAB_1_VAR_4() == False:
    exit()
print('Введите x\r\n')
x = float(input())
print('Введите y\r\n')
y = float(input())
print('Введите z\r\n')
z = float(input())
print('f = ', LAB_1_VAR_4(x,y,z))