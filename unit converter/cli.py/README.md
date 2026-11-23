# CLI.PY

The `cli.py` is a terminal-based wrapper for the unit converter program that can be run from your terminal or command prompt. The `cli.py` program has a different interface from `unit_converter.py`, mainly due to its terminal-based interface. This README offers instructions, commands, and installation guides on how to use the `cli.py` program. 

*Both `cli.py` and `unit_converter.py` are different wrappers with different interfaces and instructions. Both still depend on `converter.py`.*

## INSTALLATION

To install `cli.py`, you need `cli.py` and `cliconverter.py` installed. For the installation guide, follow the steps below.

Why download `cliconverter.py`? This file is a dependency used by `cli.py` and `unit_converter.py`. It is required to be installed. While you can install both programs independently, it won't work because they need the `cliconverter.py` dependency. `cli.py` and `unit_converter.py` are wrappers for the program.

You must have Python 3.10 and Python 3 installed on your system. You also need a terminal or a command prompt.

Install the repository by cloning it with Git or install it as a ZIP folder.

After installation, both `cli.py` and `unit_converter.py` require `cliconverter.py` for `cli.py` and `mainconverter.py` for `unit_converter.py` to be in the same folder. For your convenience, each wrapper includes its dependency in its folder. Reminder: the dependency is named differently for each wrapper. For example, `cliconverter.py` is for `cli.py`, and `mainconverter.py` is for `unit_converter.py`

Upon installation, run `cli.py` with Python 3 or Python, depending on your system. It will shortly launch a terminal, and the program is ready.

## INSTRUCTIONS

The program uses the format `python3 cli.py <value> <from_unit> <to_unit>` to convert units. In order to convert your units, you must add your numerical value to <value>, add your initial unit to <from_unit>, and put your desired unit into <to_unit>. After that, you must press Enter in order to perform the calculation. After calculating, the results will appear shortly after.

**Below is the list of commands you can enter to help you with converting units:**

`python3 cli.py <value> <from_unit> <to_unit>` **(FORMAT)**

`python3 cli.py --list`

`python3 cli.py -h`

These provide more information when using the program, offering a list of units, measurements, and the format of the program.
