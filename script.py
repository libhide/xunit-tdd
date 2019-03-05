class WasRun:
    def __init__(self, name):
        self.was_run = None


test = WasRun("testMethod")
print(test.was_run)
test.testMethod()
print(test.was_run)
