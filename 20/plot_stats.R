library(stringr)
library(ggplot2)
library(dplyr)
library(gridExtra)
library(tidyr)
library(cowplot)

input_data<-read.csv(file = 'Annotation_summary - Sheet1.tsv',sep="\t",header = TRUE)

busco_complete<-rep(0,length(input_data$BUSCO))
busco_single<-rep(0,length(input_data$BUSCO))
busco_duplicate<-rep(0,length(input_data$BUSCO))
busco_fragmented<-rep(0,length(input_data$BUSCO))
busco_missing<-rep(0,length(input_data$BUSCO))
for (i in c(1:length(input_data$BUSCO))){
busco_complete[i]<-unlist(strsplit(input_data$BUSCO[i],split = ","))[2]

busco_single[i]<-unlist(strsplit(input_data$BUSCO[i],split = ","))[3]

busco_duplicate[i]<-unlist(strsplit(input_data$BUSCO[i],split = ","))[4]

busco_fragmented[i]<-unlist(strsplit(input_data$BUSCO[i],split = ","))[5]

busco_missing[i]<-unlist(strsplit(input_data$BUSCO[i],split = ","))[6]

}

omark_complete<-rep(0,length(input_data$BUSCO))
omark_missing<-rep(0,length(input_data$BUSCO))
omark_consistent<-rep(0,length(input_data$BUSCO))
omark_inconsistent<-rep(0,length(input_data$BUSCO))
omark_contaminant<-rep(0,length(input_data$BUSCO))
omark_unknown<-rep(0,length(input_data$BUSCO))
for (i in c(1:length(input_data$OMArk.Completeness))){
  omark_complete[i]<-unlist(strsplit(input_data$OMArk.Completeness[i],split = ","))[2]
  
  omark_missing[i]<-unlist(strsplit(input_data$OMArk.Completeness[i],split = ","))[5]
  
  omark_consistent[i]<-unlist(strsplit(input_data$OMArk.Consistency[i],split = ","))[1]
  
  omark_inconsistent[i]<-unlist(strsplit(input_data$OMArk.Consistency[i],split = ","))[4]
  
  omark_unknown[i]<-unlist(strsplit(input_data$OMArk.Consistency[i],split = ","))[10]
  
}

df_omark<-data.frame(species=input_data$Species)
df_omark$pipeline<-input_data$Pipeline.used
df_omark$complete<-as.numeric(omark_complete)
df_omark$missing<-as.numeric(omark_missing)
df_omark$consistent<-as.numeric(omark_consistent)
df_omark$inconsistent<-as.numeric(omark_inconsistent)
df_omark$unknown<-as.numeric(omark_unknown)


df<-data.frame(species=input_data$Species)
df$pipeline<-input_data$Pipeline.used
df$nogenes<-as.numeric(gsub(",", "", input_data$Nr..genes))
df$complete<-as.numeric(gsub(",", "", busco_complete))
df$single<-as.numeric(gsub(",", "", busco_single))
df$duplicated<-as.numeric(gsub(",", "", busco_duplicate))
df$fragmented<-as.numeric(gsub(",", "", busco_fragmented))
df$missing<-as.numeric(gsub(",", "", busco_missing))

df_long <- reshape2::melt(df, id.vars = c("species", "pipeline", "nogenes"), variable.name = "BUSCO")

gg_nogenes <- ggplot(data = df, aes(x = species, y = nogenes, fill = pipeline)) +
  geom_bar(stat = "identity", position = position_dodge2(width = 0.9, preserve = "single"), width = 0.7) +
  labs(title = "Number of genes annotated by Species and Pipeline",
       x = "Species",
       y = "Number of genes Count") +
  #scale_fill_brewer(palette = "Set2") +  # Adjust the color palette as needed
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
gg_nogenes
ggsave(filename = 'no_genes.svg',plot = gg_nogenes,device = 'svg')

df_long <- pivot_longer(df, cols = c("single", "duplicated", "fragmented", "missing"), names_to = "Category", values_to = "Value")

df_filtered <- df_long %>%
  group_by(species,pipeline) %>%
  filter(any(Value > 0))

