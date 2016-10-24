import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Computes mean and performs a t-test, Whitney U, shapiro-welk test on two sets of NY subway data 

    
    """
    
    #read panda file and convert to dataframe
    subway_data = pandas.read_csv(filename)
    #print subway_data
    #print type(baseball_data)
    
    #rightHandBatters = baseball_data[baseball_data['handedness']=='R']['avg'].values.tolist()
    rain_ridership = subway_data[subway_data['rain']==1]['ENTRIESn_hourly'].values.tolist() 
    print "rain_ridership", rain_ridership

    #leftHandBatters = baseball_data[baseball_data['handedness']=='L']['avg'].values.tolist()
    no_rain_ridership = subway_data[subway_data['rain']==0]['ENTRIESn_hourly'].values.tolist() 
    print "no_rain_ridership", no_rain_ridership

    mean_rain = (subway_data[subway_data['rain']==1]['ENTRIESn_hourly'].sum() )/ len (rain_ridership)
    print "meain rain", mean_rain

    mean_no_rain = (subway_data[subway_data['rain']==0]['ENTRIESn_hourly'].sum() )/ len (no_rain_ridership)
    print "no mean rain", mean_no_rain

    #print (rightHandBatters)
    t_test_result = scipy.stats.ttest_ind(rain_ridership, no_rain_ridership, equal_var=False)
    #run Welch's t-test
    #print t_test_result

    U, p = scipy.stats.mannwhitneyu(subway_data['ENTRIESn_hourly'][subway_data.rain==1], subway_data['ENTRIESn_hourly'][subway_data.rain==0])

    W, p2 = scipy.stats.shapiro(subway_data['ENTRIESn_hourly'][subway_data.rain==1])
    
    print U, p

    print W, p2

    #return (False, result)

if __name__=="__main__":
    compare_averages("turnstile_data_master_with_weather.csv")

