# Arrebol

<br>

### Build Conda

Inicialmente é necessário instalar o [conda-build](https://docs.conda.io/projects/conda-build/en/latest/index.html) com o comando:

```bash
conda install conda-build
```

<br>

```bash
conda activate pablocarreira-py38
conda-build ./conda -c src/label/main # Funciona!
```

<br>

## GitActions: publicar pacotes no Conda

Adicionar converters

```bash
# convert package to other platforms
cd ~
platforms=( osx-64 linux-32 linux-64 win-32 win-64 )
find $HOME/conda-bld/linux-64/ -name *.tar.bz2 | while read file
do
    echo $file
    #conda convert --platform all $file  -o $HOME/conda-bld/
    for platform in "${platforms[@]}"
    do
       conda convert --platform $platform $file  -o $HOME/conda-bld/
    done
done
```


<br>

 Para fins de teste

```bash
conda create --name michel-py38 -c conda-forge -c michelmetran python=3.8 jupyter jupyterlab jupyter_contrib_nbextensions nb_conda nbstripout nbconvert=5.6.1 arrebol pandas requests nodejs tornado=5.1.1
```

<br>

**Referências**:

- https://www.asmeurer.com/conda-docs-test/docs/building/meta-yaml.html

- https://anaconda.org/michelmetran/dashboard

- https://docs.conda.io/projects/conda-build/en/latest/concepts/channels.html

- https://levelup.gitconnected.com/publishing-your-python-package-on-conda-and-conda-forge-309a405740cf

- https://www.youtube.com/watch?v=HSK-6dCnYVQ

- https://giswqs.medium.com/building-a-conda-package-and-uploading-it-to-anaconda-cloud-6a3abd1c5c52

- https://github.com/maxibor/conda-package-publish-action

- https://github.com/rfun/tethysapp-servicetest/blob/master/.github/workflows/main.yml
