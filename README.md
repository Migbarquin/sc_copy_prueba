# scDataCuration

## PanglaoDB

Process to download PanglaoDB data and raw data

1. Create the folder and place inside the file py_obtain_tsv.py
2. Run Panglao_obtain_tsv.sh

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

