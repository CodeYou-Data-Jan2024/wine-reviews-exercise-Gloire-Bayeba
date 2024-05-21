import pandas as pd

Wine_reviews= pd.read_csv('data/winemag-data-130k-v2.csv.zip', index_col=0)

Country_review= Wine_reviews.country.value_counts()

country_average=Wine_reviews.groupby('country') .points.mean() .round(decimals=1)

compiled= pd.DataFrame({'count':Country_review, 'points': country_average})

final_data= compiled.sort_values('count', ascending=0)

final_data.to_csv('reviews-per-country.csv')
        




