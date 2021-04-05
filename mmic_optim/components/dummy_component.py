from ..models.input import OptimInput
from ..models.output import OptimOutput
from mmic.components.blueprints import SpecificComponent
from typing import List, Tuple, Optional, Set


__all__ = ["OptimDummyComponent"]


class OptimDummyComponent(SpecificComponent):
    """
    A sample component that does nothing interesting. Follow the same structure
    to develop your own optim component. You can attach any helper method to this
    component as long as it does not overwrite the core methods in the :class:
    `SpecificComponent` class.
    """

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

        return True, OptimOutput(proc_input=inputs, molecule=inputs.molecule)
