immutable_var=(1969,1970,1971,[1987,1988,1989,1990,1991,1992,1993],'обучение в институте',True,False)
print(immutable_var)
#immutable_var[2]=1972
print("Значения элементов кортежа нельзя изменить, потому что кортеж относится к неизменяемым объектам, \nтак же как строки и числа.Наверно ячейки памяти элементов кортежа идут только для чтения,без возможности перезаписи")
mutable_list=[1987,1988,1989,1990,1991,1992,1993]
mutable_list[0]=2023
mutable_list[1]=2024
mutable_list.append(2025)
mutable_list.extend('word1')
mutable_list.extend('word2')
mutable_list.extend(['word3'])
mutable_list.remove('1')
mutable_list.remove(2025)
print(mutable_list)