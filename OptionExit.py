from Option import Option


class OptionExit(Option):

    def __init__(self, title, store):
        super().__init__(title)
        self.store = store
        self.executed = False

    def execute(self):
        self.executed = True

    def isExecuted(self):
        return self.executed
