'''1.Дан список из строк. Вывести из списка только те элементы, которые содержат символ «b».'''
'''s1 = ('yellow','blue','red') #Значения в которых будет производиться поиск нужной нам буквы
s = list(filter(lambda x: 'b' in x, s1)) #Поиск нужно нам бквы 
print(s) #Вывод ответа

s2 = [s1[i] for i in range(len(s1)) if 'b' in s1[i]]#Поиск нужно нам бквы 
print(s2)#Вывод ответа'''

'''2.Дан список из строк. Вывести список, состоящий из символов в верхнем регистре'''
'''word = ['banana','lemon','apple']
word = list (map(lambda x: x.upper(), word))
print(word)

word2 = list(filter(lambda x: x.upper(), (word)))
print(word2)'''

'''6.Даны два списка чисел. Сформировать список, содержащий только те элементы первого списка, которые есть во втором списке'''
'''list1 = ['11','26','34','42'] #Значение первого листа 
list2 = ['11','26','32','74'] #Значение второго листа 
main_list = list(filter(lambda x: x in list2,  list1)) ##Фильтруем элементы из списков
print(main_list) #Выводим сформированный новый список '''

'''7.Даны два списка чисел. Сформировать список, содержащий только те элементы первого списка, которых нет во втором списке'''
'''list1 = ['1','2','3','4'] #Значение первого листа 
list2 = ['1','6','2','7'] #Значение второго листа 
main_list = list(filter(lambda x: x not in list2,  list1)) #Фильтруем элементы из списков
print(main_list) #Выводим сформированный новый список '''