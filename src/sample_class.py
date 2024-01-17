class SampleClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        self.c = None

    def task_1(self):
        self.a = self.a + 1

    def task_2(self):
        self.b = self.b + 1

    def task_3(self):
        self.c = 3

    def task_4(self):
        return self.a + self.b + self.c
    
    def task_5(self):
        return "Will not test this task"
