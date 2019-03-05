from TestCase import TestCase


class WasRun(TestCase):
    def setup(self):
        self.log = "setup "

    def test_method(self):
        self.log += "test_method "

    def tear_down(self):
        self.log += "tear_down "
