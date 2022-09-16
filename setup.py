import os
import pathlib

from setuptools import setup

###############################################################################
#                             Dependency Loading                              #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


def req_file(filename: str, folder="requirements"):
    """Loading requirement files.
    :param filename name of requirements file
    :param folder where requirements are specified
    """
    with open(os.path.join(folder, filename), encoding='utf-8') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters
    # Example: `\n` at the end of each line
    return [x.strip() for x in content]


requirement_files = [
    "requirements.txt",
    "rasa-requirements.txt",
    "nemo-requirements.txt",
    "recording-requirements.txt"
]

install_requires = []
for file in requirement_files:
    install_requires.append(req_file(file))

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

###############################################################################

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    name='MIMOSA',
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version='0.1.0',    # Required
    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description='Multimodal Smart Home Assistance',
    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,
    long_description_content_type="text/markdown",

    author='Tim Dilger',
    author_email='tdilger@mailbox.org',
    # TODO add license
    license='undefined',
    install_requires=install_requires,
    packages=['recording', 'RASA', 'NeMo', 'bco'],
    zip_safe=False,
)
