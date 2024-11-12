f = open('text.txt').read() # открытие и чтение файла
kolvo=0
for i in f:
    kolvo += len(i) 
print(kolvo) # вывод
