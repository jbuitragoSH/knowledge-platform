from bootstrap.kernel.domain.error import Error


def test_error_has_code_and_message():
    error = Error(
        code="INVALID",
        message="Invalid value",
    )

    assert error.code == "INVALID"

    assert error.message == "Invalid value"
