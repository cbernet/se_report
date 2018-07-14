import pandas as pd
location = 'data/dump_small.csv'
df = pd.read_csv(location)
df.info()

# adding a user column by parsing the filename
df['user'] = df['path'].str.split('/',expand=True)[8]

# generating a size column (missing size at the moment)
import numpy as np
df['size'] = np.random.randint(1,100, df.shape[0])
df['dir'] = df['path'].str.extract('(.*)\/(.*)',expand=True)[0]

# filtering large files
minsize = 80
dl = df[df['size']>minsize]

# sorting by user and size
dus = dl.sort_values(by=['user', 'size'], ascending=[True, False])

# group by user then directory, sum, and sort by user and then by decreasing size
dl.groupby(['user', 'dir']).sum().sort_values(by=['user', 'size'],ascending=[True, False])
