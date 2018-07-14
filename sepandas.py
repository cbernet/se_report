import pandas as pd
pd.set_option('max_colwidth', 200)
    
location = 'data/dump.csv'
print 'reading'
df = pd.read_csv(location)
df.info()

# adding a user column by parsing the filename
print 'adding user'
df['user'] = df['path'].str.split('/',expand=True)[8]

# generating a size column (missing size at the moment)
print 'generating size'
import numpy as np
df['size'] = np.random.randint(1,100, df.shape[0])

# directory
df['dir'] = df['path'].str.extract('(.*)\/(.*)',expand=True)[0]

# access date
df['adt'] = pd.to_datetime(df['atime'],unit='s')


# filtering large files
print 'filtering large files'
minsize = 1
dl = df[df['size']>minsize]

# sorting by user and size
# dus = dl.sort_values(by=['user', 'size'], ascending=[True, False])

# group by user then directory, sum all numbers (including time...), and sort by user and then by decreasing size
print 'analysis'
maxtime = pd.Timestamp('2017-01-01')
dlold = dl[dl['adt']<maxtime]
group = dlold.groupby(['user', 'dir'])
res = group.agg({'size':'sum','adt':'max'}).sort_values(by=['user', 'size'],ascending=[True, False])  
print res
print res.loc['sviret']

# need to find a way to get the last atime for each directory
