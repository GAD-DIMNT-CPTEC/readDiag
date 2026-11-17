# Publicação no PyPI

O workflow `.github/workflows/publish-pypi.yml` publica no PyPI quando uma
release estável é publicada no GitHub. Rascunhos e pré-releases não publicam.
A execução manual em Actions apenas compila e testa: não envia ao PyPI.

## Configuração inicial

Em https://pypi.org/manage/project/readdiag/settings/publishing/, adicione um
Trusted Publisher do GitHub com estes valores:

- Owner: `GAD-DIMNT-CPTEC`
- Repository: `readDiag`
- Workflow: `publish-pypi.yml`
- Environment: `pypi`

O workflow usa o environment `pypi` do GitHub e autenticação OIDC. Não é
necessário cadastrar um token PyPI nos secrets do repositório.

## Nova versão

1. Atualize a versão em `setup.py`, `gsidiag/__init__.py`, `requirements.txt`,
   `environment.yml` e `CITATION.cff`, incluindo a data de lançamento.
2. Envie as alterações ao GitHub e execute **Publish to PyPI > Run workflow**
   para validar a compilação e os testes antes do lançamento.
3. Crie uma tag no formato `vX.Y.Z` no commit validado e publique a release
   correspondente no GitHub, descrevendo as alterações desde a tag anterior.
4. Aguarde o job `publish` concluir e confirme a versão no PyPI antes de
   anunciar que ela está disponível para instalação.

A publicação gera uma distribuição fonte e um wheel CPython 3.9 para Linux
x86_64 (manylinux2014). O wheel é compilado a partir da distribuição fonte;
a instalação, importação e renderização de um mapa são testadas antes do envio.
Outras plataformas dependem da compilação do pacote fonte.

Se houver falha antes do upload, corrija a configuração e reexecute o workflow
quando aplicável. Se o PyPI já recebeu arquivos, verifique o que foi publicado:
versões publicadas não podem ser sobrescritas. Não reutilize a tag para outro
conteúdo após a publicação no PyPI.
