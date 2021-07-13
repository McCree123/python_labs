# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:37:24 2020

@author: Comp
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

def LAB_8_VAR_4():
    times = []
    values = []
    selected_subject = []
    subject = []
    measures = []
    _str = ""
    countSubjects = 0
    countRows = 0
    
    times_on_plot = []
    values_on_plot = []
    
    while True:
        print('Введите показатель')
        _str = input()    
        if _str == "end":
            if countSubjects == 0:
                print('Введите хоть один показатель!')
                continue
            else:
                break
        selected_subject.append(_str)
        countSubjects = countSubjects + 1
    
    # Читаем AirAndGhgEmissions
    with open('AirAndGhgEmissions.csv') as csvfile:
        next(csvfile)
        next(csvfile)
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            try:
                subject.append(row['SUBJECT'])
                times.append(row['TIME'])
                values.append(row['Value'])
                measures.append(row['MEASURE'])
                countRows = countRows + 1
            except KeyError:
                print('Некорректный csv файл!')
                return
    i = 0
    measure = []
    measure.append("MLN_TONNE")
    measure.append("THND_TONNE")
    measure.append("TONNE_CAP")
    measure.append("THND_TONNECO2")
    measure.append("KG_CAP")
    while i < countSubjects:
        k = 0
        while k < len(measure):
            j = 0
            while j < countRows:
                if selected_subject[i] == subject[j]:
                    if times[j] != "" and values[j] != "" and measure[k] == measures[j]:
                        times_on_plot.append(int(times[j]))
                        values_on_plot.append(float(values[j]))
                j = j + 1
        
            if len(times_on_plot) == 0:
                k = k + 1
                continue
            
            [f, ax] = plt.subplots(figsize=(15, 10))
        
            ax.set_title('Graphic on subject ' + selected_subject[i] + ' (' + measure[k] + ')')
            ax.set_ylabel('Values')
            ax.set_xlabel('Times')
        
            f.autofmt_xdate()
        
            plt.plot(times_on_plot, values_on_plot)
        
            plt.show()
        
            times_on_plot.clear()
            values_on_plot.clear()
            
            k = k + 1
    
        i = i + 1
    
    # ----------- Доп. задание -----------
    k = ""
    while True:
        print('Введите k')
        k = input()
        bError = False
        try:
            b = int(k)
            if b < 1:
                print('Введите положительное значение больше 1')
                bError = True
            k = float(k)
            if k - b > 0:
                print('Число должно быть целочисленным')
                bError = True
            else: k = int(k)
        except ValueError:
            print('Число должно быть целочисленным, положительным и больше 1')
            bError = True
        
        if bError != True:
            break;
    
    p = ""
    while True:
        print('Введите p')
        p = input()
        bError = False
        try:
            b = int(p)
            if b < 1:
                print('Введите положительное значение больше 1')
                bError = True
            p = float(p)
            if p - b > 0:
                print('Число должно быть целочисленным')
                bError = True
            else: p = int(p)
        except ValueError:
            print('Число должно быть целочисленным, положительным и больше 1')
            bError = True
        
        if bError != True:
            break;
    
    if k > countSubjects:
        k = countSubjects
    
    if p > countSubjects:
        p = countSubjects
    
    selected_subject_ = []
    min_values = []
    max_values = []
    min_time = 1960
    current_time = int(min_time)
    max_time = 2100
    
    while current_time <= max_time:
        i = 0
        while i < countSubjects:
            j = 0
            while j < countRows:
                if selected_subject[i] == subject[j]:
                    if int(times[j]) >= current_time and int(times[j]) <= (current_time + 10):
                        if values[j] != "":
                            values_on_plot.append(float(values[j]))
                j = j + 1
            if len(values_on_plot) > 0:
                min_values.append(min(values_on_plot))
                max_values.append(max(values_on_plot))
                selected_subject_.append(selected_subject[i])
            values_on_plot.clear()
            i = i + 1
    
        print('За период с ' + str(current_time) + ' по ' + str(current_time + 10) + ' года')
        if len(min_values) == 0:
            print('---------- нет данных ----------')
            current_time += 10
            continue
    
        i = 0
        subject_lst = []
        while i < len(selected_subject_):
            subject_lst.append(selected_subject_[i])
            i += 1
    
        print('страны с максимальным показателем:')
        i = 0
        while i < k:
            ind = 1
            max_index = 0
            while ind < len(max_values):
                if max_values[ind] > max_values[max_index]:
                    max_index = ind
                ind += 1
            print('страна ' + subject_lst[max_index] + ':' + str(max_values[max_index]))
            del max_values[max_index]
            del subject_lst[max_index]
            if len(max_values) == 0: break
            i += 1
    
        i = 0
        subject_lst = []
        while i < len(selected_subject_):
            subject_lst.append(selected_subject_[i])
            i += 1
    
        print('страны с минимальным показателем:')
        i = 0
        while i < p:
            ind = 1
            min_index = 0
            while ind < len(min_values):
                if min_values[ind] < min_values[min_index]:
                    min_index = ind
                ind += 1
            print('страна ' + subject_lst[min_index] + ':' + str(min_values[min_index]))
            del min_values[min_index]
            del subject_lst[min_index]
            if len(min_values) == 0: break
            i += 1
        
        current_time += 10
        min_values.clear()
        max_values.clear()
        selected_subject_.clear()


LAB_8_VAR_4()
