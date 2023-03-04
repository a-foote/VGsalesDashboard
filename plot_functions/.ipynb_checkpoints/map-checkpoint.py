import plotly.express as px
import pandas as pd
import numpy as np
import math

df = pd.read_csv("./data/vgsales-cleaned.csv", parse_dates=['Year'])
codes = pd.read_csv("./data/plotly_countryCodes.csv")
codes.drop(labels=['GDP (BILLIONS)'], axis=1, inplace=True)

#wrangling
codes["sales"] = np.NaN
codes["names"] = np.NaN
na = ["Canada", "United States", "Mexico", "Nicaragua", "Honduras", "Cuba", "Guatemala", "Panama", "Costa Rica", "Dominican Republic", "Haiti", "Belize", "El Salvador", "Bahamas, The", "Jamaica", "Trinidad and Tobago", "Dominica", "Saint Lucia", "Antigua and Barbuda", "Barbados", "Saint Vincent and the Grenadines", "Grenada", "Saint Kitts and Nevis"]
eu = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']


for count, value in enumerate(codes['COUNTRY']):
	if (value in na):
		codes.loc[count, 'sales'] = np.sum(df['NA_Sales'])
		codes.loc[count, 'names'] = 'North America'
	if (value in eu):
		codes.loc[count, 'sales'] = np.sum(df['EU_Sales'])
		codes.loc[count, 'names'] = 'European Union'
	if (value == 'Japan'):
		codes.loc[count, 'sales'] = np.sum(df['JP_Sales'])
		codes.loc[count, 'names'] = 'Japan'
	if (math.isnan(codes.loc[count, 'sales'])):
		codes.loc[count, 'sales'] = np.sum(df['Other_Sales'])
		codes.loc[count, 'names'] = 'Other'


#figure
def map_figure():
	return px.choropleth(codes, locations="CODE", color="sales", hover_name="names", color_continuous_scale=px.colors.sequential.Plasma)

	
#map_figure()
