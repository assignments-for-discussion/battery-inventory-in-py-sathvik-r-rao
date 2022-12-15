def count_batteries_by_usage(cycles):
    # Variables to keep count of various categories of batteries
    lowCount=0
    mediumCount=0
    highCount=0
    # loop through the input values present in cycles
    for cycle in cycles:
    # condition to group them based of the cycles 
        if(cycle<310):
          lowCount+=1
        elif(cycle>=310 and cycle<929):
          mediumCount+=1
        else:
          highCount+=1
    #print(lowCount)
    #print(mediumCount)
    #print(highCount)
    # returning the count of each group of the batteries.
    return {
    "lowCount": lowCount,
    "mediumCount": mediumCount,
    "highCount": highCount
  }
