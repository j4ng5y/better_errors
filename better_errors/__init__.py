from typing import Any, NoReturn, Union, Optional


class Result:
    """
    Result represents a container that holds either an actual value or object (ok) or an exception object (err).

    Attributes
    ----------
    ok : Any | None
        the actual value of a successful operation
    err : Exception | None
        an Error object if an operation were to fail

    Methods
    -------
    value() -> Any | Exception:
        returns the non-None value of the class. If both attributes are None, returns a non-None exception describing
        that no attributes have values.
    """

    __slots__ = ['ok', 'err']

    def __init__(self, ok: Optional[Any], err: Optional[Exception]) -> NoReturn:
        """
        Constructs all necessary attributes for the Result object.

        :param ok Any | None:
            the actual value of a successful operation
        :param err Exception | None:
            an Exception object if an operation were to fail
        """
        self.ok = ok
        self.err = err

    def __repr__(self):
        return f"Result({self.ok!r}, {self.err!r})"

    def __str__(self):
        return f"Result({self.ok}, {self.err})"

    def value(self) -> Union[Any, Exception]:
        """
        Returns the non-None value of the class.

        If no value is non-None, this function will return a non-None Exception value describing the situation.

        :return: Union[Any, Exception]
        """
        if self.err is not None:
            return self.err
        else:
            if self.ok is not None:
                return self.ok
            else:
                return Exception("no result or error")