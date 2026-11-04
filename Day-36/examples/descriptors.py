class PositiveInteger:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            raise ValueError(f"{self.name} must be a positive integer")
        instance.__dict__[self.name] = value


class RetryPolicy:
    attempts = PositiveInteger()


if __name__ == "__main__":
    policy = RetryPolicy()
    policy.attempts = 3
    print("attempts:", policy.attempts)
    try:
        policy.attempts = 0
    except ValueError as exc:
        print("validation:", exc)
