from ..models.input import OptimInput
from ..models.output import OptimOutput
from .blueprint_component import OptimBluePrintComponent
from mmic.components.blueprints.generic_component import GenericComponent
from .registered import registered_comps
from typing import Dict, List, Set, Optional, Any, Tuple
import importlib

__all__ = ["OptimComponent"]


class OptimComponent(GenericComponent):
    @classmethod
    def input(cls):
        return OptimInput

    @classmethod
    def output(cls):
        return OptimOutput

    def execute(
        self,
        inputs: OptimInput,
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, OptimOutput]:

        comp = inputs.engine
        if comp not in registered_comps:
            raise NotImplementedError(
                f"Component {comp} not supported. Solve by invoking:\n"
                + f"mmic_optim.registered_comps.add({comp})"
            )

        if comp not in self.installed():
            raise ModuleNotFoundError(f"Component {comp} not installed.")

        comp_mod = importlib.import_module(comp)
        return True, comp_mod._mainComponent.compute(inputs)

    @staticmethod
    def installed(trans: Optional[Set[str]] = registered_comps) -> List[str]:
        """Returns module spec if it exists.
        Parameters
        ----------
        trans: Set[str], optional
            Supported translator names to check.
        Returns
        -------
        List[str]
            Component names that are installed.
        """
        return [spec for spec in trans if importlib.util.find_spec(spec)]

    @staticmethod
    def find_comp(dtype: str, trans: Optional[Set[str]] = registered_comps) -> str:
        """Returns mmic_component name (if any) corresponding to a specific data type.
        If no appropriate toolkit is available on the system, this method raises an error.
        Parameters
        ----------
        dtype: str
            Data type e.g. MDAnalysis, parmed, etc.
        trans: Set[str], optional
            Supported translator names to check.
        Returns
        -------
        str
            Translator name e.g. mmic_parmed
        """
        for trans, tk in trans.items():
            if dtype == tk:
                return trans

        raise ValueError(f"Could not find appropriate toolkit for {dtype} object.")
