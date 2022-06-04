from pydantic import ValidationError
import pytest
import volder.volder as vc


@pytest.mark.parametrize(
    "temp_amostra,dens_amostra,esperado", [(20, 0.83, 0.8300), (25, 0.83, 0.833354)]
)
def test_mult_volder_dens20(temp_amostra, dens_amostra, esperado):
    volcon = vc.DerConverter()
    assert (
        volcon.dens20(temp_amostra=temp_amostra, dens_amostra=dens_amostra) == esperado
    )


@pytest.mark.parametrize(
    "temp_amostra,dens_amostra,temp_ct,esperado",
    [(20, 0.83, 20, 1.000), (25, 0.83, 25, 0.995859)],
)
def test_mult_volder_fator(temp_amostra, dens_amostra, temp_ct, esperado):
    volcon = vc.DerConverter()
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
    volcon = vc.DerConverter()
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
    volcon = vc.DerConverter()
    volcon.parametros = vc.DerParametros()
    with pytest.raises(ValidationError):
        volcon.fator(
            temp_amostra=temp_amostra, dens_amostra=dens_amostra, temp_ct=temp_ct
        )
