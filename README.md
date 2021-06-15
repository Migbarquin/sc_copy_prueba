# scDataCuration

## Installing the Jupyter Notebook envirnoment

How we install everything so that it is running...

## Set up conda environment

```
conda env create -n scdatacuration -f dependencies.yml
```

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

