from abc import ABCMeta, abstractmethod
import time as t

class Lamp:
    def turnOn(self): print("Lamp is ON")
    def turnOff(self): print("Lamp is OFF")

class CommandInterface:
    __metaclass = ABCMeta

    @abstractmethod
    def execute(self): pass

class TurnOnCommand(CommandInterface):
    __lamp = None

    def __init__(self, lamp): self.__lamp = lamp

    def execute(self): self.__lamp.turnOn()


class TurnOffCommand(CommandInterface):
    __lamp = None

    def __init__(self, lamp): self.__lamp = lamp

    def execute(self): self.__lamp.turnOff()


class strobos(CommandInterface):
    __lamp = None

    def __init__(self, lamp): self.__lamp = lamp
    def signal(self, delay):
        self.__lamp.turnOn()
        t.sleep(delay)
        self.__lamp.turnOff()
        t.sleep(delay)
    def execute(self):
        print("Strobos is started...")
        for i in range(10):
            self.signal(1)

class LampCommandFactory():
    def get_command(self, type_command, lamp):
        if type_command == "On": return TurnOnCommand(lamp)
        if type_command == "Off": return TurnOffCommand(lamp)
        if type_command == "strob": return strobos(lamp)


lamp = Lamp()
LCF = LampCommandFactory()
on = LCF.get_command("On", lamp)
off = LCF.get_command("Off", lamp)
strob = LCF.get_command("strob", lamp)

on.execute()
off.execute()
strob.execute()