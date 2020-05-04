import json
from datetime import datetime

from bokeh.embed import json_item
from bokeh.models import DatetimeTickFormatter, HoverTool, Span, Label, Band, ColumnDataSource, Range1d, DataRange1d, \
    CustomJSHover, Legend
from bokeh.palettes import Colorblind8
from bokeh.plotting import figure


class MyPlot:
    # figure
    p = None

    # palette
    palette = list(Colorblind8)

    # NaN hover formatter
    nan_hover_formatter = CustomJSHover(code="""
        if (isNaN(value)) {
            return "-"
        }
        return value.toString();                                                       
    """)

    def __init__(self, figure_name, x_lower_bound=None, x_upper_bound=None, y_lower_bound=None, y_upper_bound=None):
        # set up the figure
        self.p = figure(plot_width=1000, plot_height=400, tools='pan,wheel_zoom,reset',
                        x_axis_type="datetime", toolbar_location=None, name=figure_name,
                        x_range=DataRange1d(x_lower_bound, x_upper_bound, bounds="auto"),
                        y_range=Range1d(y_lower_bound, y_upper_bound, bounds="auto"))
        self.p.sizing_mode = 'scale_width'

        # set up border
        self.p.border_fill_color = "whitesmoke"
        self.p.min_border_top = 15

        # format x axis
        self.p.xaxis.formatter = DatetimeTickFormatter(
            hours=["%B %-d"],
            days=["%B %-d"],
            months=["%B %-d"],
            years=["%B %-d"],
        )

    def add_line(self, x_column, y_column, source, name, legend):
        self.p.line(x=x_column, y=y_column, source=ColumnDataSource(source), name=name,
                    legend_label=legend, color=self.get_next_colour(), line_width=1)

    def add_vertical_bar(self, date, label):
        # create and add span to figure
        # date should be created via datetime.datetime(2001,1,1) or equivalent
        span_date = date.timestamp() * 1000
        vertical_span = Span(location=span_date, dimension='height', line_color=self.palette.pop(), line_dash='dashed',
                             line_width=2)
        span_label = Label(x=span_date, y=10, y_units='screen', text=' ' + label, text_font='helvetica',
                           text_font_size='9pt')

        self.p.add_layout(vertical_span)
        self.p.add_layout(span_label)

    def add_band(self, x_column, source, max_values_column, min_values_column):
        # add a 'confidence interval' or band to the figure
        max_min_interval = Band(base=x_column, lower=max_values_column, upper=min_values_column,
                                source=ColumnDataSource(source), level='underlay', fill_alpha=1.0, line_width=1,
                                line_color='black')
        self.p.add_layout(max_min_interval)

    def add_hover_tool(self, hover_tool):
        self.p.add_tools(hover_tool)

    def create_legend(self):
        # setup legend
        self.p.legend.location = "top_left"
        self.p.legend.click_policy = "hide"
        self.p.legend.label_text_font_size = "8pt"
        self.p.legend.spacing = 0
        self.p.legend.border_line_color = None

    def create_readme_from_template(self):
        # create the legend (note this needs to be done last after all glyphs have been added)
        self.create_legend()

        # create the json data for the plot
        item_text = json.dumps(json_item(self.p, "Plot"))

        with open('../docs/page.template', 'r') as file:
            template = file.read()

        # Replace the target strings
        template = template.replace('{PLACEHOLDER}', item_text)

        now = datetime.now()
        template = template.replace('{DATE}', now.strftime("%d/%m/%Y %H:%M:%S"))

        # Write the file out again
        with open('../docs/README.md', 'w') as file:
            print("Writing new README.md.")
            file.write(template)

    def get_next_colour(self):
        return self.palette.pop()
