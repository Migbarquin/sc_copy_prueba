
#path to folder where ypu can download panglaodb databases
#inside that folder, the file python_obtain_tsv.py has to be
cd ~/Documents/PhD/DATABASES/panglaodb

wget https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/metadata.txt
wget https://raw.githubusercontent.com/oscar-franzen/PanglaoDB/master/data/clusters_to_number_of_cells.txt

python py_obtain_tsv.py
