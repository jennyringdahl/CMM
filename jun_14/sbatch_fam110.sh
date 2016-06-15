#!/bin/bash


# Run the script like this:
# sbatch <OPTIONS> sbatch_template.sh
# Where the OPTIONS are all of:
# -A g2015056 -t 2:00:00 -p core -n 3 --res=g2015056_05 -o my_job_name.out
#
# You may change the job name (-o my_job_name.out) to anything you like.

# Any line that starts with '# ' (dash followed by space) is a comment and will not be executed

# First add the modules needed for the program(s) your're about to run:
module load bioinfo-tools vcftools/0.1.8a tabix/0.2.6

# cd to the directory where the data is (of course, use your own user name):
cd /home/pbryant

# Then list the commands that you would like to run. 
# If you'd like to add more jobs, enter them on the following lines. 

for i in 22 do 
vcf-query -c 1526-02D,Co-1301,Co-1313,Co-1314 -r $i: -f '%CHROM\t%POS\t%REF\t%ALT[\t%GT]\n' /proj/b2011117/private/databases/table_annovar/WES294/WES294_annotated.vcf.gz>fam110_chr$i.txt
done

#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y
