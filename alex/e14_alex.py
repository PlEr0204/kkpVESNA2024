from random import shuffle
a = []
for i in range (1,100):
    for j in range (0,1000):
        s = list('1'*i+'2'*i)  #поровну единиц и двоек
        shuffle(s)
        s = '0'+''.join(s)+'0' #переделываем из массива(list) в строку и добавляем нули с начала и конца
        while not '00' in s:
            if '011' in s:
                s = s.replace('011','101',1)
            else:
                s = s.replace('01', '40', 1)
                s = s.replace('02', '20', 1)
                s = s.replace('0222', '1401', 1)
        if s.count('1') == 6 and s.count('2') == 9:
            a.append(s.count('4'))
print(min(a))
