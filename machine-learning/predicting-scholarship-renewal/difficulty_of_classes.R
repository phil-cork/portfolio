
require(plyr)
#function that iterates through a folder and combines all csv files into a single dataframe
#helfpul because raw data is in separate files according to aid year
path_to_files <- "C:/Users/corkp/Documents/ms-datasets/raw-data/classes/"
read_files <- function(path_to_files){
  setwd(path_to_files)
  files = list.files(path=path_to_files, pattern="*.csv")
  data <- lapply(files, function(x) read.csv(x, header=TRUE, na.strings=c("", " ", "NA")))
  all_data <- do.call("rbind.fill", data)
  return(all_data)
}

#load data on college classes students are taking
class_data <- read_files("C:/Users/corkp/Documents/ms-datasets/raw-data/classes/")


###1. Transform Class Grades into Average Difficulty

require(dplyr)
require(qdapTools)

#keep only classes which are offered in the fall
class_data <- class_data[endsWith(as.character(class_data$ACADEMIC_PERIOD), "10"),]

#remove all courses  which aren't given standard grades
rem_courses <- c("XA", "XA-", "XB+", "XB", "XB-", "XC+", "XC", "XC-", "XD+", "XD", "XD-", "XF", "XXF",
                 "RA", "RA-", "RB+", "RB", "RB-", "RC+", "RC", "RC-", "RD+", "RD", "RD-", "RF",
                 "GA", "GA-", "GB+", "GB", "GB-", "GC+", "GC", "GC-", "GD+", "GD", "GD-", "GF",
                 "NG", "TR", "S", "CP")
for (i in rem_courses) {
  class_data <- class_data[which(class_data$FINAL_GRADE != i), ]
}
class_data <- class_data[which(class_data$COURSE_IDENTIFICATION != "TEDU205"),]
class_data <- class_data[which(class_data$COURSE_IDENTIFICATION != "EDLS100"),]


#Calculate Class Average GPA and Frequency

#seperate completed courses (not withdrawn)
class_ind <- class_data[which(class_data$COURSE_REGISTER_IND == "Y" & class_data$FINAL_GRADE != "WA" & class_data$FINAL_GRADE != "W"), ]

#convert letter grades to GPA score
cols <- c("COURSE_IDENTIFICATION", "FINAL_GRADE", "CREDITS_EARNED")
class_ind <- class_ind[cols]
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "A", 4.0, 0.0)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "A-", 3.7, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "B+", 3.3, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "B", 3.0, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "B-", 2.7, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "C+", 2.3, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "C", 2.0, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "C-", 1.7, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "D+", 1.3, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "D", 1.0, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "D-", 0.7, class_ind$gpa)
class_ind$gpa <- ifelse(class_ind$FINAL_GRADE == "F", 0.0, class_ind$gpa)

#calculate difficulty, gpa score per credit hour of given course
class_ind$diff <- class_ind$gpa * class_ind$CREDITS_EARNED

#collect classes by their ID, take the mean of the GPA of each class
class_agg <- aggregate(class_ind$gpa, list(class_ind$COURSE_IDENTIFICATION), mean)
diff_agg <- aggregate(class_ind$diff, list(class_ind$COURSE_IDENTIFICATION), mean)

#count the times each course appears to ensure GPA isn't weighted by low frequency results
course_counts <- summarize(group_by(class_ind, COURSE_IDENTIFICATION), count=n())

#standardize names, combine the average GPA and class frequency columns
names(course_counts) <- c("Course_ID", "Count")
names(class_agg) <- c("Course_ID", "Avg_gpa")
class_agg <- merge(class_agg, course_counts)

names(diff_agg) <- c("Course_ID", "Avg_diff")


## Get Credits for Each Course ##

credits_agg <- aggregate(class_ind$CREDITS_EARNED, list(class_ind$COURSE_IDENTIFICATION), max)
names(credits_agg) <- c("Course_ID", "Course_Credit")


## Class Withdrawn Frequency ###

#separate withdrawn indicators, count the times each course appears
class_with <- class_data[which(class_data$WITHDRAWN_IND == "Y" | class_data$FINAL_GRADE == "WA" | class_data$FINAL_GRADE == "W"), ]
class_with <- class_with[3]
with_counts <- summarize(group_by(class_with, COURSE_IDENTIFICATION), count=n())

##standardize names, merge withdrawn count and the total count of classes found above
names(with_counts) <- c("Course_ID", "Withdraw_Count")
class_with <- merge(with_counts, course_counts)
class_with$Withdraw_Percent <- round(class_with$Withdraw_Count/(class_with$Withdraw_Count+class_with$Count),3)


## Combine GPA and Withdraw Percent, Add to Original Data Frame ##

class_diff <- merge(class_agg, class_with, all.x=TRUE, all.y=TRUE)
#set NAs to 0
class_diff[is.na(class_diff)] <- 0
class_diff <- merge(class_diff, diff_agg)
class_diff <- merge(class_diff, credits_agg)
#round GPA to two decimal places
class_diff$Avg_gpa <- round(class_diff$Avg_gpa, 2)

keep <- c("Course_ID", "Avg_gpa", "Withdraw_Percent", "Avg_diff", "Course_Credit")
class_diff <- class_diff[keep]
write.csv(class_diff, "ClassDifficultyTotal.csv", row.names=FALSE)