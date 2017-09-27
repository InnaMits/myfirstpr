
class Lib:
    term = {}
    def __init__(self, key, value):
        self.key = key
        self.value = value
        Lib.term[key] = value
    
    @staticmethod
    def add():
        name = input('Введите термин : ')
        story = input('Введите описание : ')
        obj = Lib(name,story)
        print("Элемент добавлен")
 
    @staticmethod
    def delete():
        name = input('Введите термин : ')
        del Lib.term[name]
 
    @staticmethod
    def printOut():
        for i in Lib.term.items():
            print(i)
 
    @staticmethod
    def change():
       name = input('Введите термин : ')
       Lib.term[name] = input("Новое значение :")
 
    @staticmethod
    def view(name):
        print(Lib.term[name])
  
 
    @staticmethod
    def menu():
        x = -1
        while x != '5':
            print('''1. Вывод терминов - 1\n2. Добавить - 2 \n3. Удалить - 3 \n4. Изменить - 4  \n5. Выход - 5''')
            x = input('Введите значение : ')
            if x == '1':
                Lib.printOut()
            elif x =='2':
                Lib.add()
            elif x == '3':
                Lib.delete()
            elif x == '4':
                Lib.change()
            elif x == '5':
                break
            
a = Lib('Inna','Vakulenchuka 76')
b = Lib('Kirill','Mira 106')
Lib.menu()