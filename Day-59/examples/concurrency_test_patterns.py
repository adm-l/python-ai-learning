"""Coordinate concurrency tests with Events, not arbitrary sleeps."""
import threading


def main() -> None:
    started = threading.Event()
    release = threading.Event()
    result: list[str] = []

    def task() -> None:
        started.set()
        if not release.wait(timeout=2):
            raise TimeoutError("test did not release worker")
        result.append("finished")

    thread = threading.Thread(target=task)
    thread.start()
    assert started.wait(timeout=2), "worker did not start"
    release.set()
    thread.join(timeout=2)
    assert not thread.is_alive(), "worker leaked"
    assert result == ["finished"]
    print("coordination test passed")


if __name__ == "__main__":
    main()