custom_fill_colors <- c("single" = "cadetblue", "duplicated" = "blue", "fragmented" = "yellow", "missing" = "red")
category_order <- c("missing","fragmented","duplicated","single")
df_filtered$Category <- factor(df_filtered$Category, levels = category_order)

plot_list <- list() 

for (i in c(1:length(unique(df$species)))){
  
  df_plot<-df_filtered[df_filtered$species==unique(df$species)[i],]
  if (unique(df$species)[i]=="Homo sapiens chrom 19"){
    plot_list[[i]]<-ggplot(df_plot, aes(x = pipeline, y = Value, fill = Category)) +
      geom_bar(stat = "identity") +
      labs(title = unique(df$species)[i],
           x = "Pipeline",
           y = "Percent BUSCO genes") + ylim(c(0,10))+
      scale_fill_manual(values = custom_fill_colors, breaks = category_order) +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1),legend.position = "none")
  }else{
  plot_list[[i]]<-ggplot(df_plot, aes(x = pipeline, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  labs(title = unique(df$species)[i],
       x = "Pipeline",
       y = "Percent BUSCO genes") +
  scale_fill_manual(values = custom_fill_colors, breaks = category_order) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),legend.position = "none")
  }
}
plot<-grid.arrange(grobs=plot_list,nrow=1,widths=rep(1,length(unique(df$species))))
plot
ggsave(filename = 'busco.svg',plot=plot,device = 'svg')
df_long <- pivot_longer(df_omark, cols = c("complete", "missing"), names_to = "Category", values_to = "Value")

custom_fill_colors <- c("complete" = "cadetblue","missing" = "red")
category_order <- c("missing","complete")
df_long$Category <- factor(df_long$Category, levels = category_order)

df_filtered <- df_long %>%
  group_by(species,pipeline) %>%
  filter(any(Value > 0))

plot_list <- list() 

for (i in c(1:length(unique(df$species)))){

  df_plot<-df_filtered[df_filtered$species==unique(df$species)[i],]
  if (unique(df$species)[i]=="Homo sapiens chrom 19"){
    plot_list[[i]]<-ggplot(df_plot, aes(x = pipeline, y = Value, fill = Category)) +
      geom_bar(stat = "identity") +
      labs(title = unique(df$species)[i],
           x = "Pipeline",
           y = "Percent OMA proteins") + ylim(c(0,11))+
      scale_fill_manual(values = custom_fill_colors, breaks = category_order) +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1),legend.position = "none")
  }else{
  plot_list[[i]]<-ggplot(df_plot, aes(x = pipeline, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  labs(title = unique(df$species)[i],
       x = "Pipeline",
       y = "Percent OMA proteins") +
  scale_fill_manual(values = custom_fill_colors, breaks = category_order) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),legend.position = "none")
  }
}
plot<-grid.arrange(grobs=plot_list,nrow=1,widths=rep(1,length(unique(df$species))))
plot
ggsave(filename = 'omark_complete.svg',plot = plot,device = 'svg')

df_long <- pivot_longer(df_omark, cols = c("consistent", "inconsistent","unknown"), names_to = "Category", values_to = "Value")

custom_fill_colors <- c("consistent" = "cadetblue","inconsistent"="red","unknown" = "lightgrey")
category_order <- c("unknown","inconsistent","consistent")
df_long$Category <- factor(df_long$Category, levels = category_order)

df_filtered <- df_long %>%
  group_by(species,pipeline) %>%
  filter(any(Value > 0))

plot_list <- list() 

for (i in c(1:length(unique(df$species)))){
  df_plot<-df_filtered[df_filtered$species==unique(df$species)[i],]

  plot_list[[i]]<-ggplot(df_plot, aes(x = pipeline, y = Value, fill = Category)) +
  geom_bar(stat = "identity") +
  labs(title = unique(df$species)[i],
       x = "Pipeline",
       y = "Percent annotated proteins") +
  scale_fill_manual(values = custom_fill_colors, breaks = category_order) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),legend.position = "none")
}
plot<-grid.arrange(grobs=plot_list,nrow=1,widths=rep(1,length(unique(df$species))))
plot
ggsave(filename = 'omark_consistent.svg',plot = plot,device = 'svg')
