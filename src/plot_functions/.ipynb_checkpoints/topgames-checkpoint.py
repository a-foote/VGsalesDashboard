import altair as alt
import pandas as pd

alt.data_transformers.disable_max_rows()

df = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])
df['Year'] = df['Year'].dt.year.astype('Int64')

def topgames():
    plot = (alt.Chart(df[:5]).mark_bar().encode(
                    alt.X('Global_Sales', title = 'Sales (millions)', axis=alt.Axis(format='$s')),
                    alt.Y('Name', title ='Game Name', sort='x'),
                    tooltip=['Rank','Year','Platform','Publisher']
                ).configure_mark(
                    color='red'
                ).interactive()                
           )
    return plot.to_html()
    #plot.show()