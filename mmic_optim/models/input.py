from cmselemental.models.procedures import InputProc
from mmelemental.models.base import ProtoModel
from mmelemental.models import Molecule
from mmelemental.models.forcefield import ForceField
from pydantic import Field, validator
from typing import Optional, Dict, List, Tuple, Union

__all__ = ["InputOptim"]

class InputForces(ProtoModel):

    method: str = Field(..., description="The algorithm used to compute the force. e.g. PME")

    cutoff: Optional[float] = Field(None, description="The cut-off distance")

    cutoff_units: Optional[str] = Field("angstrom", description="The unit of cutoff distance")



class InputTraj(ProtoModel):

    geometry_freq: Optional[int] = Field(
        None, description="Every number of steps geometry are saved."
    )
    geometry_units: Optional[str] = Field(
        "angstrom",
        description="Units for atomic geometry. Defaults to Angstroms.",
        dimensionality=LENGTH_DIM,
    )
    velocities_freq: Optional[int] = Field(
        None,
        description="Save velocities every 'velocities_freq' steps.",
    )
    velocities_units: Optional[str] = Field(
        "angstrom/fs",
        description="Units for atomic velocities. Defaults to Angstroms/femtoseconds.",
        dimensionality=LENGTH_DIM / TIME_DIM,
    )
    forces_freq: Optional[int] = Field(
        None, description="Every number of steps velocities are saved."
    )
    forces_units: Optional[str] = Field(
        "kJ/(mol*angstrom)",
        description="Units for atomic forces. Defaults to KiloJoules/mol.Angstroms.",
        dimensionality=MASS_DIM * LENGTH_DIM / (SUBS_DIM * TIME_DIM ** 2),
    )
    freq: Optional[int] = Field(
        None,
        description="Every number of steps geometry, velocities, and/or forces are saved.",
    )



class InputOptim(InputProc):
    """Basic input model for energy minimization."""

    # System fields
    molecule: Dict[str, Molecule] = Field(
        ...,
        description="Molecular mechanics molecule object(s). See the :class:``Molecule`` class. "
        "Example: mol = {'ligand': Molecule, 'receptor': Molecule, 'solvent': Molecule}.",
    )
    forcefield: Dict[str, ForceField] = Field(
        ...,
        description='Forcefield object(s) or name(s) for every Molecule defined in "mol".',
    )
    boundary: Union[
        Tuple[str, str],
        Tuple[str, str, str, str],
        Tuple[str, str, str, str, str, str],
    ] = Field(
        ...,
        description="Boundary conditions in all dimensions e.g. (periodic, periodic) imposes periodic boundaries in 1D.",
    )
    cell: Optional[
        Union[
            Tuple[float, float],
            Tuple[float, float, float, float],
            Tuple[float, float, float, float, float, float],
        ]
    ] = Field(
        None,
        description="Cell dimensions in the form: ((xmin, ymin, ...), (xmax, ymax, ...))",
    )

    # I/O fields
    trajectory: Optional[Dict[str, InputTraj]] = Field(
        None,
        description="Trajectories to write for quantity 'key' every 'value' steps. E.g. {'geometry_freq': 10, 'velocities_freq': 100, 'forces_freq': 50} "
        "produces 3 trajectory objects storing positions every 10 steps, velocities, every 100 steps, and forces every 50 steps.",
    )

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

    # Forces parameters
    short_forces: Optional[InputForces] = Field(
        None, description="Schema model for computing short-range forces."
    )

    long_forces: Optional[InputForces] = Field(
        None, description="Schema model for computing long-range forces."
    )

    # Validators
    @validator("forcefield")
    def _valid_ff(cls, v, values):
        for name in values.get("molecule"):
            if name not in v:
                raise ValueError(f"{name} does not have a defined force field.")
        assert len(v) == len(values["molecule"]), (
            "Every molecule should have a single force field definition. "
            + f"{len(values['molecule'])} molecules defined using {len(v)} force fields."
        )
        return v

    @validator("cell")
    def _valid_cell(cls, v, values):
        assert len(v) == len(values.get("boundary"))
        return v
