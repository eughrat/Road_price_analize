import pandas as pd
import matplotlib.pyplot as plt


def bar_plot_cost_by_road(data, agg_category:dict, sort_category, x_axis, y_axis, chart_label,cost_category = 'Droga'):

    data.groupby([cost_category], as_index=False).agg(agg_category).sort_values(by=sort_category,ascending=False).plot.bar(x=x_axis, y=y_axis, label=chart_label)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.figure(figsize=(12, 8))
    plt.show()