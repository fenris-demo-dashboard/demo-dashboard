"""Doit pipeline."""
import os
from typing import Generator, Optional

DOIT_CONFIG = {
    "default_tasks": [
        "python_dependencies",
        "flake8",
        "black",
        "pydocstyle",
        "pylint",
        "bandit",
        "mypy",
        "pytest",
    ],
    "cleanforget": True,
    "verbosity": 0,
}

doit_process_locations = {
    "python_directories": ["dashboard_pages", "dashboard_supplements"],
    "python_files": ["demo_dashboard.py"],
}
process_locations_list = []
for sublist in list(doit_process_locations.values()):
    for process_location in sublist:
        process_locations_list.append(process_location)


def task_python_dependencies() -> Generator:
    """Check that all dependencies are installed correctly."""
    log_file = ".doit.pip.log"
    yield {
        "name": "python_dependencies",
        "actions": [f"pip install -r requirements-dev.txt --log {log_file}"],
        "file_dep": ["requirements.txt"],
        "targets": [log_file],
        "clean": True,
    }


def task_black() -> Generator:
    """Check standardized code formatting."""
    for location in process_locations_list:
        yield {
            "name": location,
            "actions": [f"black --check {location}"],
            "file_dep": list_files(location),
            "task_dep": ["python_dependencies"],
        }


def task_flake8() -> Generator:
    """Check style consistency."""
    for location in process_locations_list:
        yield {
            "name": location,
            "actions": [f"flake8 --max-line-length 100 {location}"],
            "file_dep": list_files(location),
            "task_dep": ["python_dependencies"],
        }


def task_pydocstyle() -> Generator:
    """Check compliance with docstring conventions."""
    for location in process_locations_list:
        if location != "tests":
            yield {
                "name": location,
                "actions": [
                    f"pydocstyle --convention=numpy --match-dir='[^\.].*' {location}"
                ],
                "file_dep": list_files(location),
                "task_dep": ["python_dependencies"],
            }


def task_pylint() -> Generator:
    """Check for code errors and enforces a pythonic coding standard."""
    for location in process_locations_list:
        if location != "tests":
            yield {
                "name": location,
                "actions": [f"pylint --rcfile=setup.cfg {location}"],
                "file_dep": list_files(location) + ["setup.cfg"],
                "task_dep": ["python_dependencies"],
            }


def task_mypy() -> Generator:
    """Check static python types."""
    for location in process_locations_list:
        yield {
            "name": location,
            "actions": [f"mypy --config-file=setup.cfg {location}"],
            "file_dep": list_files(location) + ["setup.cfg"],
            "task_dep": ["python_dependencies"],
        }


def task_bandit() -> Generator:
    """Check for security issues."""
    for location in process_locations_list:
        yield {
            "name": location,
            "actions": [f"bandit {location}"],
            "file_dep": list_files(location),
            "task_dep": ["python_dependencies"],
        }


def task_pytest() -> dict:
    """Check that all tests are passing."""
    file_deps = []
    for path in process_locations_list:
        file_deps += list_files(path)

    return {
        "actions": ["coverage run -m pytest tests"],
        "file_dep": file_deps,
        "task_dep": ["python_dependencies"],
    }


def task_pytest_junit_report() -> dict:
    """Create a pytest report."""
    file_deps = []
    for path in process_locations_list:
        file_deps += list_files(path)

    return {
        "actions": [
            "coverage run --branch -m pytest -v --junitxml=report.xml",
            "coverage report -m",
        ],
        "file_dep": file_deps,
        "task_dep": ["python_dependencies"],
    }


def list_files(file_location: str, ignore_extensions: Optional[list] = None) -> list:
    """List all files found in a given directory.

    If the name of a python file is provided,
    then a list with that file name is returned.
    """
    if ignore_extensions is None:
        ignore_extensions = []

    if file_location[-2:] == "py":
        return [file_location]

    files_list = []
    for root, _, files in os.walk(file_location):
        for file in files:
            file = os.path.join(root, file)
            _, file_extension = os.path.splitext(file)
            if file_extension not in ignore_extensions:
                files_list.append(file)
    return files_list
