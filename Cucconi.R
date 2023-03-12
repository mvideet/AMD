library(ggplot2)
library(nonpar)
library(dplyr)
#reading the data
amddata <- read.csv("/Users/mvideet/Downloads/AMD.csv")

#creating a vector that will store all the genes with a p-val > 0.01
Gene <- c("0")
pval <- c("0")
imp_genes <- data.frame(Gene,pval)

#looping through each of the genes
for(i in 4:ncol(amddata)-1){
  #getting the name of the gene
  column_name <- names(amddata)[i]
  #recieving the gene data for each of the rows along with the AMD classification
  df =amddata[, c(column_name, "mgs_level")]
  #splitting by MGS4 and MGS1
  gene1 <- filter(df, mgs_level=="MGS4")
  gene1 <- as.numeric(unlist(as.list(gene1[column_name])))
  gene2 <- filter(df, mgs_level=="MGS1")
  gene2 <- as.numeric(unlist(as.list(gene2[column_name])))
  #recieiving the p-value
  str<-(unlist(cucconi.test(gene1,gene2,method='bootstrap'), use.names = FALSE)[3])
  str <- as.double(str)
  #if the p_value is less than 1 meaning that it is significant
  if(str < 0.01){
  #adding to that vector
  imp_genes[nrow(imp_genes)+1,]=list(Gene = toString(column_name), pval = toString(str))
  }
  #plotting the distribution of each of the genes
  plot(density(gene1), main = str)
  lines(density(gene2), col = "blue")
  legend("topright", c("MGS4", "MGS1"),
         col =c("black","blue"), lty=1)
  
}
#printing the list
print(imp_genes)

