from pydantic import ValidationError
import pytest
import volder.volder as vc


@pytest.mark.parametrize(
    "temp_amostra,dens_amostra,esperado", [(20, 0.83, 0.8300), (25, 0.83, 0.82)]
)
def mult_test_volder_dens20(temp_amostra, dens_amostra, esperado):
    volcon = vc.DerConverter()
    assert (
        volcon.dens20(temp_amostra=temp_amostra, dens_amostra=dens_amostra) == esperado
    )


def test_volder():
    dens_amostra: float = 0.83
    temp_amostra: float = 20
    temp_ct: float = 20
    volcon = vc.DerConverter()
    den20: float = volcon.dens20(temp_amostra=temp_amostra, dens_amostra=dens_amostra)
    fator: float = volcon.fator(
        temp_amostra=temp_amostra, dens_amostra=dens_amostra, temp_ct=temp_ct
    )
    assert den20 == 0.8300
    assert fator == 1.0000


def test_invalid_volconv():

    volcon = vc.DerConverter()

    dens_amostra: float = 0.4
    temp_amostra: float = 20

    with pytest.raises(ValidationError):
        volcon.dens20(temp_amostra=temp_amostra, dens_amostra=dens_amostra)

    dens_amostra = 1.3
    temp_amostra = 20

    with pytest.raises(ValidationError):
        volcon.dens20(temp_amostra=temp_amostra, dens_amostra=dens_amostra)

    dens_amostra = 0.83
    temp_amostra = 50

    with pytest.raises(ValidationError):
        volcon.dens20(temp_amostra=temp_amostra, dens_amostra=dens_amostra)

    dens_amostra = 0.83
    temp_amostra = -4

    with pytest.raises(ValidationError):
        volcon.dens20(temp_amostra=temp_amostra, dens_amostra=dens_amostra)

    dens_amostra = 0.83
    temp_amostra = 10

    with pytest.raises(ValidationError):
        volcon.dens20(temp_amostra="a", dens_amostra=dens_amostra)  # type: ignore

    with pytest.raises(ValidationError):
        volcon.dens20(temp_amostra=temp_amostra, dens_amostra="a")  # type: ignore
