# Building JanusGraph client for Python

- Building Library:
        
    - To build the library, run the following command:
        ```
         pyb (On Unix machines)
         pyb_ (On Windows machines)
         ```
         
    - To install the library (after Building library):
        ```bash
        pip install target/dist/janusgraph_python/dist/janusgraph_python-X.tar.gz
        # X is the version number of library
        ```
        
    - To install library using Pip (It is not yet hosted):
        ```bash
        # X is version number of JanusGraph Python client supported
        pip install janusgraph_python=X
        ```
       
    - To build the docs for drivers: The docs are currently being built using 
    [Sphinx](http://www.sphinx-doc.org/en/1.5/tutorial.html). Scripts are created to make documentation generation 
    easier:
        ```bash
        # For Unix systems
        ./build-docs-standalone.sh
        # For Windows systems
        build-docs.bat
        ```
    
    - If above steps seem complicated to you, then a shell script has been created to take care of your needs :-)
    The script works on Unix and Windows machine, though needs a CLI like Git bash (On Windows)
    
    The shell script accepts following parameters:
    - -d: Default to true. Implies, if documentation is to be build.
    - -b: Defaults to true. Implies if library is to be build.
    - -i: Default to false. Implies if library is to be installed on local system.
    
    If any of the defaults needs to be changed, the parameter needs to be specified explicitly while running the script.
    
     - If you want to build just the documentation, without the library.
        ```bash
        ./build.sh -b false
        ```
        
     - If you want to build just the library, and install it but aren't interested in building docs.
        ```bash
        ./build.sh -d false -i true
        ```
        
     - If you just want to build the library.
        ```bash
        ./build.sh -d false
        ```
        
     - And so on depending on your requirements.

Once done, you can see the built HTML files under `docs/_build/index.html` directory.