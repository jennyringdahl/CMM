for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y
do
echo -e CHROM'\t'POS'\t'REF'\t'ALT'\t'1526-02D '\t'Co-1301 '\t'Co-1313 '\t'Co-1314>fam110_chr$i.txt
vcf-query -c 1526-02D,Co-1301,Co-1313,Co-1314 -r $i: -f '%CHROM\t%POS\t%REF\t%ALT[\t%GT]\n' /proj/b2011117/private/databases/table_annovar/WES294/WES294_annotated.vcf.gz >> fam110_chr$i.txt
done
