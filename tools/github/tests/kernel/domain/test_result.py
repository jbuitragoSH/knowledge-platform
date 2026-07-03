from bootstrap.kernel.domain.error import Error
from bootstrap.kernel.domain.result import Result


def test_result_ok():
    result = Result.ok("hello")

    assert result.success

    assert result.value == "hello"

    assert result.error is None


def test_result_fail():
    error = Error(
        code="INVALID",
        message="Invalid",
    )

    result = Result.fail(error)

    assert not result.success

    assert result.value is None

    assert result.error == error
