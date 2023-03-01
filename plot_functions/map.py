import plotly as px
import pandas as pd
import numpy as np

df = pd.read_csv("./data/vgsales-cleaned.csv", parse_dates=['Year'])
codes = pd.read_csv("./data/plotly_countryCodes.csv")

#wrangling
codes["sales"] = np.NaN
na = ["Canada", "United States", "Mexico", "Nicaragua", "Honduras", "Cuba", "Guatemala", "Panama", "Costa Rica", "Dominican Republic", "Haiti", "Belize", "El Salvador", "Bahamas, The", "Jamaica", "Trinidad and Tobago", "Dominica", "Saint Lucia", "Antigua and Barbuda", "Barbados", "Saint Vincent and the Grenadines", "Grenada", "Saint Kitts and Nevis"]
eu = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']
# #adding names
# codes$names = NA
# codes[codes[,'COUNTRY'] %in% na,'names'] = 'North America'
# codes[codes[,'COUNTRY'] %in% eu,'names'] = 'European Union'
# codes[codes[,'COUNTRY'] == 'Japan','names'] = 'Japan'
# codes[is.na(codes[,'names']),'names'] = 'Other'

for count, value in enumerate(codes):
	if (codes.loc[count, 'COUNTRY'] in na):
		codes.loc[count, 'sales'] = np.sum(df['NA_Sales'])

print(codes.describe())

#figure
#def map_figure():
#	plot = 
	
	
#	return plot

	
#map_figure()
