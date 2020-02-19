import pandas as pd
import numpy as np
import billboard

database = pd.DataFrame(columns=['Title','Artist'])

chart = billboard.ChartData('hot-100')
count = 0
while chart.previousDate and count < 1001 :
    for song in chart:
        if song.title not in database['Title'].values:
            count += 1
            database.loc[count] = [song.title, song.artist]
            print(count)
    chart = billboard.ChartData('hot-100', chart.previousDate)

database.to_csv('hotsongs.csv')
