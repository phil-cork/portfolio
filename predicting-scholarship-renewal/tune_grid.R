#Prior to running this script, create dataframe df for desired tunegrid test.

# Create model with default paramters
control <- trainControl(method="repeatedcv", number=10, repeats=3)
metric <- "Accuracy"
mtry <- sqrt(ncol(df))
tunegrid <- expand.grid(.mtry=mtry)
rf_default <- train(LIFE.Eligible~., data=train, method="rf", metric=metric, tuneGrid=tunegrid, trControl=control)
print(rf_default)

#Change the mtry range based on the number of attributes
tunegrid <- expand.grid(.mtry=c(1:5))
rf_gridsearch <- train(LIFE.Eligible~., data=train, method="rf", metric=metric, tuneGrid=tunegrid, trControl=control)
print(rf_gridsearch)
plot(rf_gridsearch)