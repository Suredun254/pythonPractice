class Pycharm:
    def execute(self):
        print('compiling')
        print('running ')


class Myide:
    def execute(self):
        print('it executes')
        print('it edits')


class Laptop:
    def code(self, ide):
        ide.execute()


# ide = Pycharm()

ide = Myide()
lap1 = Laptop()
lap1.code(ide)
