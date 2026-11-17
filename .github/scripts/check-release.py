"""Check version consistency before building or publishing a release."""
import ast
import os
from pathlib import Path

setup = ast.parse(Path('setup.py').read_text())
call = next(n for n in ast.walk(setup) if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name) and n.func.id == 'setup')
version = next(ast.literal_eval(k.value) for k in call.keywords if k.arg == 'version')
module = ast.parse(Path('gsidiag/__init__.py').read_text())
module_version = next(ast.literal_eval(n.value) for n in module.body
                      if isinstance(n, ast.Assign)
                      and any(isinstance(t, ast.Name) and t.id == '__version__'
                              for t in n.targets))
assert version == module_version, 'setup.py and gsidiag.__version__ differ'
for filename in ['requirements.txt', 'environment.yml']:
    assert f'readDiag=={version}' in Path(filename).read_text(), filename
assert f'version: {version}' in Path('CITATION.cff').read_text(), 'CITATION.cff'
tag = os.environ.get('RELEASE_TAG', '')
if tag:
    assert tag == f'v{version}', f'Tag {tag!r} must match v{version}'
print(f'Validated readDiag {version}' + (f' ({tag})' if tag else ' (build-only test)'))
