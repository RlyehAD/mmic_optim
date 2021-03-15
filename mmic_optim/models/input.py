from mmelemental.models.proc.base import ProcInput
from pydantic import Field
from typing import Optional, Dict, List

__all__ = ["OptimInput"]


class OptimInput(ProcInput):
    """ Basic model for energy minimization. """

    # Global fields
    max_steps: int = Field(
        None, description="Max number of optimization steps to perform."
    )
    step_size: float = Field(None, description="Step size for constant step marching.")
    step_size_units: Optional[str] = Field(
        None, description="Step size unit. Any unit supported by pint is allowed."
    )
    tol: Optional[float] = Field(
        None,
        description="Tolerance used to indicate when the optimization scheme has converged.",
    )
    tol_units: Optional[float] = Field(None, description="Tolerance unit e.g. kJ/mol.")

    # Algorithmic fields
    method: str = Field(
        None,
        description="Optimization method to use e.g. conjugate_gradient.",
    )

    # Geometric constraint fields
    bond_const: Optional[Dict[str, List[int]]] = Field(
        None,
        description="Specifies which bonds/angles/etc. in a molecule are constrained specified by their indices. E.g bond_const = {'solvent': [0,2,6]}.",
    )
    bond_const_method: Optional[str] = Field(
        None,
        description="Method used to constraint what's defined in 'constraints' e.g. LINCS or SHAKE.",
    )
    bond_const_tol: Optional[float] = Field(
        None, description="Tolerance used for constraint self-consistency."
    )
