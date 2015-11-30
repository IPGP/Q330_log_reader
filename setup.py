from setuptools import setup

INSTALL_REQUIRES = [
    'obspy>=0.8.0']

setup(
    name="Q330_log_reader",
    version="0.0.1",
    description="Decode Quanterra Q330 digitizer log files using Obspy.",
    author="Sebastien Bonaime",
    author_email="bonaime@ipgp.fr",
    url="https://github.com/bonaime/Q330_log_reader",
    download_url="https://github.com/bonaime/Q330_log_reader.git",
    install_requires=INSTALL_REQUIRES,
    keywords=["Q330", "ObsPy", "Seismology", "LOG", "Quanterra","decode"],
    packages=["Q330_log_reader"],
    entry_points={
        'console_scripts':
            ['Q330_log_reader = Q330_log_reader:main'],
    },
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or " +
        "Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description="""\
A python script to decode Quanterra Q330 Digitizer clients log files using Obspy
"""
)