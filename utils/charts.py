import plotly.express as px

def create_bar_chart(df):

    fig = px.bar(
        df,
        x="Crop",
        y="Images",
        color="Crop",
        text="Images"
    )

    return fig
