class Stationery():
    title = "принадлежность"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Ручка не стирается ластиком.")


class Penсil(Stationery):
    def draw(self):
        print("Карандашом можно рисовать.")


class Handle(Stationery):
    def draw(self):
        print("Купил цветные маркеры, карандаш мне больше не нужен")


class Paint(Stationery):
    pass


pen = Pen()
pen.draw()

pencil = Penсil()
pencil.draw()

handle = Handle()
handle.draw()

# В данном случае мы используем метод родительского класса, так как одноименного в экземпляре нет.
paint = Paint()
paint.draw()
