class Root:
    def identify(self):
        print("Root")


class Left(Root):
    def identify(self):
        print("Left")
        super().identify()


class Right(Root):
    def identify(self):
        print("Right")
        super().identify()


class Combined(Left, Right):
    def identify(self):
        print("Combined")
        super().identify()


if __name__ == "__main__":
    print("MRO:", [cls.__name__ for cls in Combined.__mro__])
    Combined().identify()
