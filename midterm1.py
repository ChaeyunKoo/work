#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import matplotlib.pyplot as plt

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : 'gDyhxKdJOQAkCymIp3u03RELZ8PSJxPJT+phQjKvDbyavlrZineNwqdkh1s/Tmth71ZAydhQNyiAt8SvE6fC/g==', 
         'pageNo' : '1', 
         'numOfRows' : '1000', 
         'dataType' : 'JSON', 
         'base_date' : '20230513', 
         'base_time' : '0600', 
         'nx' : '55', 
         'ny' : '127' }

response = requests.get(url, params=params)
json_data = json.loads(response.content)

# 온도, 강수확률, 습도 데이터 추출
temperature_data = []
pop_data = []
reh_data = []
for item in json_data['response']['body']['items']['item']:
    if item['category'] == 'T1H':
        temperature_data.append(float(item['obsrValue']))
    elif item['category'] == 'POP':
        pop_data.append(float(item['obsrValue']))
    elif item['category'] == 'REH':
        reh_data.append(float(item['obsrValue']))

# 그래프 출력
fig, ax = plt.subplots(3, 1, figsize=(10, 10))

ax[0].plot(temperature_data, marker='o')
ax[0].set_ylabel('Temperature')

ax[1].plot(pop_data, marker='o')
ax[1].set_ylabel('Probability of Precipitation')

ax[2].plot(reh_data, marker='o')
ax[2].set_ylabel('Relative Humidity')
ax[2].set_xlabel('Time')

plt.show()


# In[ ]:




