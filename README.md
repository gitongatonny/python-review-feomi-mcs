# python-review-feomi-mcs

Python review assignment for **FEOMI** (Electives, Semester 1) on the MSc Cyber Security Engineering programme at Óbuda University.

The work lives in a single notebook, [`python-review.ipynb`](python-review.ipynb), with outputs kept so it can be read without running it.

## Contents

| Lab | Topic |
|-----|-------|
| 2.2 | `print()` exercises, deliberate syntax/name errors, literals and basic types |
| 2.3 | Variables and f-strings (apples exercise + personal experimentation) |
| 2.4 | Miles/kilometres conversion |
| 2.6 | Variables, naming rules, comments, mini-tests (a–f) |
| 2.7 | Operators, control flow, lists, references vs copies, functions (Tables 1–4) |

## Running it

```bash
# Install Jupyter (any recent Python 3)
pip install jupyterlab

# Open the notebook
jupyter lab python-review.ipynb
```

Lab 2.7 task 1 uses `input()`, so run that cell interactively.

## Repository history

Each lab was added as its own commit on a `lab-<n>` branch and merged through a pull request, so `git log --first-parent` reads as one entry per lab.
