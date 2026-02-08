from typing import Callable


def cache(func: Callable) -> Callable:
    story = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in story:
            print("Getting from cache")
        else:
            story[args] = func(*args, **kwargs)
            print("Calculating new result")
        return story[args]
    return wrapper


@cache
def long_time_func(number_one: int, number_two: int, number_three: int) -> int:
    return ((number_one ** number_two ** number_three)
            % (number_one * number_three))


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
