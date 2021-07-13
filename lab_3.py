# Код к заданию
def LAB_3_VAR_4(a):
    result = 0;
    if ((a == 0) or (a == 1)):
        return 1;
    result = LAB_3_VAR_4(a - 1) * a;
    return result;

#test 1
def TEST1_LAB_3_VAR_4():
    success_result = 6
    result = LAB_3_VAR_4(3)
    
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
def TEST2_LAB_3_VAR_4():
    success_result = 24
    result = LAB_3_VAR_4(4)
    
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
def TEST3_LAB_3_VAR_4():
    success_result = 120
    result = LAB_3_VAR_4(5)
    
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
print('Lab 3\r\n')
print('Прогон тестовых сценариев...\r\n')
if TEST1_LAB_3_VAR_4() == False:
    exit()
if TEST2_LAB_3_VAR_4() == False:
    exit()
if TEST3_LAB_3_VAR_4() == False:
    exit()

print('Введите a\r\n')
a = int(input())
print('Факториал числа: ', LAB_3_VAR_4(a))