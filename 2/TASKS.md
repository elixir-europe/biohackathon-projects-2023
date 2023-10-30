### Real data

- Install requirements

```
 sudo apt-get install pdfjam texlive-extra-utils samtools

```
- Get reference sequence

```
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa

```

- Get human sequence from  https://www.internationalgenome.org/data-portal/sample

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

## Synthetic data

![](https://github.com/zstephens/neat-genreads/raw/master/docs/NEATNEAT.png)

- [ ] Using NEAT: https://github.com/zstephens/neat-genreads
  - [ ] https://github.com/zstephens/neat-genreads#targeted-region-simulation

## Benchmarking genomic variant calling

![](https://www.ghga.de/fileadmin/_processed_/f/0/csm_NCBench_figure_aa9d066ede.png)

- [ ] Check proposed workflow for benchmarking https://www.ghga.de/news/detail/benchmarking-genomic-variant-calling I guess the code to run it is this one:  https://github.com/snakemake-workflows/dna-seq-benchmark/
