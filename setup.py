"""
    CIJOE distribution package for 'example'
"""
import codecs
import glob
import os
from setuptools import setup


def read(*parts):
    """Read parts to use a e.g. long_description"""

    here = os.path.abspath(os.path.dirname(__file__))

    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as pfp:
        return pfp.read()


setup(
    name="cijoe-pkg-example",
    version="0.2.1",
    description="CIJOE: package for 'example'",
    long_description=read('README.rst'),
    author="Simon A. F. Lund",
    author_email="os@safl.dk",
    url="https://github.com/refenv/cijoe-pkg-example",
    license="Apache License 2.0",
    install_requires=[
        "cijoe (>=0.2.2)"
    ],
    zip_safe=False,
    data_files=[
        ("bin", glob.glob("bin/*")),

        ("share/cijoe/hooks", glob.glob("hooks/*")),
        ("share/cijoe/modules", glob.glob("modules/*.sh")),

        ("share/cijoe/envs", glob.glob("envs/*")),

        ("share/cijoe/testfiles", glob.glob("testfiles/*")),
        ("share/cijoe/testcases", glob.glob("testcases/*")),
        ("share/cijoe/testsuites", glob.glob("testsuites/*")),
        ("share/cijoe/testplans", glob.glob("testplans/*"))
    ],
    options={'bdist_wheel': {'universal': True}},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Text Processing",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Software Development :: Testing"
    ],
)
