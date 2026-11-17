#!/usr/bin/env bash
set -euo pipefail
export PATH="/opt/python/cp39-cp39/bin:$PATH"
python -m pip install build
python -m build --sdist --outdir dist
mkdir -p /tmp/readdiag-wheels
python -m pip wheel --no-deps --wheel-dir /tmp/readdiag-wheels dist/*.tar.gz
auditwheel repair --plat manylinux2014_x86_64 --wheel-dir dist /tmp/readdiag-wheels/*.whl
