#Organizes the data by city
#Coumlns of outputted data are as below
# City      Number of Complaints        Population

import pandas as pd
import numpy as np

com_file = 'C://Users//Michael//Documents//Spring_2019//Cox_Project//Comcast//comcastcomplaints//complaints_clean_csv.csv'
pop_file = 'C://Users//Michael//Documents//Spring_2019//Cox_Project//US_census_2015_pop_by_city_csv.csv'
dest =  'C://Users//Michael//Documents//Spring_2019//Cox_Project//com_per_city_csv.csv'
complaints = pd.read_csv(com_file)
pop = pd.read_csv(pop_file)



place_holder = np.zeros((len(pop['City']),2))

final = pd.DataFrame(data=place_holder,columns = ['Population','Complaints'],index = pop['City'])

#adds the correct population to the dataframe

index = 0
for cit in final.index:
    final['Population'][cit] = pop['Population in 2015'][index]
    index = index + 1

#Counts the instances of complaints in each City
for cit in complaints['City']:

    try:
        cit = cit.strip()
        final['Complaints'][cit] = int(final['Complaints'][cit]) + 1
    except:
        temp = pd.DataFrame(data = [[25000,1]],columns = ['Population','Complaints'],index = [cit])
        final = final.append(temp)
print(final)


final.to_csv(dest)