# Dandalion Plot
library(polycor)
library(ConsensusClusterPlus)

d <- read.csv(".csv", header=TRUE)
head(d)


mads=apply(d,1,mad)
d=d[rev(order(mads))]
d = sweep(d,1, apply(d,1,median,na.rm=T))
d = as.matrix(d)

library(ConsensusClusterPlus)
title=tempdir()

results = ConsensusClusterPlus(d,maxK=6,reps=50,pItem=0.8,pFeature=1, title=title,clusterAlg="hc",distance="pearson",seed=1262118388.71279,plot="png")
results[[2]][["consensusMatrix"]][1:5,1:5]
results[[2]][["consensusTree"]]