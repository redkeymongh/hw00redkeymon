# mypackage

CPE 486/586, Homework 1, Question 12: elementary row operations on PyTorch
tensors, packaged as an installable subpackage `mypackage.matrix`.

## Layout

```
mypackage/
├── pyproject.toml
├── README.md
└── mypackage/
    ├── __init__.py
    └── matrix/
        ├── __init__.py
        └── elementary.py
```

## Functions (in `mypackage.matrix.elementary`)

- `rowswap(matrix, source, target)` — swap two rows of a tensor.
- `rowscale(matrix, row, factor)` — scale a row by any real factor.
- `rowreplacement(matrix, row1, row2, j, k)` — replace row1 with `j*row1 + k*row2`.
- `rref(matrix)` — reduced row echelon form, built from the three functions above.

## Local testing (before publishing)

```bash
cd mypackage/matrix
python elementary.py
```

This runs the `__main__` block, which reproduces the required test sequence
on

```
[[1, 3, 0, 0, 3],
 [0, 0, 1, 0, 9],
 [0, 0, 0, 1, -4]]
```


## Building and publishing to PyPI

```bash
python -m pip install --upgrade build twine
python -m build                 # creates dist/*.tar.gz and dist/*.whl
python -m twine upload dist/*   # uploads to PyPI (needs a PyPI account/token)
```

Remember to bump `version` in `pyproject.toml` every time you re-publish.

## Installing in Google Colab

```python
!pip install yourkeyword
from yourkeyword.matrix import elementary
```

## Publishing to GitHub

```bash
git init
git add .
git commit -m "Add matrix subpackage with elementary row operations"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```
