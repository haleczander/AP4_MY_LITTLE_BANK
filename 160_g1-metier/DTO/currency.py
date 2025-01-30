class Currency:
    def __init__(self, label, allowed):
        self.label = label
        self.allowed = allowed
    def get_label(self):
        return self.label
    def is_allowed(self):
        return self.allowed