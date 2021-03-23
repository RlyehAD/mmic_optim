"""
Unit and regression test for the mmic_optim package.
"""

# Import package, test suite, and other packages as needed
import mmic_optim
from mmic_optim import OptimInput, OptimComponent
import pytest
import sys
import json
import os


mol_file = os.path.join("mmic_optim", "data", "molecule.json")
ff_file = os.path.join("mmic_optim", "data", "forcefield.json")


def test_mmic_optim_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_optim" in sys.modules


def test_mmic_optim_models():
    with open(mol_file, "r") as fp:
        mol = json.load(fp)

    with open(ff_file, "r") as fp:
        ff = json.load(fp)

    inputs = OptimInput(
        component="mmic_optim", molecule={"mol": mol}, forcefield={"mol": ff}
    )
    outputs = mmic_optim.components.optim_component.OptimComponent.compute(inputs)
