# abstract class and abstract method
from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print('connected to power')


class CPU:
    def running(self, com):
        print('it is running')
        com.process()


class Program:
    def compile(self, com):
        print('it is compiling')
        com.process()


com1 = Laptop()
com2 = CPU()

com1.process()
com2.running(com1)

prog1 = Program()
prog1.compile(com1)
