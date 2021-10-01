from ..models.input import OptimInput
from ..models.output import OptimOutput
from mmic.components.blueprints import StrategyComponent
from cmselemental.util.decorators import classproperty
from typing import Set


__all__ = ["OptimComponent"]


class OptimComponent(StrategyComponent):
    @classproperty
    def input(cls):
        return OptimInput

    @classproperty
    def output(cls):
        return OptimOutput

    @classproperty
    def version(cls) -> str:
        """Finds program, extracts version, returns normalized version string.
        Returns
        -------
        str
            Return a valid, safe python version string.
        """
        return ""

    @classproperty
    def tactic_comps(cls) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        return {"mmic_optim_openmm", "mmic_optim_gmx"}
