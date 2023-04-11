#!/usr/bin/env python
# coding: utf-8

# In[200]:


#States population without any packages

with open('statesP.csv', 'r') as f:
    next(f)
    results1 = []
    for line in f:
            words = line.split(',')
            results1.append((words[0], words[1]))
    print(results1)


# In[201]:


#Now we put it as a dictionary

dictforp = {rows[0]:{"population":rows[1].strip()}for rows in results1}
print(dictforp)


# In[202]:


#States area, where we do the same thing

with open('statesA.csv', 'r') as f:
    next(f)
    results2 = []
    for line in f:
            words = line.split(',')
            results2.append((words[0], words[1]))
    print(results2)


# In[203]:


#Now we put it as a dictionary
dictfora = {rows[0]:{"area":rows[1].strip()}for rows in results2}
print(dictfora)


# In[204]:


#Here we create a list with the keys, or names of the states in the dataset to iterate through it
states = []
for key in dictfora.keys():
  states.append(key)


# In[205]:


#here, we create an element called population on the dictionary for areas, and fill those positions 
#with the population field of dictforp while also matching keys as we go
for i in range(len(states)):
    dictfora[states[i]]['population'] = dictforp[states[i]]['population']


# In[206]:


print(dictfora)
#here we will see that indeed keys were matched and not each state has its area and population


# In[207]:


#Now we want to create a density field and we will fill that part by using the division
#between the population and area of each of the matching keys in list a

for i in range(len(states)):
    dictfora[states[i]]['density'] = float(dictfora[states[i]]['population'])/float(dictfora[states[i]]['area'])


# In[208]:


print(dictfora)
#As we can see, now each state has its respective density as an element of their name key


# In[246]:


#Now we want to write some code to figure out which state has the highest density
#this code is a bit rudimentary because of the scarcity of tools dictionaries have
print("The state with the highest population density is:")
t = []

for i in range(len(states)):
    r,b,c = dictfora[states[i]].values()
    t.append(c)

#now that we have all the values in a list, we can use the max function to check the value
highestd = max(t)

#and now that we have the value, we can check which state has it
for i in range(len(states)):
    z,y,u = dictfora[states[i]].values()
    if u == highestd:
        print(states[i])

print(f"And the population density that state has is: {highestd} people per square miles of land")
#so here we can see that the max density is 1062.43, and that is find in


# In[247]:


#And now to find the lowest we apply the same methodology but using min for the list

print("The state with the lowest population density is:")

o = []

for i in range(len(states)):
    r,b,c = dictfora[states[i]].values()
    o.append(c)

#now that we have all the values in a list, we can use the max function to check the value
lowestd = min(o)

#and now that we have the value, we can check which state has it
for i in range(len(states)):
    z,y,u = dictfora[states[i]].values()
    if u == lowestd:
        print(states[i])

print(f"And the population density that state has is: {lowestd} people per square miles of land")


# In[ ]:


#now, we must create a dataset printing it out as a CSV file 


# In[250]:


print("State, area, population, density")
for i in range(len(states)):
    print(states[i],",", ','.join([str(elem) for elem in list(dictfora[states[i]].values())]), sep='')


# In[ ]:


#After doing so, we must put all these information separetly in a list, so we can do calculations


# In[263]:


#first we create empty lists
area = []
population = []
density = []

for i in range(len(states)):
    r,b,c = dictfora[states[i]].values()
    area.append(r)
    population.append(b)
    density.append(c)

#now we convert them into floats because they used to be strings inside of the dictionary
area = [float(i) for i in area]
population = [float(i) for i in population]
density = [float(i) for i in density]


# In[269]:


#now we create a lambda function to take the mean of a dataset
mean = lambda data: sum(data) / len(data)

areaMean = mean(area)
populationMean = mean(population)
densityMean = mean(density)
print("The mean of the area between states is:", areaMean, " miles squared")
print("The mean of the population between states is:", populationMean, " people")
print("The mean of the population density between states is:", densityMean, " people per square miles")


# In[272]:


#Now we have to calculate the standart deviation for these variables
#to do so, we first calculate the variance and then take the square root. Lets use maps

def variance(data):
    # for every number, subtract the mean, sq the result
    mu = mean(data)
    # sum of sq differences
    return sum((x - mu) ** 2 for x in data) / len(data)

def standard_deviation(data):
    return variance(data) ** 0.5


# In[280]:


stdOfArea = standard_deviation(area)
stdOfPopulation = standard_deviation(population)
stdOfDensity = standard_deviation(density)


print("The standart deviation of the area between states is:", stdOfArea)
print("The standart deviation of the population between states is:", stdOfPopulation)
print("The standart deviation of the population density between states is:", stdOfDensity)


# In[302]:


#now we need the correlation, but to find it we must create a function that calculates the covariance
def covariance(x, y):
    # Finding the mean of the series x and y
    mean_x = sum(x)/float(len(x))
    mean_y = sum(y)/float(len(y))
    # Subtracting mean from the individual elements
    sub_x = [i - mean_x for i in x]
    sub_y = [i - mean_y for i in y]
    numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
    denominator = len(x) #which represents n in the formula
    cov = numerator/denominator
    return cov


# In[303]:


#now we just simply use the function above and calculate the correlation between variables

def corr(x,y):
    x_std= standard_deviation(x)
    y_std= standard_deviation(y)
    return covariance(x,y) / (x_std*y_std)


# In[304]:


print("The correlation between area and population is: ", corr(area,population))


# In[ ]:


#what we can say about this correlation is that its a low correlation between both
#meaning that a larger state would not mean a larger population, but at the same time
#because it isnt strong negatively, it doesnt mean population will be larger on small places
#then we can conclude that such relation averages out as there are places in the US with large land
#and no people, as well as large land with a lot of people and a similar story with small states
#then we must conclude that it depends where you look at. Probably if we delimit our analysis to the
#west side of the country, the correlation would be stronger.

