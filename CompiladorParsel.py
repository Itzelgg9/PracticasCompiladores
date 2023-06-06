class Parser:
    def __init__(self):
        self.stack = []
        self.parsing_table = {
            ("Q", "select"): ["D"],
            ("D", "select"): ["select", "P"],
            ("P", "from"): ["from", "id"],
            ("P", "id"): ["id"],
            ("P", "id", ","): ["id", ",", "P"],
            ("P", "*"): ["*"],
            ("P", "*", "from"): ["*", "from", "id"]
        }

    def parse(self, tokens):
        self.stack = ["$", "Q"]
        index = 0

        while self.stack:
            current_token = tokens[index] if index < len(tokens) else "$"
            top = self.stack[-1]

            print("Current Token:", current_token)
            print("Top of Stack:", top)

            if top == current_token:
                if top == "$":
                    print("Accepted")
                    return True

                self.stack.pop()
                index += 1
                print("Matched terminal:", current_token)
            else:
                key = (top, current_token)
                if key in self.parsing_table:
                    production = self.parsing_table[key]
                    self.stack.pop()
                    for symbol in reversed(production):
                        self.stack.append(symbol)
                    print("Reduced using production:", production)
                else:
                    print("Unexpected token:", current_token)
                    return False

        return False


class CompiladorParsel:
    def __init__(self):
        self.parser = Parser()

    def run(self):
        tokens = ["select", "*", "from", "id"]

        result = self.parser.parse(tokens)

        if result:
            print("La secuencia es válida según la gramática.")
        else:
            print("La secuencia no es válida según la gramática.")


compilador = CompiladorParsel()
compilador.run()
