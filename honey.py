def open_file(file):
    '''Открываем файл'''
    honey_file = open(file=file, mode='r', encoding='utf-8')
    return honey_file


def order_dict(file_info):
    '''Принимаем информацию из файла
    Возвращаем словарь словарей
    заказ->пчеловод->заказчик->сорт меда: количество'''
    zakaz = {}
    for line in honey_file:
        if 'заказ' in line.lower():
            beekeeper = line.split()[-1][:-1]
            if beekeeper not in zakaz:
                zakaz[beekeeper] = {}
        elif len(line) > 3:
            order = line.strip('\n;').split(':')
            customer, goods_all = order
            if customer not in zakaz[beekeeper]:
                zakaz[beekeeper][customer] = {}
            kinds_goods = goods_all.strip('\n;').split(',')
            customer_order = zakaz[beekeeper][customer]
            for good in kinds_goods:
                good_2 = good.strip().split(' - ')
                customer_order[good_2[0]] = int(good_2[1])
        else:
            continue
    return zakaz


def beekeeper_order_dict(zakaz):
    beekeeper_order = {}
    for beekeeper in zakaz:
        beekeeper_order[beekeeper] = {}
        for cust in zakaz[beekeeper]:
            for honey in zakaz[beekeeper][cust]:
                if honey not in beekeeper_order[beekeeper]:
                    beekeeper_order[beekeeper][honey] = 0
                beekeeper_order[beekeeper][honey] += zakaz[beekeeper][cust][honey]
    return beekeeper_order


def order_print(beekeper_order):
    for beekeeper in beekeeper_order:
        ext = f'Заказано у {beekeeper}: '
        ext_list = []
        for honey in beekeeper_order[beekeeper]:
            ext_list.append(f'{honey} - {beekeeper_order[beekeeper][honey]}')
        ext = ext + ', '.join(ext_list) + '.'
        print(ext)


'''Открываем файл'''
file = 'Honey_2021.txt'
honey_file = open_file(file)

'''
Собираем информацию о заказе из файла в словари:
заказ->пчеловод->заказчик->сорт меда: количество
'''
zakaz = order_dict(honey_file)

'''
Закрываем файл
'''
honey_file.close()

'''
Собираем информацию в словарь:
пчеловод->сорт меда: общее количество (по сорту)
'''
beekeeper_order = beekeeper_order_dict(zakaz)

'''
Пытаемся красиво вывести
'''
order_print(beekeeper_order)


'''
Конец
'''
