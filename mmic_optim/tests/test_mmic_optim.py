"""
Unit and regression test for the mmic_optim package.
"""

# Import package, test suite, and other packages as needed
import mmic_optim
from mmic_optim.models import OptimInput
from mmic_optim.components.optim_component import OptimComponent
import pytest
import sys


def test_mmic_optim_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_optim" in sys.modules


def test_mmic_optim_models():
    mmic_optim.components.registered.registered_comps.add("mmic_optim")
    inputs = OptimInput(engine="mmic_optim")
    outputs = mmic_optim.components.optim_component.OptimComponent.compute(inputs)
