import pytest

from bootstrap.kernel.domain.domain_exception import DomainException


def test_domain_exception():
    with pytest.raises(DomainException):
        raise DomainException("Domain error")
