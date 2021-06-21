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

If there exists already an environment with this name, we can manually delete it first.

```
conda remove --name scdatacuration --all
```

If you want to install the environment including already all dependencies simply run:


```
conda create -n scdatacuration -f dependencies.yml
```

## PanglaoDB

Process to download PanglaoDB data and raw data

1. Getting metadata from https://panglaodb.se/:
```
wget https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/metadata.txt
wget https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/clusters_to_number_of_cells.txt
```
The other option is run the file Panglao_data_download.sh (replacing the directory with the selected one).

2. Creation of tsv file
In your python notebook:
```
import pandas as pd
df = pd.read_csv('clusters_to_number_of_cells.txt', header=None, delimiter = ",")
df.columns = ["SRA accession", "SRS accession", "Cluster index", "Number of cells"]
l = df.groupby('SRS accession')['Number of cells'].sum()
df2 = pd.DataFrame(data=l)
df3 = pd.read_csv('metadata.txt', header=None, delimiter = ",")
df3.columns = ["SRA accession", "SRS accession", "Tissue origin of the sample", "scRNA-seq protocol","Species","Sequencing instrument","Number of expressed genes","Median number of expressed genes per cell","Number of cell clusters in this sample","Is the sample from a tumor? (1 true otherwise false)","Is the sample from primary adult tissue?","Is the sample from a cell line?"]
df4 = pd.merge(left=df3, right=df2, left_on='SRS accession', right_on='SRS accession')
df4.to_csv("PanglaoDB", sep="\t", index=False)
```
The ipynb file is already included inside DataFolder folder

3. Open tsv file
In your python notebook:
```
import pandas as pd
panglao = pd.read_csv('PanglaoDB', sep='\t')
panglao
```
Example of selection of samples:
```
panglao.loc[panglao['Species'] == "Homo sapiens"]
```
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
