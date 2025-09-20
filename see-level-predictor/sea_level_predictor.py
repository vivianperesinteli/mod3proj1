import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    plt.plot(years_extended, res.intercept + res.slope * years_extended, "r", label="Linha de Regressão Original")

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent_extended = pd.Series([i for i in range(2000, 2051)])
    plt.plot(years_recent_extended, res_recent.intercept + res_recent.slope * years_recent_extended, "g", label="Linha de Regressão (2000-presente)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()