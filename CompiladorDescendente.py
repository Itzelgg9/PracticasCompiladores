class SQLDescendente:
    def __init__(self):
        self.TABLE = {
            "Q": {"select": "D"},
            "D": {"distinct": "P", "identificador": "P"},
            "P": {"*": "", "identificador": "A"},
            "A": {"identificador": "A2A1"},
            "A1": {",": "A", "$": ""},
            "A2": {"identificador": "A3"},
            "A3": {"identificador": "", ".": "A", "$": ""},
            "T": {"identificador": "T2T1"},
            "T1": {",": "T", "$": ""},
            "T2": {"identificador": "T3"},
            "T3": {"identificador": "", "$": ""}
        }

    def analyze(self, input):
        stack = ["$", "Q"]
        index = 0

        while stack:
            top = stack[-1]
            current_symbol = input[index] if index < len(input) else "$"

            if top in self.TABLE and current_symbol in self.TABLE[top]:
                action = self.TABLE[top][current_symbol]

                if not action:
                    stack.pop()
                else:
                    stack.pop()
                    symbols = action.split()
                    stack.extend(reversed(symbols))

                if current_symbol != "$":
                    index += 1
            else:
                return False

        return index == len(input)

def main():
    input_string = "select * from id"
    parser = SQLDescendente()
    is_valid = parser.analyze(input_string)

    if is_valid:
        print("La cadena es válida.")
    else:
        print("La cadena no es válida.")

if __name__ == "__main__":
    main()
