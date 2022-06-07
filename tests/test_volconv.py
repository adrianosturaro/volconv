from pydantic import ValidationError
import pytest
from volder import DerConverter as dc  # type: ignore


@pytest.mark.parametrize(
    "temp_amostra,dens_amostra,esperado",
    [
        (20, 0.83, 0.8300),
        (25, 0.83, 0.833354),
        ("20", 0.83, 0.8300),
        (20, "0.83", 0.8300),
    ],
)
def test_mult_volder_dens20(temp_amostra, dens_amostra, esperado):
    volcon = dc()
    assert (
        volcon.dens20(temp_amostra=temp_amostra, dens_amostra=dens_amostra) == esperado
    )


@pytest.mark.parametrize(
    "temp_amostra,dens_amostra,temp_ct,esperado",
    [
        (20, 0.83, 20, 1.000),
        (25, 0.83, 25, 0.995859),
        ("20", 0.83, 20, 1.000),
        (20, "0.83", 20, 1.000),
        (20, 0.83, "20", 1.000),
    ],
)
def test_mult_volder_fator(temp_amostra, dens_amostra, temp_ct, esperado):
    volcon = dc()
    assert (
        volcon.fator(
            temp_amostra=temp_amostra, dens_amostra=dens_amostra, temp_ct=temp_ct
        )
        == esperado
    )


@pytest.mark.parametrize(
    "temp_amostra,dens_amostra",
    [
        (-1, 0.83),
        (80, 0.83),
        (25, 0.3),
        (25, 1.4),
        (80, 1.4),
        ("a", 0.83),
        (80, "b"),
        ("a", "b"),
    ],
)
def test_mult_invalid_volder_dens(temp_amostra, dens_amostra):
    volcon = dc()
    with pytest.raises(ValidationError):
        volcon.dens20(temp_amostra=temp_amostra, dens_amostra=dens_amostra)


@pytest.mark.parametrize(
    "temp_amostra,dens_amostra,temp_ct",
    [
        (-1, 0.83, 20),
        (80, 0.83, 20),
        (20, 0.3, 20),
        (-1, 1.4, 20),
        (20, 0.83, -1),
        (20, 0.83, 80),
        ("a", 0.83, 20),
        (-1, "a", 20),
        (-1, 0.83, "a"),
    ],
)
def test_mult_invalid_volder_fator(temp_amostra, dens_amostra, temp_ct):
    volcon = dc()
    with pytest.raises(ValidationError):
        volcon.fator(
            temp_amostra=temp_amostra, dens_amostra=dens_amostra, temp_ct=temp_ct
        )
