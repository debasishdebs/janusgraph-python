
conda create --name tmpenv -y > nul

call activate tmpenv

COPY build.py docs/build.py

pip install pybuilder > nul
pip install sphinx > nul

sphinx-apidoc -o docs/ src/main/python/janusgraph_python

pyb_ sphinx_generate_documentation

cd docs

del build.py
del janusgraph_python*.rst
del modules.rst

call deactivate

conda env remove --name tmpenv -y > nul

pause