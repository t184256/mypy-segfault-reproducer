import functools
from typing import Callable, ParamSpec, TypeVar, overload

_P = ParamSpec('_P')
_T = TypeVar('_T')


@overload  # for decorating with decorator(), None -> f(func -> decorated_func)
def decorator(
    callable_: None = None,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    ...


@overload  # for decorating with decorator, func -> decorated func
def decorator(callable_: Callable[_P, _T]) -> Callable[_P, _T]:
    ...


def decorator(
    callable_: Callable[_P, _T] | None = None,
) -> (
    Callable[_P, _T] |
    Callable[[Callable[_P, _T]], Callable[_P, _T]]
):
    if callable_ is None:
        return decorate
    return decorate(callable_)


# do the actual decorating
def decorate(f: Callable[_P, _T]) -> Callable[_P, _T]:
    @functools.wraps(f)
    def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        print(f, args, kwargs)
        return f(*args, **kwargs)

    return wrapper


# that'd how I'd like to use it then

@decorator
def f(x):
    return x


@decorator()
def g(x):
    return x


print(f(3))
print(g(3))
