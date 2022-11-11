class Dog:
    def __init__(self, angry):
        self.angry = angry
    def say_gaw(self): # имя self для первого аргумента метода
        # это общепринятое но не обязательное правило
        if self.angry:
            print("!GAW-GAW!")
        else:
            print("gaw-gaw")
    def ping(self):
        self.angry = True

    def feed(self, food_count):
        if food_count > 10:
            self.angry = False


my_dog = Dog(True)
my_dog.say_gaw()      # вызовется функция Dog.say_gaw с параметром self = my_dog
my_dog.feed(14)
my_dog.say_gaw()
my_dog.ping()
my_dog.say_gaw()
my_dog.feed(3)
my_dog.say_gaw()
my_dog = Dog()