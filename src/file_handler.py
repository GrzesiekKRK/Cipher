import cipher
import json


class FileHandler:
    def __init__(self, filename: str, contents: cipher.Text):
        self.filename = filename
        self.contents = contents

    def write(self):
        data = {'data': self.contents}
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def read_file(filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return data
