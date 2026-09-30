# python-review-feomi-mcs

Python review assignment for **FEOMI** (Foundations and Efficient Operation of Modern Infrastructure), an elective in Semester 1 of the MSc Cyber Security Engineering programme at Óbuda University.

**Lecturer:** Dr. Alwahab Dhulfiqar Zoltan

The work lives in [`python-review.ipynb`](python-review.ipynb), with outputs kept so it can be read without running it. [`python-review.py`](python-review.py) is a plain-script copy (VS Code / Spyder `# %%` cell format); the notebook is the source of truth.

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

### Alternative: VS Code with the Jupyter extension

1. Install [VS Code](https://code.visualstudio.com/) and the **Python** and **Jupyter** extensions (both from Microsoft).
2. Open this folder and open `python-review.ipynb`.
3. Click **Select Kernel** (top right) and pick a Python 3 interpreter.
4. Use **Run All**, or run cells one at a time with `Shift+Enter`.

The `python-review.py` copy also works: its `# %%` markers show a **Run Cell** button above each cell and run in the Jupyter Interactive Window.

Lab 2.7 task 1 uses `input()`, so run that cell interactively.
