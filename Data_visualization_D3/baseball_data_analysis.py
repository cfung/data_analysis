import pandas as pd
import numpy as np

df = pd.read_csv('baseball_data.csv')

print 'total HR avg', df['HR'].mean()
print 'R HR avg', df.loc[df['handedness']=='R']['HR'].mean()
print 'L HR avg', df.loc[df['handedness']=='L']['HR'].mean()
print 'B HR avg', df.loc[df['handedness']=='B']['HR'].mean()
print "*****"
print 'total batting avg', df['HR'].mean()
print 'R batting avg', df.loc[df['handedness']=='R']['avg'].mean()
print 'L batting avg', df.loc[df['handedness']=='L']['avg'].mean()
print 'B batting avg', df.loc[df['handedness']=='B']['avg'].mean()

print "count of 0 batting avg..", df.loc[df['avg']==0].stack().count()

print "count of R..", df.loc[df['handedness']=='R'].stack().count()
print "count of L..", df.loc[df['handedness']=='L'].stack().count()
print "count of B..", df.loc[df['handedness']=='B'].stack().count()

print 'R batting avg AND not 0: ', df.loc[(df['handedness']=='R') & (df['avg'] != 0)]['avg'].mean()
print 'L batting avg AND not 0: ', df.loc[(df['handedness']=='L') & (df['avg'] != 0)]['avg'].mean()
print 'B batting avg AND not 0: ', df.loc[(df['handedness']=='B') & (df['avg'] != 0)]['avg'].mean()