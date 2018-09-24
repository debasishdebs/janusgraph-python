# JanusGraph-Python
#### Python Client drivers for [JanusGraph](janusgraph.org) 

JanusGraph-Python is the Python drivers for connecting to JanusGraph. 
It extends Apache TinkerPop™'s [Gremlin-Python](http://tinkerpop.apache.org/docs/current/reference/#_gremlin_python) 
as its core dependency with additional support for JanusGraph-specific types and predicates.


The library has been tested with following Python versions:

    - [Python 3.4](https://www.python.org/download/releases/3.4.0/).
    - [Python 3.5](https://www.python.org/download/releases/3.5.0/).
    - [Python 3.6](https://www.python.org/download/releases/3.6.0/).
    
Once the required Python version is installed on system, the following requirements needs
to be fulfilled to start building the library. (**NOTE**: The following requirements aren't needed if 
installing the drivers from PyPi)

- VirtualEnv:
    ```
    pip install virtualenv
    ```
    
- PyBuilder:
    ```
    pip install pybuilder
    ```
        
**NOTE** : The above commands will download the latest version of libraries, and have been tested against the recent 
versions. 

Once above requirements are installed, use following commands to build library or building the docs.

- Building Library: You can build the library yourself to test out the functionality of library. Refer to 
[Building docs](BUILDING.md) for documentation on how to build the library.


- Installing the Library:
    
    - To install library using Pip (It is not yet hosted):
    
    ```bash
        # X is version number of JanusGraph Python client supported
        pip install janusgraph_python=X
    ```
    
    - To install library from tarball, once it is built:
     
     ```bash
        pip install target/dist/janusgraph_python/dist/janusgraph_python-X.tar.gz
        # X is the version number of library
     ```

## Community
JanusGraph-Python uses the same communication channels as JanusGraph in general. 
So, please refer to the 
[Community section in JanusGraph's main repository](https://github.com/JanusGraph/janusgraph#community) 
for more information about these various channels.


## Contributing
Please see 
[`CONTRIBUTING.md` in JanusGraph's main repository](https://github.com/JanusGraph/janusgraph/blob/master/CONTRIBUTING.md) 
for more information, including CLAs and best practices for working with GitHub.


## License

JanusGraph Python driver code is provided under the [Apache 2.0
license](APACHE-2.0.txt) and documentation is provided under the [CC-BY-4.0
license](CC-BY-4.0.txt). For details about this dual-license structure, please
see [`LICENSE.txt`](LICENSE.txt).
