import altair as alt
import pandas as pd

alt.data_transformers.disable_max_rows()

df = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])

def piechart():
    plot = (alt.Chart(df).mark_arc().encode(
                    theta=alt.Theta(
                        field='Platform_grouped',
                        aggregate='count'
                    ),
                    color=alt.Color(
                        field='Platform_grouped',
                        legend=None
                    ),
                    tooltip = ['Platform_grouped','count(Platform_grouped):Q']
                )             
           )
    return plot.to_html()
    #plot.show()