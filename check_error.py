regular_file = open("output.csv", 'r')

regular = regular_file.readlines()
regular_file.close()

count = 0
for line in regular:
    count += 1
    
    # skip header
    if count == 1:
      continue
    
    player = line.strip().split(',')

    # checking number of attributes
    if len(player) != 24:
      print 'deu blade: ',len(player),count
