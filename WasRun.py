from TestCase import TestCase


class WasRun(TestCase):
    def setup(self):
        self.was_run = None
        self.log = "setup "

    def test_method(self):
        self.was_run = 1
        self.log += "test_method "
