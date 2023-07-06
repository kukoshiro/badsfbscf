import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')
df.dropna()
df.info()
print(df['Rating.1'].value_counts())
horror_count = 0
horror_rating = 0
dram_count = 0
dram_rating = 0
def drama_average(row):
    global horror_count, horror_rating
    if row['Genre'].find('Horror')!=-1:
        horror_rating += row['Rating.1']
        horror_count +=1
    global dram_count, dram_rating
    if row['Genre'].find('Drama')!=-1:
        dram_rating += row['Rating.1']
        dram_count +=1
    return False

df.apply(drama_average, axis = 1)
print('средний рейтинг комедий',round(dram_rating/dram_count, 2))
print('средний рейтинг хорроров',round(horror_rating/horror_count, 2))


# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('IMDB-Movie-Data.csv')
# # df.info()
# # df['Rating'] = df['Rating'].apply(int)
# print(df.head())