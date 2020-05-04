import datetime

from bokeh.io import output_file, show
import pandas as pd
import numpy as np

from helpers import plot_helpers

# set up a data source
df = pd.DataFrame()
df['dates'] = pd.date_range('2020-01-01', '2020-05-01')
df.set_index(['dates'])
df['values'] = np.random.randint(0, 5, size=len(df))
df['max_expected'] = np.random.randint(4, 8, size=len(df))
df['min_expected'] = np.random.randint(-2, 2, size=len(df))

# set up the plot
my_plot = plot_helpers.MyPlot("test_plot", x_lower_bound=min(df['dates']), x_upper_bound=(max(df['dates'])),
                              y_lower_bound=min(df['min_expected']) - 5, y_upper_bound=max(df['max_expected']) + 5)
my_plot.add_line('dates', 'values', df, 'random', 'Random Line')
my_plot.add_vertical_bar(datetime.datetime(2020, 2, 1), 'test_span')
my_plot.add_band('dates', df, 'max_expected', 'min_expected')
# my_plot.create_legend()

my_plot.create_readme_from_template()

# # output the plot
# output_file("../docs/test.html", title='test_plot')
# show(my_plot.p)
