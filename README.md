# scDataCuration

## Set up conda environment from scratch

To find packages we want to install, we can check which Conda packages are available in 
https://anaconda.org/.

Create the environment named scdatacuration:

```
conda create -n scdatacuration

```

Activate the environment:

```
conda activate scdatacuration
```

Now you can install packages (here pandas):

```
conda install -c conda-forge pandas
```

Deactivate the environment:

```
conda deactivate
```

Export the software currently installed in the environment named scdatacuration into the dependency files.

```
conda env export --name scdatacuration > dependencies.yml
```

## Set up conda environment from dependencies.yml

If you want to install the environment including already all dependencies simply run:

```
conda create -n scdatacuration -f dependencies.yml
```

## PanglaoDB

Process to download PanglaoDB data and raw data

1. Create the folder and place inside the file py_obtain_tsv.py
2. Run Panglao_data_download.sh
3. Read_tsv.py to read the tsv file

## Installing the Jupyter Notebook envirnoment

How we install everything so that it is running...


## Activate the "vir" environment on the shared compute cluster
```
conda activate scdatacuration
```

## Run Jupyter notebooks

```
python -m ipykernel install --user --name vir --display-name "Python (vir)"
jupyter notebook
```
Select `Python (vir)` as the kernel.

