from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def setup(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.was_run)

    def test_setup(self):
        self.test.run()
        assert(self.test.was_setup)


if __name__ == "__main__":
    TestCaseTest("testRunning").run()
    TestCaseTest("test_setup").run()
