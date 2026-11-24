from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Return the list of requirements, ignoring blank lines,
    comments, and editable installs like '-e .'
    """
    requirements = []
    with open(file_path, encoding="utf-8-sig") as file_obj:
        for line in file_obj:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("-e"):
                continue
            requirements.append(line)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Sharifa",
    author_email="sharifatumoro00@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)