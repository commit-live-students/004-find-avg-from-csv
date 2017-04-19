#Question - 4: Let's import our datafile mpg.csv, which contains fuel economy data for 234 cars.
#find the average hwy mpg for each class of vehicle in our dataset.
import csv

def calculateAvgHwy(filename):
    with open(filename) as csvfile:
        mpg = list(csv.DictReader(csvfile))

    vehicleclass = set(d['class'] for d in mpg) # what are the class types
    HwyMpgByClass = []

    for t in vehicleclass: # iterate over all the vehicle classes
        summpg = 0
        vclasscount = 0
        for d in mpg: # iterate over all dictionaries
            if d['class'] == t: # if the cylinder amount type matches,
                summpg += float(d['hwy']) # add the hwy mpg
                vclasscount += 1 # increment the count
        HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

    HwyMpgByClass.sort(key=lambda x: x[1])
    return HwyMpgByClass