rm(list = ls())
gc()

library(data.table)
library(stringr)
library(vcfR)
library(dplyr)

vcf_read_one <- read.vcfR("file1.vcf", 
                      verbose = FALSE )

vcf_one = vcfR::getFIX(vcf_read_one) |> as.data.frame() |> setDT()
vcf_one$scenario = "One"

vcf_read_two <- read.vcfR("file2.vcf", 
                               verbose = FALSE )

vcf_two = vcfR::getFIX(vcf_read_two) |> as.data.frame() |> setDT()
vcf_two$scenario = "Two"


rm(vcf_read_one, vcf_read_two)
x = rbind(vcf_one, vcf_two)

rm(vcf_one, vcf_two)


y = x[, c("CHROM", "POS", "REF", "ALT", "scenario"), with = FALSE]



y$mut = paste(y$CHROM, y$POS, y$REF, y$ALT, sep = ":")


z = y[, by = mut, .(
    scenarios = paste(scenario, collapse = "+")
)]

z = z[order(z$scenarios), ]

fwrite(
    z, "All_mutation-overlaps.csv",
    row.names = FALSE, quote = TRUE, sep = ","
)


library(ggvenn)
library(ggplot2)

y = split(y, y$scenario)


y = list(
    'One' = y$one$mut,
    'Two' = y$two$mut
)

gr = ggvenn(
    y,
    fill_color = c("#43ae8d", "#ae4364")
) +
    
    coord_equal(clip = "off")


ggsave(
    plot = gr, filename = "Plots/All-overlap-plot.pdf", device = cairo_pdf,
    width = 8, height = 8, units = "in"
)


ggsave(
    plot = gr, filename = "Plots/All-overlap-plot.jpeg",
    width = 8, height = 8, units = "in", dpi = 600
)
