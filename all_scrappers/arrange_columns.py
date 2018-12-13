

import pandas as pd

df=pd.read_csv(r'D:\YK Python\homedepot\homedepot\homedepot_productinfo_10-07-2018_part1.csv')

df1=df[['modelnumber', 'title', 'response_url', 'ratings', 'reviews', 'price', 'brand', 'ship_to_home', 'pick_up_at_store', 'breadcrumb', 'node_1', 'node_2', 'node_3', 'node_4', 'node_5', 'node_6', 'home_installation', 'no_of_accessories', 'no_of_images', 'no_of_videos']]

df1.to_csv(r'D:\YK Python\homedepot\homedepot\homedepot_productinfo_10-07-2018_part1_ordered.csv')