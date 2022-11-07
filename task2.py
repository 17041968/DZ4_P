#В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
data = open('icecream.txt', 'r', encoding='utf-8')
icecream = data.readlines()
data.close()

first = set(icecream[0].replace('\n', '').split(', '))
second = set(icecream[1].replace('\n', '').split(', '))
print(first)
print(second)
print(first.difference(second))