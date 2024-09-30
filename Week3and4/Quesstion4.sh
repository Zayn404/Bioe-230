
#!/bin/bash

echo > gene_finder_14.txt

for file in $(find ../ncbi_dataset/data/ -name 'GCA*fna*')

do

echo $file
echo $file >> gene_finder_14.txt
python gene_finder1.py -f $file >> gene_finder_14.txt

done
