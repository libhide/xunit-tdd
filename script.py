from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.was_run)
        test.run()
        assert(test.was_run)

if __name__ == "__main__":
    TestCaseTest("testRunning").run()
