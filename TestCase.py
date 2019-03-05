class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setup()
        method = getattr(self, self.name)
        method()

    def setup(self):
        pass
