from utils.stats import popularsbar, populars

print('1: Get Popular Categories As Bar \n2: Get Popular Categories By Text\n')
select = int(input('Input: '))
if select == 1:
    k = int(input('n Category: '))
    popularsbar('../data/raw.csv',k)

elif select == 2:
    k = int(input('n Category: '))
    populars('../data/raw.csv',k)
