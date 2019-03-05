from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.was_run = 1

