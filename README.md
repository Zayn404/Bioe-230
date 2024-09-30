# Bioe-230
[almualzm@login509-02-l ~]$ cd HW3
[almualzm@login509-02-l HW3]$ git clone https://github.com/Zayn404/Bioe-230.git
Cloning into 'Bioe-230'...

(gnome-ssh-askpass:897731): Gtk-WARNING **: 13:41:46.671: cannot open display:
error: unable to read askpass response from '/usr/libexec/openssh/gnome-ssh-askpass'
Username for 'https://github.com': zainabmmm1154@gmail.com

(gnome-ssh-askpass:898237): Gtk-WARNING **: 13:42:52.776: cannot open display:
error: unable to read askpass response from '/usr/libexec/openssh/gnome-ssh-askpass'
Password for 'https://zainabmmm1154@gmail.com@github.com':
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (7/7), 15.99 MiB | 14.08 MiB/s, done.
[almualzm@login509-02-l HW3]$ ls
Bioe-230
[almualzm@login509-02-l HW3]$ cd Bioe-230
[almualzm@login509-02-l Bioe-230]$ ls
ncbi_dataset.tsv  ncbi_dataset.zip  README.md
[almualzm@login509-02-l Bioe-230]$ unzip ncbi_dataset.zip
Archive:  ncbi_dataset.zip
replace README.md? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: README.md
  inflating: ncbi_dataset/data/data_summary.tsv
  inflating: ncbi_dataset/data/assembly_data_report.jsonl
  inflating: ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000007125.1/GCF_000007125.1_ASM712v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000008545.1/GCF_000008545.1_ASM854v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000008565.1/GCF_000008565.1_ASM856v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000008625.1/GCF_000008625.1_ASM862v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000008725.1/GCF_000008725.1_ASM872v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000006745.1/GCF_000006745.1_ASM674v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000006825.1/GCF_000006825.1_ASM682v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000006865.1/GCF_000006865.1_ASM686v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000008605.1/GCF_000008605.1_ASM860v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000008785.1/GCF_000008785.1_ASM878v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic.fna
  inflating: ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic.fna
  inflating: ncbi_dataset/data/GCF_000008525.1/GCF_000008525.1_ASM852v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000008745.1/GCF_000008745.1_ASM874v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000027305.1/GCF_000027305.1_ASM2730v1_genomic.fna
  inflating: ncbi_dataset/data/GCF_000091085.2/GCF_000091085.2_ASM9108v2_genomic.fna
  inflating: ncbi_dataset/data/dataset_catalog.json
  inflating: md5sum.txt
[almualzm@login509-02-l Bioe-230]$ ls
md5sum.txt  ncbi_dataset  ncbi_dataset.tsv  ncbi_dataset.zip  README.md
[almualzm@login509-02-l Bioe-230]$ cd ncbi_dataset
[almualzm@login509-02-l ncbi_dataset]$ ls
data
[almualzm@login509-02-l ncbi_dataset]$ cd data
[almualzm@login509-02-l data]$ ls
assembly_data_report.jsonl  GCA_000008625.1  GCF_000008545.1
dataset_catalog.json        GCA_000008725.1  GCF_000008565.1
data_summary.tsv            GCA_000008745.1  GCF_000008605.1
GCA_000006745.1             GCA_000008785.1  GCF_000008625.1
GCA_000006825.1             GCA_000027305.1  GCF_000008725.1
GCA_000006865.1             GCA_000091085.2  GCF_000008745.1
GCA_000007125.1             GCF_000006745.1  GCF_000008785.1
GCA_000008525.1             GCF_000006825.1  GCF_000027305.1
GCA_000008545.1             GCF_000006865.1  GCF_000091085.2
GCA_000008565.1             GCF_000007125.1
GCA_000008605.1             GCF_000008525.1
## Q3
# Extract the relevant data:
[almualzm@login509-02-l data]$ cut -f 1,11 data_summary.tsv > size.tsv
# The smallest genome:
[almualzm@login509-02-l data]$ tail -n +2 size.tsv | sort -t$'\t' -k2 -n | head -n 1
>> Chlamydia trachomatis D/UW-3/CX 1042519                                          
# The largest genome:
[almualzm@login509-02-l data]$ tail -n +2 size.tsv | sort -t$'\t' -k2 -n | tail -n 1
>> Vibrio cholerae O1 biovar El Tor str. N16961    4033464
# Outputting Only the Genome Sizes- Smallest
[almualzm@login509-02-l data]$ cat data_summary.tsv | awk -F '\t' 'NR > 1 {print $10}' | sort -n | head -n 1
>> 1042519
# Outputting Only the Genome Sizes- Largest
[almualzm@login509-02-l data]$ cat data_summary.tsv | awk -F '\t' '{print $10}' | sort -n | tail -n 1
>> 2961149

## Q4
# Checking the names to verify the numerical output:
[almualzm@login509-02-l data]$ cut -f 1 data_summary.tsv | grep -E 'c.*c'
Organism Scientific Name
Pasteurella multocida subsp. multocida str. Pm70
Lactococcus lactis subsp. lactis Il1403
Helicobacter pylori 26695
Deinococcus radiodurans R1 = ATCC 13939 = DSM 20539
Helicobacter pylori J99
Pasteurella multocida subsp. multocida str. Pm70
Lactococcus lactis subsp. lactis Il1403
Helicobacter pylori 26695
Deinococcus radiodurans R1 = ATCC 13939 = DSM 20539
Helicobacter pylori J99
# Noticed there are duplicates, code to include uniq only
[almualzm@login509-02-l data]$ tail -n +2 data_summary.tsv | cut -f 1 | grep
 -i "c.*c" | sort | uniq
Chlamydia pneumoniae CWL029
Chlamydia trachomatis D/UW-3/CX
Deinococcus radiodurans R1 = ATCC 13939 = DSM 20539
Helicobacter pylori 26695
Helicobacter pylori J99
Lactococcus lactis subsp. lactis Il1403
Pasteurella multocida subsp. multocida str. Pm70
[almualzm@login509-02-l data]$ tail -n +2 data_summary.tsv | cut -f 1 | grep
 -i "c.*c" | grep -vi "coccus" | sort | uniq
Chlamydia pneumoniae CWL029
Chlamydia trachomatis D/UW-3/CX
Helicobacter pylori 26695
Helicobacter pylori J99
Pasteurella multocida subsp. multocida str. Pm70
# Numerical Outputs
[almualzm@login509-02-l data]$ tail -n +2 data_summary.tsv | cut -f 1 | grep -i "c.*c" | sort | uniq | wc -l
>> 7
[almualzm@login509-02-l data]$ tail -n +2 data_summary.tsv | cut -f 1 | grep -i "c.*c" | grep -vi "coccus" | sort | uniq | wc -l
>> 5
## Q5
[almualzm@login509-02-l data]$ find . -name "*.fna" -size +3M | wc -l
>> 6
