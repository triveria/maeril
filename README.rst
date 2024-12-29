maeril
======

Ensemble of Random Tools
------------------------

Maeril is a versatile toolkit designed to provide a collection of random utilities.

Contents
--------

- `Installation`_
- `Usage`_
  - `Commands`_
  - `Examples`_
- `License`_


Installation
------------

Follow these steps to install maeril:

.. code-block:: shell

    pip install maeril

Ensure you have Python 3.7 or higher installed on your system.
It's recommended to use a virtual environment to manage dependencies.

Usage
-----

Maeril provides a command-line interface with various commands to perform different tasks.
Below are the available commands and examples to help you get started.

Commands
~~~~~~~~

Maeril offers the following commands:

.. code-block:: shell

    maeril prompt <input_path>
    maeril dump [FILE_NAME] --list

- **prompt**: Generate prompt from prompt.md template.
- **dump**: Copies a specified file from the `dump_files` directory to the current working directory or lists all available dump files.

Examples
~~~~~~~~

Here are some examples demonstrating how to use maeril effectively:

.. code-block:: shell

    # Example of using the prompt command to process an input file
    maeril prompt example_input.md

    # Example of listing all available dump files
    maeril dump --list

    # Example of dumping a prompt template
    maeril dump prompt.md

License
-------

Maeril is licensed under the MIT License.
See the `LICENSE`_ file for more details.
