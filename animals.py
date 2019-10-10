# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Animal:
    _metaclass_ = ABCMeta

    def accept(self, operation): pass


class AnimalOperation:
    _metaclass_ = ABCMeta

    def visitMonkey(self, monkey): pass

    def visitLion(self, lion): pass

    def visitDolphin(self, dolphin): pass


class Monkey(Animal):

    def shout(self): print("OOh oo aaa!")

    def accept(self, operation): operation.visitMonkey(self)


class Lion(Animal):

    def roar(self): print("Grrr!")

    def accept(self, operation): operation.visitLion(self)


class Dolphin(Animal):

    def speak(self): print("tiiia!")

    def accept(self, operation): operation.visitDolphin(self)


class Speak(AnimalOperation):
    def visitMonkey(self, monkey): monkey.shout()

    def visitLion(self, lion): lion.roar()

    def visitDolphin(self, dolphin): dolphin.speak()


monkey = Monkey()
lion = Lion()
dolphin = Dolphin()
speak = Speak()
monkey.accept(speak)
monkey.shout()
lion.accept(speak)
dolphin.accept(speak)