from typing import Callable, Any


def cache(func: Callable) -> Callable:
    story = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in story or tuple(kwargs.values()) in story:
            print("Getting from cache")
        else:
            if len(args) != 0:
                story[args] = func(*args, **kwargs)
            else:
                story[tuple(kwargs.values())] = func(*args, **kwargs)
            print("Calculating new result")
        return story[args] if len(args) != 0 else story[tuple(kwargs.values())]
    return wrapper


@cache
def long_time_func(number_one: int, number_two: int, number_three: int) -> int:
    return ((number_one ** number_two ** number_three)
            % (number_one * number_three))


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
