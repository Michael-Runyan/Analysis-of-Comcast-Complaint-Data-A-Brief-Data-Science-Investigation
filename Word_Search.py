#Searches through the complaints and categories it through counting frequency of key words

import pandas as pd
import numpy as np

format_file = 'C://Users//Michael//Documents//Spring_2019//Cox_Project//com_per_city_csv.csv'
com_file = 'C://Users//Michael//Documents//Spring_2019//Cox_Project//Comcast//comcastcomplaints//complaints_clean_csv.csv'

dest = 'C://Users//Michael//Documents//Spring_2019//Cox_Project//complaint_category.csv'

format = pd.read_csv(format_file)
com = pd.read_csv(com_file)

#Creates an empty dataframe to add values
place_holder = np.zeros((len(format['Unnamed: 0']),4))
count = pd.DataFrame(data = place_holder,index  = format['Unnamed: 0'],columns = ['customer service', 'internet','cable','price'])

#words and categories searched for
c_service = ['customer service','rep','techs','technicians']
internet = ['internet','wifi','slow','router','signal']
cable_tv = ['cable','dvr']
price = ['price','$','charge','bill']
error = []

#generic searching method
#paramer: Array of words searching for
def search_for(cat,post_num):
    for word in cat:
        try:
            if word in com['text'][post_num].lower():
              count[cat[0]][com['City'][post_num].strip()] = count[cat[0]][com['City'][post_num].strip()].copy() + 1
              break
        except:
            error.append(post_num)
#searchs each post for the words
for index in range(len(com)):
    search_for(c_service,index)
    search_for(internet,index)
    search_for(cable_tv,index)
    search_for(price,index)

print(len(error))
print(error)
count.to_csv(dest)