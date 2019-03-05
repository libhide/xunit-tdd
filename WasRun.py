from TestCase import TestCase


class WasRun(TestCase):
    def setup(self):
        self.was_run = None
        self.was_setup = 1

    def test_method(self):
        self.was_run = 1
