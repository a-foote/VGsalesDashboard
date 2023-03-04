import altair as alt
import pandas as pd

alt.data_transformers.disable_max_rows()
df = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])

def sales_hist():
    plot = (alt.Chart(df).mark_bar().encode(
                    alt.X('Global_Sales', bin=alt.Bin(extent=[0, 3], step=0.2), title = 'Sales (millions)', axis=alt.Axis(format='$s')),
                    alt.Y('count()', scale=alt.Scale(type="log"), title = 'Number of Games'),
                    tooltip=['count()']
                )
            .configure_mark(color='red')
           )
    return plot.to_html()
    #plot.show()