import altair as alt
import pandas as pd

alt.data_transformers.disable_max_rows()

#df = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])

def heatmap():
    plot = (alt.Chart(df).mark_rect().encode(
                    alt.X('Platform_grouped', title = 'Platform', axis=alt.Axis(labelAngle=-45)),
                    alt.Y('Genre'),
                    color = alt.Color('count()',title ='Games Count', scale=alt.Scale(scheme='lightgreyred')),
                    tooltip=['count()']
                )
            .properties(width=500, height=500)
            .interactive()
           )
    return plot.to_html()
    #plot.show()