Virtualenv Update Path
====

This modulke provides a cli interface to use for adding extra folders to the ``PATH`` environment variable associated with the targeted environment variable. This has the effect of extending the list of folder included upon environment activation, and enables virtualenvironments to be used as limited user profiles.

The module functions by appending a path override to the init scripts associated with the environment in question. 


Installation

This module is pip installable:

.. code-block:: bash

    pip install virtualenv-update-path

Usage

For updating all supported update paths

.. code-block:: bash
    virtualenv-update-path "<path to virtualenv Script folder>" "<folder to include in path>""