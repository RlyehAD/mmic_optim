from ..models.input import OptimInput
from ..models.output import OptimOutput
from mmic.components.blueprints.generic_component import GenericComponent
import abc
from typing import Dict, List, Tuple, Optional, Any


__all__ = ["OptimBluePrintComponent"]


class OptimBluePrintComponent(GenericComponent, abc.ABC):
    @classmethod
    def input(cls):
        return OptimInput

    @classmethod
    def output(cls):
        return OptimOutput

    @abc.abstractmethod
    def execute(
        self,
        inputs: OptimInput,
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, OptimOutput]:

        raise NotImplementedError
