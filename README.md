# Optimization Component

[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_optim/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_optim/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_optim/branch/master/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_optim/branch/main)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic_optim.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic_optim/context:python)

This is part of the [MolSSI](http://molssi.org) Molecular Mechanics Interoperable Components ([MMIC](https://github.com/MolSSI/mmic)) project. This package provides a strategy component for running energy minimization based on a force field.

## Preparing Input

```python
# Import molecule data model
from mmelemental.models.molecule import Molecule

# Construct molecule object
solute = Molecule.from_file(path_to_file)
solvent = Molecule.from_file(path_to_file)

# Construct input data model from molecule object
inop = {
    "mol":{
        "solute": solute, "solvent": solvent
    }, 
    nsteps=1e4
}
```

## Running energy minimization

```python
# Import generic component for running energy minimization
from mmic_optim.components import OptimComponent

# Run minimization
outop = OptimComponent.compute(inop)
```

## Extracting output
```python
pot_energy = output.observables["pot_energy"]
...
```

### Copyright

Copyright (c) 2021, Andrew Abi-Mansour


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.
