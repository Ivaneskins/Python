'''Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.'''

list = [int(i) for i in input().split()]
uniq = []
for i in list:
    if list.count(i) == 1:
        uniq.append(i)
print(' '.join([str(i) for i in uniq]))

