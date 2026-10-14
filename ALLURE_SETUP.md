# Allure setup for StepikEducationPetshop

## Run the tests and collect Allure results

1. Activate the project's virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the required test credentials and checkout details are present in the local `.env` file. Do not commit `.env`.
4. Run:
   ```bash
   pytest -sv
   ```
   The `pytest.ini` file automatically clears and writes the latest result set to `allure-results/`.
5. Open the interactive report:
   ```bash
   allure serve allure-results
   ```

`allure-pytest` is a Python package and is already listed in `requirements.txt`. The `allure` command used to generate/open reports comes from a separate Allure Commandline installation. If your terminal cannot find `allure`, install Allure Commandline for your operating system and configure it in `PATH`.

## What was changed

- `pytest.ini`: sets the test discovery path and enables Allure result collection by default.
- `tests/test_*.py`: adds report titles, descriptions, feature/story labels, severity and readable business steps.
- `pages/*.py` and `base/base_class.py`: adds named Allure steps to meaningful page actions and checks.
- `base/base_class.py`: keeps local screenshot files and also attaches checkpoint screenshots to the report.
- `conftest.py`: attaches a screenshot and current URL when a test fails during its call phase.
- `.gitignore`: excludes generated Allure result and report folders.

## Important behavior

The current purchase scenario intentionally stops before final order submission. The submit call and final confirmation assertion remain commented out to avoid creating a real order while practicing automation. The Allure report describes the behavior that is actually enabled in the test; it does not claim that an order was submitted.
