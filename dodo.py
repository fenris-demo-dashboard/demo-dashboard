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

python_directories = ["demo_api_pages", "demo_supplements", "demo_app.py"]


def task_python_dependencies():
    log_file = ".doit.pip.log"
    return {
        "actions": [f"pip install -r requirements-dev.txt --log {log_file}"],
        "file_dep": ["requirements.txt", "requirements-dev.txt"],
        "targets": [log_file],
        "clean": True,
    }


def task_black():
    for directory in python_directories:
        yield {
            "name": directory,
            "actions": [f"black --check {directory}"],
            "file_dep": list_files(directory),
            "task_dep": ["python_dependencies"],
        }


def task_flake8():
    for directory in python_directories:
        yield {
            "name": directory,
            "actions": [f"flake8 --max-line-length 100 {directory}"],
            "file_dep": list_files(directory),
            "task_dep": ["python_dependencies"],
        }


def task_pydocstyle():
    for directory in python_directories:
        if directory != "tests":
            yield {
                "name": directory,
                "actions": [f"pydocstyle --convention=numpy {directory}"],
                "file_dep": list_files(directory),
                "task_dep": ["python_dependencies"],
            }


def task_pylint():
    for directory in python_directories:
        if directory != "tests":
            yield {
                "name": directory,
                "actions": [f"pylint {directory}"],
                "file_dep": list_files(directory),
                "task_dep": ["python_dependencies"],
            }


def task_mypy():
    return {
        "actions": ["mypy heimdal"],
        "file_dep": list_files("heimdal") + ["setup.cfg"],
        "task_dep": ["python_dependencies"],
    }


def task_bandit():
    return {
        "actions": ["bandit heimdal"],
        "file_dep": list_files("heimdal"),
        "task_dep": ["python_dependencies"],
    }


def task_pytest():
    file_deps = []
    for path in python_directories:
        file_deps += list_files(path)

    return {
        "actions": ["coverage run -m pytest tests"],
        "file_dep": file_deps,
        "task_dep": ["python_dependencies"],
    }


def task_pytest_junit_report():
    file_deps = []
    for path in python_directories:
        file_deps += list_files(path)

    return {
        "actions": [
            "coverage run --source=heimdal --branch -m pytest -v --junitxml=report.xml",
            "coverage report -m",
        ],
        "file_dep": file_deps,
        "task_dep": ["python_dependencies"],
    }


def list_files(directory, ignore_extensions=None):
    import os

    if ignore_extensions is None:
        ignore_extensions = []

    fs = []
    for root, directories, files in os.walk(directory):
        for file in files:
            file = os.path.join(root, file)
            filename, file_extension = os.path.splitext(file)
            if file_extension not in ignore_extensions:
                fs.append(file)
    return fs
