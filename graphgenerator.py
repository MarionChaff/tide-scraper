import plotly.graph_objects as go
from plotly.subplots import make_subplots

class TideGraphGenerator:

    def __init__(self, tides_x, tides_y):
        self.tides_x = tides_x
        self.tides_y = tides_y
        self.plot = self.create_tide_graphs()

    def create_tide_graphs(self):

        fig = make_subplots()

        # Plot the main tide line
        fig.add_trace(go.Scatter(x = self.tides_x, y = self.tides_y,
                                 mode ='lines', name = 'hauteur',
                                 line = dict(color = '#0B4C82', width = 2),
                                 showlegend = False,
                                 hovertemplate='%{x|%H:%M}<br>%{y:.2f}m'))

        # Finetune formatting
        fig.update_yaxes(tickformat=',.0f', range=[max(min(self.tides_y), 0) - 0.5, max(self.tides_y) + 0.5])
        fig.update_xaxes(tickformat='%Hh', dtick=3600000)

        fig.update_layout(
            font=dict(family="Quicksand, sans-serif", size=14, weight="bold"),
            xaxis=dict(showgrid=True, gridcolor='#F2EFEF', tickcolor='gray', linecolor='lightgrey'),
            yaxis=dict(showgrid=True, gridcolor='#F2EFEF', tickcolor='gray', linecolor='lightgrey', ticksuffix='m'),
            plot_bgcolor='rgba(255, 255, 255, 0.8)',
            showlegend=False,
            margin=dict(l=10, r=10, t=20, b=10),
            width=800,
            height=400,
            paper_bgcolor='rgba(0,0,0,0)'
            )

        fig.show()

        return fig
