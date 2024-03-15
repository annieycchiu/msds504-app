import math
import random
import numpy as np
import pandas as pd

import plotly.graph_objs as go
import streamlit as st

colors = {
    'USF_Green': '#00543C',
    'USF_Yellow': '#FDBB30',
    'USF_Gray': '#75787B'
}


## Binomial Distribution

class BinomialDistribution:
    def __init__(self, n, p, size=1, colors=colors):
        self.n = n
        self.p = p
        self.size = size
        self.colors = colors

        self.simulated_data = None
        self.simulate_binomial_dist_data()

        self.x_axis_min = 0
        self.x_axis_max = self.n + 1
        self.x_vals = np.arange(0, self.n + 1)

        self.pmf_probs = None
        self.calculate_pmf()

    def simulate_binomial_dist_data(self):
        """
        Simulate binomial distribution data based on the provided parameters.
        """
        outcomes = np.random.rand(self.size, self.n) < self.p
        self.simulated_data = np.sum(outcomes, axis=1)

    def calculate_pmf(self):
        # Calculate PMF using binomial distribution formula
        self.pmf_probs = np.array([round(math.comb(self.n, k) * (self.p**k) * ((1 - self.p)**(self.n - k)), 3) for k in self.x_vals])

    def plot_theoretical_pmf(self):
        """
        Plot the probability mass function (PMF) for the binomial distribution using Plotly.
        """
        # Define hover text
        hover_temp = '<b>Number of Successes</b>: %{x}<br><b>Probability</b>: %{customdata}'
        customize_data = [f'{round(y * 100, 2)}%' for y in self.pmf_probs]

        # Create stem plot
        fig = go.Figure()

        # Add scatter dots
        fig.add_trace(
            go.Scatter(
                x=self.x_vals, y=self.pmf_probs, 
                mode='markers', marker=dict(color=self.colors['USF_Green']),
                hovertemplate=hover_temp, name='', customdata=customize_data,
                hoverlabel=dict(font=dict(color='white'))))

        # Add vertical stems
        for i in range(len(self.x_vals)):
            fig.add_shape(
                type='line',
                x0=self.x_vals[i], y0=0,
                x1=self.x_vals[i], y1=self.pmf_probs[i],
                line=dict(color=self.colors['USF_Green'], width=2))

        # Set layout
        if max(self.x_vals) <= 30:
            tickvals = self.x_vals
            tickmode = 'array'
        else:
            tickvals = None
            tickmode = 'auto'

        fig.update_layout(
            title="<span style='font-size:18px; font-weight:bold;'>Binomial Distribution Theoretical PMF</span>",
            xaxis_title='Number of Successes',
            yaxis_title='Probability',
            hoverlabel=dict(font=dict(size=14), bgcolor=self.colors['USF_Green']),
            xaxis=dict(tickmode=tickmode, tickvals=tickvals, tickangle=0))
        
        # Show plot
        st.plotly_chart(fig, use_container_width=True)

    def plot_prob_table(self):
        """
        Plot the probability table for the binomial distribution.
        """
        prob_df = pd.DataFrame({'x': self.x_vals, 'P(X=x)': self.pmf_probs})

        # Transpose DataFrame
        transposed_df = prob_df.T

        # Render DataFrame as HTML table with row names but without column names
        html_table = transposed_df.to_html(header=False, index=True)

        # Wrap HTML table within a <div> element with a fixed width and horizontal scrollbar
        html_with_scrollbar = f'<div style="overflow-x:auto;">{html_table}</div>'

        # Display HTML table with horizontal scrollbar
        st.write(html_with_scrollbar, unsafe_allow_html=True)

    def plot_empirial_pmf(self):
        """
        Plot the simulation results using Plotly.
        """
        # Count the occurrences of each value
        unique, count = np.unique(self.simulated_data, return_counts=True)

        y_vals = [0] * (self.n + 1)

        for u, c in zip(unique, count):
            y_vals[u] = c

        # Define hover text
        hover_temp = '<b>Number of Successes</b>: %{x}<br><b>Count</b>: %{y}<br><b>Percentage</b>: %{customdata}'
        customize_data = [f'{round(y/self.size * 100, 2)}%' for y in y_vals]

        # Create bar plot
        fig = go.Figure()

        # Add trace for bar plots
        fig.add_trace(
            trace=go.Bar(
                x=self.x_vals, y=y_vals,
                marker=dict(color=self.colors['USF_Yellow'], opacity=0.8),
                hovertemplate=hover_temp, name='', customdata=customize_data,
                hoverlabel=dict(font=dict(color='white'))))

        # Set layout
        if max(self.x_vals) <= 30:
            tickvals = self.x_vals
            tickmode = 'array'
        else:
            tickvals = None
            tickmode = 'auto'

        fig.update_layout(
            go.Layout(
                title="<span style='font-size:18px; font-weight:bold;'>Binomial Distribution Empirial PMF (Simulation)</span>",
                xaxis_title='Number of Successes',
                yaxis_title='Frequency (Count)',
                hoverlabel=dict(font=dict(size=14), bgcolor=self.colors['USF_Yellow']),
                xaxis=dict(tickmode=tickmode, tickvals=tickvals, tickangle=0)))
            
        # Show plot 
        st.plotly_chart(fig, use_container_width=True)