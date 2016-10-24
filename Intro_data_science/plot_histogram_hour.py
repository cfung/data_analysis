import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, lets 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Why don't you plot two histograms on the same axes, showing hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histograph may look similar to the following graph:
    http://i.imgur.com/9TrkKal.png
    
    You can read a bit about using matplotlib and pandas to plot
    histograms:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can look at the information contained within the turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    plt.figure()
    #rain = turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['rain'] == 1].values
    #rain = turnstile_weather[['ENTRIESn_hourly']][turnstile_weather.rain == 1]
    #no_rain = turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['rain'] == 0].values
    #  [ 1  5  9 13 17 21  0  4 12 16 20  8  2  6 10 14 18 22  3  7 11 15 19 23] totlal = 24
    hour = turnstile_weather['Hour']
    total_hours = turnstile_weather.Hour.unique()
    total_units = turnstile_weather.UNIT.unique()

    aggregate_total_hours = {}

    

    test = ['R001', 'R002']

    for hour in total_hours:

        aggregate_total_entries = 0

        for unit in total_units:
        
            if not math.isnan(turnstile_weather[['ENTRIESn_hourly']][(turnstile_weather['Hour'] == hour) & (turnstile_weather['UNIT'] == unit)].mean()):
                aggregate_total_entries += turnstile_weather[['ENTRIESn_hourly']][(turnstile_weather['Hour'] == hour) & (turnstile_weather['UNIT'] == unit)].mean()
        
        aggregate_total_hours[hour] = aggregate_total_entries

    print "agg_total hours....",aggregate_total_hours
    print "ending...********"
    #print "AND ...\n", turnstile_weather[['ENTRIESn_hourly']][(turnstile_weather['Hour'] == 0) & (turnstile_weather['UNIT'] == unit)]


    print "hour p = 0 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 0].mean()
    print "hour p = 1 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 1].mean()
    print "hour p = 2 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 2].mean()
    print "hour p = 3 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 3].mean()
    print "hour p = 4 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 4].mean()
    print "hour p = 5 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 5].mean()
    print "hour p = 6 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 6].mean()
    print "hour p = 7 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 7].mean()
    print "hour p = 8 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 8].mean()
    print "hour p = 9 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 9].mean()
    print "hour p = 10 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 10].mean()
    print "hour p = 11 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 11].mean()
    print "hour p = 12 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 12].mean()
    print "hour p = 13 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 13].mean()
    print "hour p = 14 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 14].mean()
    print "hour p = 15 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 15].mean()
    print "hour p = 16 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 16].mean()
    print "hour p = 17 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 17].mean()
    print "hour p = 18 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 18].mean()
    print "hour p = 19 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 19].mean()
    print "hour p = 20 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 20].mean()
    print "hour p = 21 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 21].mean()
    print "hour p = 22 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 22].mean()
    print "hour p = 23 ...\n", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['Hour'] == 23].mean()

    hour_avg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    entries_avg = [357637, 161818, 13373, 3397, 80957, 40599, 20906, 109297, 210288, 405622, 76633, 82304, 735946, 
    315277, 141271, 51944, 577618, 415462, 64072, 37277, 805516, 430585, 36692, 10371]

    entries = turnstile_weather['ENTRIESn_hourly']
  
    #df_rain = rain.reset_index()
    #df_norain = norain.reset_index()

    '''
    turnstile_weather[['ENTRIESn_hourly']][turnstile_weather.rain == 1].hist()
    '''
    #gb = turnstile_weather.groupby('rain')

    #plt.scatter(hour, entries, color='y')
    plt.scatter(hour_avg, entries_avg, color='y')
    #gb = gb.reset_index().values
    #plt.hist(df_norain['ENTRIESn_hourly'], bins=150, alpha=0.5, color='g', label ='No Fog')
    #plt.hist(gb.get_group(1).ENTRIESn_hourly, label ='Rain')

    #turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['rain'] == 1].hist() # your code here to plot a historgram for hourly entries when it is raining
    #turnstile_weather['...'] # your code here to plot a historgram for hourly entries when it is not raining
    
    #plt.hist(rain, label = 'rainy days')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Subway entries per hour')
    plt.axis([0, 24, 0, 450000])
    plt.title('Mean of Number of Entries by the Hour of the Day')
    #plt.suptitle('Hourly subway entries during foggy and non-foggydays')
    #plt.legend(['No fog', 'Fog'])

    #print "rain == 1", turnstile_weather[['ENTRIESn_hourly']][turnstile_weather['rain'] == 1]
    
    #print "rain == 0", turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0]

    return plt


if __name__ == "__main__":
    image = "plot_hour.png"
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    plt = entries_histogram(turnstile_weather)
    plt.xlim([0, 24])
    plt.savefig(image)
