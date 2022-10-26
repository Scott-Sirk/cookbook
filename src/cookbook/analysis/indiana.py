
import numpy as np
from cookbook.analysis.general import General
from cookbook.collect.web import Indiana_Web_API

class Indiana_Analysis(General):
    def __init__(self):
        super().__init__()
        self.api = Indiana_Web_API()

    def covid_vax_data(self):

        df = self.api.query_data('c496b384-f543-417e-912f-995caebf5fc0')

        df['eligible_population'] = df['eligible_population'].replace('Suppressed', np.nan).astype(float)
        df['fully_vaccinated'] = df['fully_vaccinated'].replace('Suppressed', np.nan).astype(float)

        df['percent_fully_vaccinated'] = (df['fully_vaccinated']/df['eligible_population'])*100

        print(df.columns)
        print(df)
        summary = df['percent_fully_vaccinated'].describe()
        print(summary)
        q1 = summary['25%']
        q2 = summary['50%']
        q3 = summary['75%']

        print( df['zip_cd'][df['percent_fully_vaccinated']<q1] )
        print( df['zip_cd'][(df['percent_fully_vaccinated']>q1) & (df['percent_fully_vaccinated']<q2)] )
        print( df['zip_cd'][(df['percent_fully_vaccinated']>q2) & (df['percent_fully_vaccinated']<q3)] )
        print( df['zip_cd'][df['percent_fully_vaccinated']>q3] )

        #make bar graph?  -proba dist.
        #display rate vax over zip code map?
        ##https://towardsdatascience.com/redlining-mapping-inequality-in-peer-2-peer-lending-using-geopandas-part-2-9d8af584df0b


ia = Indiana_Analysis()
ia.covid_vax_data()
