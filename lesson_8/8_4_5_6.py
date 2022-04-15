# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class InCorrectData(Exception):
    def __init__(self, text):
        self.text = text


class NotEnSpace(Exception):
    def __init__(self, free_places, need):
        self.free_places = free_places
        self.need = need

    def __str__(self):
        return f'Not enough space, free places = {self.free_places}, need = {self.need}'


class Warehouse:
    def __init__(self, places):
        self.places = places
        self.base = {}
        self.all_info = {}
        self.all_obj = {}

    def accept(self, product, quantity):
        if type(quantity) != int:
            raise InCorrectData('Количество должно быть задано целым числом!')
        free_places = self.places - sum(self.base.values())
        if quantity > free_places:
            raise NotEnSpace(free_places, quantity)
        ad_info = {}
        ad_obj = {}
        if product.product_type in self.base.keys():
            c = self.base[product.product_type]
            self.base[product.product_type] += quantity
            for i in range(c, c+quantity):
                ad_info[i] = product.info
                ad_obj[i] = self
                self.all_info[product.product_type][i] = ad_info[i]
                self.all_obj[product.product_type][i] = ad_obj[i]
        else:
            self.base[product.product_type] = quantity
            for i in range(quantity):
                ad_info[i] = product.info
                ad_obj[i] = self
            self.all_info[product.product_type] = ad_info
            self.all_obj[product.product_type] = ad_obj

    def send(self, product, quantity):
        # дописать исключения
        if type(quantity) != int:
            raise InCorrectData('Количество должно быть задано целым числом!')
        if product in self.base.keys():
            if quantity <= self.base[product]:
                [self.all_info[product].pop(key) for key in range(self.base[product] - quantity, self.base[product])]
                #for i in range(self.base[product]-quantity, self.base[product]):
                    #del self.all_info[product][i]
                self.base[product] -= quantity

            else:
                print(f'There is not enough quantity of the {product} product in our Warehouse. Sorry')
                # можно отправлять сколько есть, писать сколько есть и их отправлять
        else:
            print('There is no such a product in our Warehouse. Sorry')


class OfficeEquipment:
    def __init__(self, p, n):
        self.price = p
        self.name = n


class Printer(OfficeEquipment):
    def __init__(self, p, n, ps):
        super().__init__(p, n)
        self.paper_size = ps
        self.product_type = 'printer'
        self.info = {'price': self.price, 'name': self.name, 'paper_size': self.paper_size}


class Scanner(OfficeEquipment):
    def __init__(self, p, n, q):
        super().__init__(p, n)
        self.quality = q
        self.product_type = 'scanner'
        self.info = {'price': self.price, 'name': self.name, 'quality': self.quality}


class Xerox(OfficeEquipment):
    def __init__(self, p, n, speed):
        super().__init__(p, n)
        self.speed = speed
        self.product_type = 'xerox'
        self.info = {'price': self.price, 'name': self.name, 'speed': self.speed}


my_warehouse = Warehouse(100)
my_printer = Printer(200, 'hp', 'A4')
my_scanner = Scanner(150, 'LG', 'high')
my_xerox = Xerox(60, 'Sony', 50)
my_printer_1 = Printer(280, 'hps', 'A3')

my_warehouse.accept(my_printer, 2)
print(my_warehouse.base)
print(my_warehouse.all_info)

my_warehouse.accept(my_scanner, 1)
print(my_warehouse.base)
print(my_warehouse.all_info)

my_warehouse.accept(my_xerox, 3)
print(my_warehouse.base)
print(my_warehouse.all_info)

my_warehouse.accept(my_printer_1, 2)
print(my_warehouse.base)
print(my_warehouse.all_info)


try:
    my_warehouse.send('printer', 3)

except InCorrectData as err:
    print(err)

print(my_warehouse.base)
print(my_warehouse.all_info)

try:
    my_warehouse.accept(my_scanner, 110)
except InCorrectData as err:
    print(err)
except NotEnSpace as err:
    print(err)
print(my_warehouse.base)
print(my_warehouse.all_info)








