from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def test_template_method(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert("setup test_method " == self.test.log)


if __name__ == "__main__":
    TestCaseTest("test_template_method").run()
