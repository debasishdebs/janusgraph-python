#!/usr/bin/env bash

# Copyright 2018 JanusGraph Python Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Defaults
docs=true
build=true
install=false
ENV_NAME=tempENV

while getopts ":d:b:i:" opt; do
  case "${opt}" in
    d)
      docs=$OPTARG
      ;;
    b)
      build=$OPTARG
      ;;
    i)
      install=$OPTARG
      ;;
    \?)
      echo "Usage $0 -d [Build Docs?] -b [Build Lib?] -i [Install Lib?]"
      exit 1
      ;;
  esac
done

if [ -z "${1:-}" ]; then
  echo "Usage "$(basename "$0")" -d [Build Docs?] -b [Build Lib?] -i [Install Lib?]\n"
  echo "Building with defaults $0 -d true -b true -i false"
fi

pip install virtualenv

virtualenv "${ENV_NAME}"

# Installing Pre requisites
chmod +x before-script.sh
./before-script.sh "${ENV_NAME}"

if [ "${docs}" == "true" ]
then
  echo "Building documentation"
  chmod +x build-docs.sh
  ./build-docs.sh "${ENV_NAME}"
fi

if [ "${build}" == "true" ]
then
  echo "Building library"
  chmod +x build.sh
  ./build-library.sh "${ENV_NAME}"
fi

if [ "${install}" == "true" ]
then
  echo "Installing library"
  # Install the library
  python -m pip install target/dist/janusgraph_python/dist/janusgraph_python-*.tar.gz
fi

# Remove all files for temp environment, as that is already deactivated
rm -rf "${ENV_NAME}"