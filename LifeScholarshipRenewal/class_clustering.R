library(dplyr)
library(Rtsne)
library(cluster)
library(magrittr)
library(ggplot2)

# need df preexisting

gower_dist <- daisy(df,
                    metric = "gower")

summary(gower_dist)

gower_mat <- as.matrix(gower_dist)
df[which(gower_mat == min(gower_mat[gower_mat != min(gower_mat)]), arr.ind =TRUE)[1,], ]

sil_width <- c(NA)

for (i in 2:15) {
  
  pam_fit <- pam(gower_dist, diss=TRUE, k=i)
  
  sil_width[i] <- pam_fit$silinfo$avg.width
  
}

plot(1:15, sil_width,
     xlab = "Number of clusters",
     ylab = "Silhouette Width",
     lines(1:15, sil_width))

pam_fit <-pam(gower_dist, diss=TRUE, k=2)

pam_results <- df %>%
  dplyr::select(-ID) %>%
  mutate(cluster=pam_fit$clustering) %>%
  group_by(cluster) %>%
  do(the_summary = summary(.))

pam_results$the_summary

df[pam_fit$medoids, ]

tsne_obj <- Rtsne(gower_dist, is_distance = TRUE)

tsne_data <- tsne_obj$Y %>%
  data.frame() %>%
  setNames(c("X", "Y")) %>%
  mutate(cluster = factor(pam_fit$clustering),
         name = df$ID)

ggplot(aes(x = X, y = Y), data = tsne_data) +
  geom_point(aes(color = cluster))