from TestResult import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.setup()
        method = getattr(self, self.name)
        method()
        self.tear_down()
        return result
    
    def tear_down(self):
        pass
