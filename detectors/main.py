class Subject:

    def __init__(self):
        self.observers = []

    def notify(self):
        for observer in self.observers:
            observer.notify(self)


class Observer:

    def notify(self, subject):
        raise NotImplementedError()


class Fridge(Subject):

    def __init__(self):
        super().__init__()
        self._temperature = -5

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()


class ConsoleThermometer(Observer):

    def notify(self, subject):
        print('ConsoleThermometer:', subject.temperature)


class Processor(Observer):

    def notify(self, subject):
        if subject.temperature > 10:
            # охладить до 0-я
            while subject.temperature > 0:
                subject.temperature -= 1


if __name__ == '__main__':
    fridge = Fridge()
    fridge.temperature = 0
    fridge.temperature = 1

    thermometer = ConsoleThermometer()
    fridge.observers.append(thermometer)

    fridge.temperature = 2
    fridge.temperature = 3
    fridge.temperature = 4
    fridge.temperature = 5

    processor = Processor()
    fridge.observers.append(processor)

    fridge.temperature = 2
    fridge.temperature = 3
    fridge.temperature = 4
    fridge.temperature = 5

    fridge.temperature = 15





