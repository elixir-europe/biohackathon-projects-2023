### Real data

- Install requirements

```
 sudo apt-get install pdfjam texlive-extra-utils samtools bedtools bcftools

```
- Get reference sequence

```
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa

```

- Get human sequence data from  https://www.internationalgenome.org/data-portal/sample for example [HG01504](https://www.internationalgenome.org/data-portal/sample/HG01504)

#### BAM files

```
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000_genomes_project/data/IBS/HG01504/alignment/HG01504.alt_bwamem_GRCh38DH.20150718.IBS.low_coverage.cram


```

- Convert to BAM

```
samtools view -T GRCh38_full_analysis_set_plus_decoy_hla.fa  -b -o HG01504.alt_bwamem_GRCh38DH.20150718.IBS.low_coverage.bam HG01504.alt_bwamem_GRCh38DH.20150718.IBS.low_coverage.cram

```
- Find coordinates for TP53 from Ensembl https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141510;r=17:7661779-7687538


- Extract region

```
samtools view -b HG01504.alt_bwamem_GRCh38DH.20150718.IBS.low_coverage.bam 17:7565097-7590856 > TP53.bam
```

#### FASTQ files

We can use bedtools to convert the BAM file to FASTQ. This command will generate two FASTQ files (TP53_R1.fastq and TP53_R2.fastq) for paired-end data. If your data is single-end, only the -fq file will be populated.

```
bedtools bamtofastq -i TP53.bam -fq TP53_R1.fastq -fq2 TP53_R2.fastq

```


#### VCF files

- Download VCF

```
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000_genomes_project/release/20190312_biallelic_SNV_and_INDEL/ALL.chr7.shapeit2_integrated_snvindels_v2a_27022019.GRCh38.phased.vcf.gz
```



- Filter TP53
  
``` 
bcftools view -r chr17:7661779-7687550 input.vcf > TP53.vcf
```
#### TP53.bed file

``` 
chr17   7661779   7687550   TP53
```


## Synthetic data

![](https://github.com/zstephens/neat-genreads/raw/master/docs/NEATNEAT.png)

- [ ] https://github.com/ncsa/NEAT
- [ ] https://github.com/4MedBox/Synthetic_DNA_Simulator [Documentation](https://docs.google.com/document/d/1ELpjAqmxfPtjS1Jc2MgVjlHq6_4AaNBm/edit)
      
## Benchmarking genomic variant calling

![](https://www.ghga.de/fileadmin/_processed_/f/0/csm_NCBench_figure_aa9d066ede.png)

- [ ] Check proposed workflow for benchmarking https://www.ghga.de/news/detail/benchmarking-genomic-variant-calling I guess the code to run it is this one:  https://github.com/snakemake-workflows/dna-seq-benchmark/
