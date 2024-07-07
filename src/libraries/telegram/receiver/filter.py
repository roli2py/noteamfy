class Filter:

    @staticmethod
    def filter(type_: str):
        match type_:
            case "command":
                return True
            case _:
                return False
