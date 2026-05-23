# 📘 Assignment: Testing & Continuous Integration (CI)

## 🎯 Objective

Introduce unit testing with `pytest`, simple mocking, and continuous integration using GitHub Actions to automatically run tests on push and pull requests.

## 📝 Tasks

### 🛠️ Write Unit Tests

#### Description

Create unit tests for provided functions using `pytest`. Ensure tests are deterministic and cover edge cases.

#### Requirements
Completed program should:

- Include a `tests/` directory with pytest test modules
- Provide tests that cover normal and edge cases for each function in the starter code
- Use assertions to validate behavior; mock external calls if present

### 🛠️ Measure Test Coverage

#### Description

Run tests with coverage measurement and ensure a minimum coverage threshold is met.

#### Requirements
Completed program should:

- Include `pytest` and `coverage` in `requirements.txt`
- Provide a command to run tests with coverage (example below)
- Aim for at least 80% coverage for the starter code

### 🛠️ Configure CI Workflow

#### Description

Add a GitHub Actions workflow that runs tests and reports results on push and pull requests.

#### Requirements
Completed program should:

- Include a workflow file under `.github/workflows/ci.yml`
- Install dependencies and run `pytest` on multiple Python versions
- Fail the CI run when tests fail

## ▶️ Try it locally

Run the tests locally with:

`pip install -r requirements.txt`

`pytest --maxfail=1 -q`

## 📂 Files included

- `starter-code.py` — functions to test
- `tests/test_core.py` — example tests
- `requirements.txt` — test/runtime dependencies
- `.github/workflows/ci.yml` — CI workflow definition
