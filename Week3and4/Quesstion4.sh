
#!/bin/bash

echo > Question4_Outputs.txt

for file in $(find ../ncbi_dataset/data/ -name 'GCA*fna*')

do

echo $file
echo $file >> Question4_Outputs.txt
python gene_finder1.py -f $file >> Question4_Outputs.txt

done
