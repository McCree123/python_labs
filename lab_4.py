# Код к заданию
def LAB_4_VAR_4(message,g,s):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    cnt_b = []
    for rem in s:
        alphabet = alphabet.replace(rem, '')
    for a in alphabet:
        cnt_b.append(0);
    for b_m in message:
        ind = alphabet.find(b_m)
        if ind != -1:
            cnt_b[ind] += 1
    i = 0
    ind_max_cnt_b = 0
    max_ = cnt_b[0]
    for num in cnt_b[1:]:
        i += 1
        if max_ < num:
            max_ = num
            ind_max_cnt_b = i
    if g != 0 and max_ != 0:
        string_ = s + alphabet[ind_max_cnt_b]
        return alphabet[ind_max_cnt_b] + LAB_4_VAR_4(message, g-1, string_)
    else:
        return ''

#test 1
def TEST1_LAB_4_VAR_4():
    success_result = 'qwer'
    result = LAB_4_VAR_4('qwertyuiop', 4, '')
    
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
def TEST2_LAB_4_VAR_4():
    success_result = 'rtyqweuiop'
    result = LAB_4_VAR_4('qwerrrrrttttyyyuiop', 10, '')
    
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
def TEST3_LAB_4_VAR_4():
    success_result = 'qerty'
    result = LAB_4_VAR_4('qqwwwwwerty', 6, 'w')
    
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
print('Lab 4\r\n')
print('Прогон тестовых сценариев...\r\n')
if TEST1_LAB_4_VAR_4() == False:
    exit()
if TEST2_LAB_4_VAR_4() == False:
    exit()
if TEST3_LAB_4_VAR_4() == False:
    exit()

print('Введите сообщение строчными латинскими буквами\r\n')
message = input()
print('Сколько самых встречающихся букв от самого часто встречаемого до самого менее встречаемого вывести?')
g = int(input())
print('Какие буквы игнорировать при подсчёте? (Оставьте строку пустой если это не требуется)')
s = input()
print('Самые часто встречаемые буквы: ', LAB_4_VAR_4(message,g,s))