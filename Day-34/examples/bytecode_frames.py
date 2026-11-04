import dis
import inspect
import traceback


def calculate_total(values):
    total = 0
    for value in values:
        total += value
    return total


def outer():
    return calculate_total([1, 2, 3])


if __name__ == "__main__":
    print("result:", outer())
    print("code object:", calculate_total.__code__.co_name)
    print("signature:", inspect.signature(calculate_total))
    print("bytecode:")
    dis.dis(calculate_total)

    try:
        1 / 0
    except ZeroDivisionError:
        print("traceback:")
        traceback.print_exc()
