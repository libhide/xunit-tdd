from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def setup(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert(self.test.was_run)

    def test_setup(self):
        self.test.run()
        assert("setup " == self.test.log)


if __name__ == "__main__":
    TestCaseTest("test_running").run()
    TestCaseTest("test_setup").run()
