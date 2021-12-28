class Logger:
    def __init__(self):
        self.filename = assign_file()

    def write(self, string: str, new_line=True):
        with open(self.filename, "a+") as file:
            if new_line:
                file.write(string + "\n")
            else:
                file.write(string)

def assign_file() -> str:
        file = "src/data/game001.txt"
        # file = "src/data/game" + str(num) + ".txt"
        return file