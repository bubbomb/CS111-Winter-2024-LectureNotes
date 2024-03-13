from simonsays import simonize

import pytest

def test_simonize_base():
    assert simonize('run') == 'Simon says "run"'

def test_simonize_lowercase():
    assert simonize('Run') == 'Simon says "run"'

def test_simonize_verb():
    with pytest.raises(TypeError):
        simonize('pizza chair')

def test_simonize_white_space():
    assert simonize('     join my cult') == 'Simon says "join my cult"'