# Install Samtools, BCFTools and htslib on linux

# Install some build dependencies

```sh
sudo apt-get install autoconf automake make gcc perl zlib1g-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev libncurses5-dev
```

# [samtools]

```sh
$ wget https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2 -O samtools.tar.bz2
$ tar -xjvf samtools.tar.bz2
$ cd samtools-{version}
$ make
$ sudo make prefix=/usr/local/bin install
# if you have old version such as 0.x from samtools, you may remove it and create a link to new version
$ sudo apt remove samtools
$ sudo ln -s /usr/local/bin/bin/samtools /usr/bin/samtools
# Or, you can just use the path to call samtools
$ /usr/loca/bin/bin/samtools -h
```

# [BCFtools]

```sh
$ wget https://github.com/samtools/bcftools/releases/download/1.3.1/bcftools-1.3.1.tar.bz2 -O bcftools.tar.bz2
$ tar -xjvf bcftools.tar.bz2
$ cd bcftools-{version}
$ make
$ sudo make prefix=/usr/local/bin install
$ sudo ln -s /usr/local/bin/bin/bcftools /usr/bin/bcftools
```

# [HTSlib]

```sh
$ wget https://github.com/samtools/htslib/releases/download/1.3.2/htslib-1.3.2.tar.bz2 -O htslib.tar.bz2
$ tar -xjvf htslib.tar.bz2
$ cd htslib-{version}
$ make
$ sudo make install
```

   [samtools]: <https://github.com/samtools/samtools>
   [BCFTools]: http://samtools.github.io/bcftools/
   [HTSlib]: https://github.com/samtools/htslib
   
