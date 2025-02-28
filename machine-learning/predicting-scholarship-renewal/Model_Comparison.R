library(randomForest)
library(caret)
#library(doParallel)

#cl <- makePSOCKcluster(4)
#registerDoParallel(cl)

set.seed(20129388)
df <- read.csv("LIFE/LIFE Project/LIFE_dataset_1218_ff_train_0508.csv")

################################################
# DAY ONE

#load training dataset
df_d1 <- df

#remove any possible duplicates or superflorous row counts if present
df_d1 <- df_d1[!duplicated(df_d1$ID),]
df_d1 <- df_d1[!(names(df_d1) %in% c("X"))]

# drop midterm and final grades to train only on data available on Day One
df_d1$Midterm.GPA <- NULL
df_d1$FallFinal.GPA <- NULL

## Create train & test with a specific cohort
train <- df_d1[df_d1$Aid_Year != 17, ]
test <- df_d1[df_d1$Aid_Year == 17, ]

#remove ID and Aid Year variables from the train data since they won't be useful predictors in future years
train$ID <- NULL
train$AID_YEAR <- NULL

#build and train random forest with optimized mtry and suitable ntree
#mtry optimized based on tune_grid.R file
rf <- randomForest(as.factor(LIFE.Eligible)~., data=train, cutoff=c(.6,.4), norm.votes=TRUE, ntree = 1501, importance=TRUE, mtry=7)
rf

#output feature importance plot
imp <- varImp(rf)
varImpPlot(rf, type=2, n.var=8, main='Feature Importances', color='navy')

#create test predictions using both probability and response output
test_probs <- predict(rf, test, type = "prob")
prob_in <- test_probs[,2]
test_pred <- predict(rf, test, type="response")

#create Confusion matrix and show sensitivity and specificity of the test data
cm <- table(test_pred, test$LIFE.Eligible)
cm
sensitivity(cm)
specificity(cm)

#store test results for separating into tiers
test_results_d1 <- data.frame(ID=test$ID, prediction=test_pred, target=test$LIFE.Eligible, prob_in = prob_in, Eligible = test$LIFE.Eligible)
test_results_d1$buckets_d1 <- cut(test_results_d1$prob_in, c(0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1))

# create output of a student's ID and their predicted risk
keep = c("ID","Eligible", "prob_in", "buckets_d1")
risk <- test_results_d1[keep]
names(risk) <- c("ID", "Eligible", "prob_in_d1", "buckets_d1")

################################################
# MIDTERM

#load training dataset
df_m <- df

#remove any possible duplicates or superflorous row counts if present
df_m <- df_m[!duplicated(df_m$ID),]
df_m <- df_m[!(names(df_m) %in% c("X"))]

# drop midterm or final grades as needed for testing different time periods
#df_m$Midterm.GPA <- NULL
df_m$FallFinal.GPA <- NULL

## Create train & test with a specific cohort
train <- df_m[df_m$Aid_Year != 17, ]
test <- df_m[df_m$Aid_Year == 17, ]

#remove ID and Aid Year variables from the train data since they won't be useful predictors in future years
train$ID <- NULL
train$AID_YEAR <- NULL

#build and train random forest with optimized mtry and suitable ntree
#mtry optimized based on tune_grid.R file
rf <- randomForest(as.factor(LIFE.Eligible)~., data=train, cutoff=c(.6,.4), norm.votes=TRUE, ntree = 1501, importance=TRUE, mtry=9)
rf

#output feature importance plot
imp <- varImp(rf)
varImpPlot(rf, type=2, n.var=8, main='Feature Importances', color='navy')

#create test predictions using both probability and response output
test_probs <- predict(rf, test, type = "prob")
prob_in <- test_probs[,2]
test_pred <- predict(rf, test, type="response")

#create Confusion matrix and show sensitivity and specificity of the test data
cm <- table(test_pred, test$LIFE.Eligible)
cm
sensitivity(cm)
specificity(cm)

#store test results for separating into tiers
test_results_m <- data.frame(ID=test$ID, prediction=test_pred, target=test$LIFE.Eligible, prob_in = prob_in, Eligible = test$LIFE.Eligible)
test_results_m$buckets_m <- cut(test_results_m$prob_in, c(0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1))

# create output of a student's ID and their predicted risk
keep = c("ID","Eligible", "prob_in", "buckets_m")
risk_mid <- test_results_m[keep]
names(risk_mid) <- c("ID", "Eligible", "prob_in_mid", "buckets_mid")

risk <- merge(risk, risk_mid, by=c("ID", "Eligible"))

################################################
# FALL FINAL

#load training dataset
df_ff <- df

#remove any possible duplicates or superflorous row counts if present
df_ff <- df_ff[!duplicated(df_ff$ID),]
df_ff <- df_ff[!(names(df_ff) %in% c("X"))]

# drop midterm or final grades as needed for testing different time periods
#df_ff$Midterm.GPA <- NULL
#df_ff$FallFinal.GPA <- NULL

## Create train & test with a specific cohort
train <- df_ff[df_ff$Aid_Year != 17, ]
test <- df_ff[df_ff$Aid_Year == 17, ]

#remove ID and Aid Year variables from the train data since they won't be useful predictors in future years
train$ID <- NULL
train$AID_YEAR <- NULL

#build and train random forest with optimized mtry and suitable ntree
#mtry optimized based on tune_grid.R file
rf <- randomForest(as.factor(LIFE.Eligible)~., data=train,cutoff=c(.6,.4), norm.votes=TRUE, ntree = 1501, importance=TRUE, mtry=6)
rf

#output feature importance plot
imp <- varImp(rf)
varImpPlot(rf, type=2, n.var=8, main='Feature Importances', color='navy')

#create test predictions using both probability and response output
test_probs <- predict(rf, test, type = "prob")
prob_in <- test_probs[,2]
test_pred <- predict(rf, test, type="response")

#create Confusion matrix and show sensitivity and specificity of the test data
cm <- table(test_pred, test$LIFE.Eligible)
cm
sensitivity(cm)
specificity(cm)

#store test results for separating into tiers
test_results_ff <- data.frame(ID=test$ID, prediction=test_pred, target=test$LIFE.Eligible, prob_in = prob_in, Eligible = test$LIFE.Eligible)
test_results_ff$buckets_ff <- cut(test_results_ff$prob_in, c(0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1))

# create output of a student's ID and their predicted risk
keep = c("ID","Eligible", "prob_in", "buckets_ff")
risk_ff <- test_results_ff[keep]
names(risk_ff) <- c("ID", "Eligible", "prob_in_ff", "buckets_ff")

risk <- merge(risk, risk_ff, by=c("ID", "Eligible"))
