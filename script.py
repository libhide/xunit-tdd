from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.was_run)
        test.run()
        assert(test.was_run)

    def test_setup(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.was_setup)


if __name__ == "__main__":
    TestCaseTest("testRunning").run()
    TestCaseTest("test_setup").run()
