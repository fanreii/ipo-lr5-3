f = open('text.txt').read()
kolvo=0
for i in f:
    kolvo += len(i) 
print(kolvo)