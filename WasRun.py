class WasRun:
    def __init__(self, name):
        self.was_run = None

    def testMethod(self):
        self.was_run = 1

    def run(self):
        self.testMethod()
