from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def test_template_method(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert("setup test_method tear_down " == self.test.log)

    def test_result(self):
        self.test = WasRun("test_method")
        result = self.test.run()
        assert("1 run, 0 failed" == result.summary())

    def test_failed_result(self):
        self.test = WasRun("test_broken_method")
        result = self.test.run()
        assert("1 run, 1 failed" == result.summary())


if __name__ == "__main__":
    TestCaseTest("test_template_method").run()
    TestCaseTest("test_result").run()
