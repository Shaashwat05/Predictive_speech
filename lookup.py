import pandas as pd 
import numpy as np 

col_names = ['Website', 'Trustworthiness', 'Avg_Daily_Visitors', 'Avg_Daily_Pageviews']
data = pd.read_csv("Web_Scrapped_websites.csv", encoding = "ISO-8859-1", usecols=col_names)

name = data['Website'].tolist()
trust = data['Trustworthiness'].tolist()
visit = data['Avg_Daily_Visitors'].tolist()
view = data['Avg_Daily_Pageviews'].tolist()

web = [name, trust, visit, view]

#Cleaning data- removing unwanted, bad websites
def delete(i):
    del web[0][i]
    del web[1][i]
    del web[2][i]
    del web[3][i]



# removing websites with unsatisfactory trust
i=0
while(i<len(web[1])):
    if(web[1][i] == 'Unsatisfactory'):
        delete(i)
    else:
        i+=1


# removing websites with no views or unknown views
i=0
while(i<len(web[1])):
    try:
        if(np.isnan(web[2][i])):
            delete(i)
        else:
            i+=1
    except:
        i+=1
        continue




