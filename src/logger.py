class Logger:
    def __init__(self):
        self.filename = assign_file()

    def write(self, string: str):
        with open(self.filename, "a+") as file:
            file.write(string + "\n")

def assign_file() -> str:
        file = "src/data/game001.txt"
        # file = "src/data/game" + str(num) + ".txt"
        return file