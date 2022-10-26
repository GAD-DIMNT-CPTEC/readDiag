# readDiag

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GAD-DIMNT-CPTEC/readDiag/HEAD)

**English:** the readDiag documentation is available [here](https://gad-dimnt-cptec.github.io/readDiag/).

O pacote ReadDiag foi concebido para ser uma ferramenta que possibilita o fácil acesso aos arquivos diagnósticos gerados pelo [Gridpoint Statistical Interpolation (GSI) system](https://github.com/NOAA-EMC/GSI). Existem duas formas distintas de acessar (ler) os arquivos diagnósticos do GSI por meio do ReadDiag. A primeira é por meio da classe `readDiag.py` diretamente no python e a segunda é diretamente no fortran usando como base o modulo `ReadDiagMod.f90`.

## Requerimentos

Para instalação no ambiente python alguns pacotes extras são necessários, assim será possível fazer algumas plotagens simples a partir do uso da classe readDiag. Os pré-requisitos principais são:

* basemap;
* cartopy;
* gcc;
* geopandas;
* geos;
* gfortran;
* matplotlib;
* numpy;
* pandas;
* proj4;
* pyproj;
* python (3.7.6);
* xarray.

Para facilitar a configuração de um ambiente Python para uso com o readDiag, utilize o arquivo `environment.yml` com o conda:

```
conda env create -f environment.yml
```

Caso não seja de interesse usar o pacote python, pode-se utilizar somente o modulo em fortran. Para tal, todas as dependências já estão inclusas no pacote. Porém, recomenda-se usar o compilador gfortran.

## Instalação

Maiores detalhes sobre a instalação podem ser vistas no arquivo `INSTALL.md`, no entanto, para a instalação no ambiente python faça o seguinte:

```
python setup.py install
```

**Nota:** para desisntalar o readDiag, dentro do ambiente conda onde o pacote está instalado, utilize o comando `pip uninstall gsidiag`.

## Uso

Veja o notebook Jupyter `readdiag_examples.ipynb` com vários exemplos de uso.

<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode" target="_blank"><img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" alt="CC-BY-NC-SA" width="100"/></a>
