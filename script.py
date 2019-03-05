from TestCase import TestCase
from WasRun import WasRun
from TestResult import TestResult
from TestSuite import TestSuite


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

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert("1 run, 1 failed" == result.summary())

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("test_template_method"))
    suite.add(TestCaseTest("test_result"))
    suite.add(TestCaseTest("test_failed_result"))
    suite.add(TestCaseTest("test_failed_result_formatting"))
    suite.add(TestCaseTest("test_suite"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
