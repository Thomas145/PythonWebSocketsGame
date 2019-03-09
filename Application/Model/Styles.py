import uuid
import string


class NoStyle:

    def __init__(self):
        self.id = uuid.uuid4()

    def display(self):
        return ""

    def selected(self):
        return False

    def same_style(self, style):
        return False


class SelectedStyle(NoStyle):

    def __init__(self, index):
        self.id = uuid.uuid4()
        self.char = string.ascii_uppercase[index:index+1]

    def display(self):
        return self.char

    def selected(self):
        return True

    def same_style(self, style):
        return style.id == self.id

