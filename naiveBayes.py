  
# 
#  Naive Bayes Classifier chapter 6
#


# _____________________________________________________________________

class Classifier:
    def __init__(self, input_data, dataFormat):

        """ a classifier will be built from files with the input_data
        excluding the file with test_data. dataFormat is a string that
        describes how to interpret each line of the data files. For example,
        for the iHealth data the format is:
        "attr	attr	attr	attr	class"
        """
   
        total = 0
        classes = {}
        counts = {}
        
        
        # reading the data in from the file
        self.format = dataFormat.strip().split(',')
        self.prior = {}
        self.conditional = {}
        filename = input_data 
        f = open(filename)
        lines = f.readlines()
        f.close();
        for line in lines:
            fields = line.strip().split(',')
            ignore = []
            vector = []
            for i in range(len(fields)):
                if self.format[i] == 'num':
                    vector.append(float(fields[i]))
                elif self.format[i] == 'attr':
                    vector.append(fields[i])                           
                elif self.format[i] == 'comment':
                    ignore.append(fields[i])
                elif self.format[i] == 'class':
                    category = fields[i]
            # now process this instance
            total += 1
            classes.setdefault(category, 0)
            counts.setdefault(category, {})
            classes[category] += 1
            # now process each attribute of the instance
            col = 0
            for columnValue in vector:
                col += 1
                counts[category].setdefault(col, {})
                counts[category][col].setdefault(columnValue, 0)
                counts[category][col][columnValue] += 1
        
        #
        # ok done counting. now compute probabilities
        #
        # first prior probabilities p(h)
        #
        for (category, count) in classes.items():
            self.prior[category] = count / float(total)
        #
        # now compute conditional probabilities p(h|D)
        #
        for (category, columns) in counts.items():
              self.conditional.setdefault(category, {})
              for (col, valueCounts) in columns.items():
                  self.conditional[category].setdefault(col, {})
                  for (attrValue, count) in valueCounts.items():
                      self.conditional[category][col][attrValue] = (
                          count / float(classes[category]))
        self.tmp =  counts                
        

           
    def testClassifier(self, test_data):
        """Evaluate the classifier with data from the file
        test_data"""
        filename = test_data
        f = open(filename)
        lines = f.readlines()
        totals = {}
        f.close()
        loc = 1
        for line in lines:
            loc += 1
            data = line.strip().split(',')
            vector = []
            classInColumn = -1
            for i in range(len(self.format)):
                  if self.format[i] == 'num':
                      vector.append(float(data[i]))
                  elif self.format[i] == 'attr':
                      vector.append(data[i])
                  elif self.format[i] == 'class':
                      classInColumn = i
            theRealClass = data[classInColumn]
            classifiedAs = self.classify(vector)
            totals.setdefault(theRealClass, {})
            totals[theRealClass].setdefault(classifiedAs, 0)
            totals[theRealClass][classifiedAs] += 1
        return totals


    
    def classify(self, itemVector):
        """Return class we think item Vector is in"""
        results = []
        for (category, prior) in self.prior.items():
            prob = prior
            col = 1
            for attrValue in itemVector:
                if not attrValue in self.conditional[category][col]:
                    # we did not find any instances of this attribute value
                    # occurring with this category so prob = 0
                    prob = 0
                else:
                    prob = prob * self.conditional[category][col][attrValue]
                col += 1
            results.append((prob, category))
        # return the category with the highest probability
        return(max(results)[1])
 

def beginClassification(input_data, test_data, dataFormat):
    results = {}
    c = Classifier(input_data,  dataFormat)
    t = c.testClassifier(test_data)
    for (key, value) in t.items():
        results.setdefault(key, {})
        for (ckey, cvalue) in value.items():
            results[key].setdefault(ckey, 0)
            results[key][ckey] += cvalue
                
    # now print results
    categories = list(results.keys())
    categories.sort()
    print(   "\n            Classified as: ")
    header =    "             "
    subheader = "               +"
    for category in categories:
        header += "%8s   " % category
        subheader += "-------+"
    print (header)
    print (subheader)
    total = 0.0
    correct = 0.0
    for category in categories:
        row = " %10s    |" % category 
        for c2 in categories:
            if c2 in results[category]:
                count = results[category][c2]
            else:
                count = 0
            row += " %5i |" % count
            total += count
            if c2 == category:
                correct += count
        print(row)
    print(subheader)
    print("\n%5.3f percent correct" %((correct * 100) / total))
    print("total of %i instances" % total)

beginClassification("input_data","test_data", "comment,,comment,comment,comment,comment,comment,num,num,num,num,num,num,num,num,num,num,num,num,num,num,num,num,class")
#c = Classifier("house-votes/hv", 0,num
#                       "class\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr")

#c = Classifier("iHealth/i", 10,
#                       "attr\tattr\tattr\tattr\tclass")
#print(c.classify(['health', 'moderate', 'moderate', 'yes']))

#c = Classifier("house-votes-filtered/hv", 5, "class\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr")
#t = c.testBucket("house-votes-filtered/hv", 5)
#print(t)

