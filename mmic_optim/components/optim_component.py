from ..models.input import OptimInput
from ..models.output import OptimOutput
from mmic.components.blueprints import StrategyComponent
from typing import Set


__all__ = ["OptimComponent"]


class OptimComponent(StrategyComponent):
    @classmethod
    def input(cls):
        return OptimInput

    @classmethod
    def output(cls):
        return OptimOutput

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
