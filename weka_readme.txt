Loading the output.csv file in Weka

In order for Weka 3.7 to work with the output.csv file, some parameters have to be changed.
When opening the file in Weka, choose "Use converter" and set the following parameters:

enclosureCharacters = "
missingValue = NULL
stringAttributes = 3,4

After loading you can choose to remove the first_name and last_name attributes
since they aren't supposed to influence in the classification.