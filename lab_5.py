# Код к заданию
def LAB_5_VAR_4(message):
    msg = message.lower()
    symbols = 'бвгджз'
    ret = ''
    i = -1
    ind = -1
    
    for s in symbols:
        i += 1
        ind = msg.find(s)
        if ind == -1:
            ret += s
    
    return ret

#test 1
def TEST1_LAB_5_VAR_4():
    success_result = 'бгд'
    result = LAB_5_VAR_4('Ёжик резиновый')
    
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
def TEST2_LAB_5_VAR_4():
    success_result = 'бгджз'
    result = LAB_5_VAR_4('шёл и насвистывал')
    
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
def TEST3_LAB_5_VAR_4():
    success_result = 'гжз'
    result = LAB_5_VAR_4('с дырочкой в правом боку')
    
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
print('Lab 5\r\n')
print('Прогон тестовых сценариев...\r\n')
if TEST1_LAB_5_VAR_4() == False:
    exit()
if TEST2_LAB_5_VAR_4() == False:
    exit()
if TEST3_LAB_5_VAR_4() == False:
    exit()

print('Введите сообщение русскими буквами\r\n')
message = input()
print('Глухие согласные буквы в алфавитном порядке, которые не встречаются:', LAB_5_VAR_4(message))