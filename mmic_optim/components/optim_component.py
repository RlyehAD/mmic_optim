from ..models.input import OptimInput
from ..models.output import OptimOutput
from mmic.components.blueprints import GenericComponent
from typing import Set


__all__ = ["OptimComponent"]


class OptimComponent(GenericComponent):
    @classmethod
    def input(cls):
        return OptimInput

    @classmethod
    def output(cls):
        return OptimOutput

    @property
    def supported_comps(self) -> Set[str]:
        """Returns the supported components e.g. set(['mmic_mda',...]).
        Returns
        -------
        Set[str]
        """
        return set(["mmic_optim_openmm"])
