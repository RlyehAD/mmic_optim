from ..models.input import InputOptim
from ..models.output import OutputOptim
from mmic.components.blueprints import StrategyComponent
from typing import Set


__all__ = ["OptimComponent"]


class OptimComponent(StrategyComponent):
    @classmethod
    def input(cls):
        return InputOptim

    @classmethod
    def output(cls):
        return OutputOptim

    @classmethod
    def get_version(cls) -> str:
        """Finds program, extracts version, returns normalized version string.
        Returns
        -------
        str
            Return a valid, safe python version string.
        """
        return ""

    @classmethod
    def tactic_comps(cls) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        return set(["mmic_optim_openmm"])
