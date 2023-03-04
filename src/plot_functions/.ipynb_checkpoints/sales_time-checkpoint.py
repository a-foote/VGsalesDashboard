import altair as alt
#import pandas as pd

alt.data_transformers.disable_max_rows()

#df = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])

def sales_time(df):
    plot = (alt.Chart(df, title='Total Regional Sales').mark_circle().encode(
                    alt.X('Year:T',scale=alt.Scale(zero=False), title=None), 
                    alt.Y('sum(Global_Sales)', title='Sum of Sales (millions)', axis=alt.Axis(format='$s'))
                )
           )
    
    band = (alt.Chart(df).mark_errorband(extent='ci').encode(
                    x='Year',
                    y='Global_Sales'
                )
    
           )
    
    final_plot = (plot + band).configure_mark(color='red')
    return final_plot.to_html()
    #final_plot.show()