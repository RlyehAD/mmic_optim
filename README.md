mmic_optim
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/REPLACE_WITH_OWNER_ACCOUNT/mmic_optim/workflows/CI/badge.svg)](https://github.com/REPLACE_WITH_OWNER_ACCOUNT/mmic_optim/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/mmic_optim/branch/master/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/mmic_optim/branch/master)

# Optimization Component

## Temporary installation

```bash
pip install . -r requirements

git clone https://github.com/MolSSI/mmic
cd mmic && pip install . && cd .. && rm -rf mmic

git clone https://github.com/MolSSI/mmelemental         
cd mmelemental && pip install . && cd .. && rm -rf mmelemental

pytest mmic_optim/tests
```

## Preparing Input

```python
# Import molecule data model
from mmelemental.models.molecule import Molecule

# Construct molecule object
solute = Molecule.from_file(path_to_file)
solvent = Molecule.from_file(path_to_file)

# Import optimization data model
from mmic_optim.models import OptimInput

# Construct input data model from molecule object
input = OptimInput(
    mol={"solute": solute, "solvent": solvent}, nsteps=1e4, engine="openmm"
)
```

## Running energy minimization with NAMD component

```python
# Import generic component for running energy minimization
from mmic_optim.components import OptimComponent

# Run minimization
output = OptimComponent.compute(input)

# Extract potential energy from output
pot_energy = output.observables.pot_energy
```

### Copyright

Copyright (c) 2021, Andrew Abi-Mansour


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.
