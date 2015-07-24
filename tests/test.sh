#!/bin/sh

BUILD_IMAGE='millitest'
BASEDIR=$(dirname $0)

docker build -t ${BUILD_IMAGE} ${BASEDIR}/..

docker run ${BUILD_IMAGE} python -m unittest tests
