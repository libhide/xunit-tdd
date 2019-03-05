class WasRun:
    def __init__(self, name):
        self.was_run = None

    def testMethod(self):
        self.was_run = 1

test = WasRun("testMethod")
print(test.was_run)
test.testMethod()
print(test.was_run)
