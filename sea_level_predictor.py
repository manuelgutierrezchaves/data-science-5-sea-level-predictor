import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    fig, ax = plt.subplots()
    plt.scatter(x, y, c = 'red')

    # Create first line of best fit
    reg = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051, 1)])
    y_pred = reg.intercept + reg.slope * x_pred
    plt.plot(x_pred, y_pred, 'g')

    # Create second line of best fit
    df_modern = df.query("Year >= 2000")
    x_modern = df_modern["Year"]
    y_modern = df_modern["CSIRO Adjusted Sea Level"]
    reg_modern = linregress(x_modern, y_modern)
    x_modern_pred = pd.Series([i for i in range(2000, 2051, 1)])
    y_modern_pred = reg_modern.intercept + reg_modern.slope * x_modern_pred
    plt.plot(x_modern_pred, y_modern_pred, 'r')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()