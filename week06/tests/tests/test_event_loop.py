from unittest.mock import patch

import pytest

from toy_event_loop import EventLoop, Sleep, sleep, worker


@pytest.fixture
def event_loop() -> EventLoop:
    return EventLoop()


def test_sleep_creates_sleep_object() -> None:
    generator = sleep(2)

    result = next(generator)

    assert isinstance(result, Sleep)
    assert result.delay == 2


@pytest.mark.parametrize(
    "delay",
    [0, 1, 2, 5],
)
def test_sleep_delay(delay: float) -> None:
    generator = sleep(delay)

    result = next(generator)

    assert isinstance(result, Sleep)
    assert result.delay == delay


def test_create_task(event_loop: EventLoop) -> None:
    event_loop.create_task(worker("Task A", 1))

    assert len(event_loop.ready) == 1


def test_task_runs_coroutine(event_loop: EventLoop) -> None:
    event_loop.create_task(worker("Task A", 0))

    task = event_loop.ready.popleft()

    with patch("builtins.print"):
        result = task.run()

    assert isinstance(result, Sleep)
    assert result.delay == 0


def test_event_loop_completes_task(event_loop: EventLoop) -> None:
    event_loop.create_task(worker("Task A", 0))

    with patch("time.sleep"):
        event_loop.run_forever()

    assert len(event_loop.ready) == 0
    assert len(event_loop.sleeping) == 0


def test_event_loop_runs_multiple_tasks(event_loop: EventLoop) -> None:
    event_loop.create_task(worker("Task A", 0))
    event_loop.create_task(worker("Task B", 0))
    event_loop.create_task(worker("Task C", 0))

    with patch("time.sleep"):
        event_loop.run_forever()

    assert len(event_loop.ready) == 0
    assert len(event_loop.sleeping) == 0


def test_event_loop_waits_when_no_ready_tasks(
    event_loop: EventLoop,
) -> None:
    event_loop.create_task(worker("Task A", 1))

    task = event_loop.ready.popleft()
    sleep_obj = task.run()

    event_loop.sleeping.append((task, sleep_obj))

    # Make the task appear to still be sleeping.
    with patch(
        "toy_event_loop.time.perf_counter",
        return_value=sleep_obj.wake_time - 1,
    ):
        with patch("toy_event_loop.time.sleep") as mock_sleep:
            # Make the sleep call end the loop instead of
            # actually waiting forever.
            mock_sleep.side_effect = lambda _: event_loop.sleeping.clear()

            event_loop.run_forever()

    mock_sleep.assert_called_once_with(0.01)