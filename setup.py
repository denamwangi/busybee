from setuptools import setup

setup(
    name="BusyBee",
    version="1.0",
    py_modules=["busybee_cli"],
    install_requires=["Click"],
    entry_points="""
		[console_scripts]
		busybee_cli=busybee_cli:cli
	""",
)
