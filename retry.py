import random
from typing import Callable, Any
from functools import wraps


def retry(func: Callable) -> Callable:
    """decorator that retries a function until it returns something other than None"""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        success = False
        while not success:
            result = func(*args, **kwargs)
            if result is not None:
                success = True
        return result
    return wrapper


@retry
def return_three() -> int | None:
    """returns the number 3 randomly, otherwise None"""
    number = random.randint(1, 5)
    if number == 3:
        return number
    return None


if __name__ == "__main__":
    print(return_three())
