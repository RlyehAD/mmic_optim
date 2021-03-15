from ..models.input import OptimInput
from ..models.output import OptimOutput
from .blueprint_component import OptimBluePrintComponent
from typing import List, Tuple, Optional


__all__ = ["OptimDummyComponent"]


class OptimDummyComponent(OptimBluePrintComponent):
    def execute(
        self,
        inputs: OptimInput,
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, OptimOutput]:

        return True, OptimOutput(procInput=inputs)
