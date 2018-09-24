========================
Installation of Drivers
========================

The library, janusgraph-python can be installed either using PyPi or else can be build from the main repository. 
Currently, it is not yet hosted to PyPi, till version 1.0.0 is out, but you can clone the repository and build the
library yourself.

++++++++++++++++++++++++
Installation using PyPi
++++++++++++++++++++++++

.. code-block:: bash

    pip install janusgraph-python
    # This installs the latest version of JanusGraph-Python drivers. To install specific to JanusGraph version,
    # please use the following syntax

    pip install janusgraph-python==x.y.z
    # Where x.y.z is version number, corresponding to JanusGraph version you are using.
    # Please refer to compatibility matrix to get version compatible against each JanusGraph version

The JanusGraph client follows x.y.z version number, and according to [Semantic Versioning](https://semver.org/) z is
patch number. Hence, if a client is build using x.y against JanusGraph a.b.c, irrespective of `.z` change,
the client will remain compatible.

Example::
    
    Version 1.0.0 is compatible with JanusGraph 0.3.0. Meaning that 1.0.1/1.0.2/..1.0.x will all be compatible with
    JanusGraph 0.3.0

++++++++++++++++++++++++++++++++++++++++++++
Installation by building from repository
++++++++++++++++++++++++++++++++++++++++++++

A shell script has been created for easy install of the library. The script accepts following parameters:
    - -d: Default to true. Implies, if documentation is to be build.
    - -b: Defaults to true. Implies if library is to be build.
    - -i: Default to false. Implies if library is to be installed on local system.

If any of the defaults needs to be changed, the parameter needs to be specified explicitly while running the script.

Examples::
    .. code-block:: bash

    # If you want to build just the documentation, without the library.
    ./build.sh -b false

    # If you want to build just the library, and install it but aren't interested in building docs.
    ./build.sh -d false -i true

    # If you just want to build the library.
    ./build.sh -d false

    # And so on depending on your requirements.

**NOTE**: When install flag is set to true, it installs the library only to Global python environment, and
currently doesn't install to virtual environment.
