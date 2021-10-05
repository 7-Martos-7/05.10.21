bums=open('aste.txt', 'a', encoding='utf-8')
bums.write('Ģrobiņā nav vēl sniega!')

bums=open('aste.txt', 'r', encoding='utf-8')
print(bums.read())




bums.close()