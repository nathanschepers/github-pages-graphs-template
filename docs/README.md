<script src="https://cdn.bokeh.org/bokeh/release/bokeh-2.0.1.min.js"></script>
# Graph Template for github pages graphs
By: <nathan.schepers@protonmail.com>

<div id="Plot"></div>
---
## The Plot

## Footnotes

---
Updated on: 04/05/2020 20:11:20

<script>
    item_text = {"target_id": "Plot", "root_id": "1004", "doc": {"roots": {"references": [{"attributes": {}, "id": "1007", "type": "LinearScale"}, {"attributes": {"months": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}, "id": "1046", "type": "MonthsTicker"}, {"attributes": {}, "id": "1078", "type": "UnionRenderers"}, {"attributes": {"data_source": {"id": "1028"}, "glyph": {"id": "1030"}, "hover_glyph": null, "muted_glyph": null, "name": "random", "nonselection_glyph": {"id": "1031"}, "selection_glyph": null, "view": {"id": "1033"}}, "id": "1032", "type": "GlyphRenderer"}, {"attributes": {}, "id": "1009", "type": "LinearScale"}, {"attributes": {"months": [0, 2, 4, 6, 8, 10]}, "id": "1047", "type": "MonthsTicker"}, {"attributes": {}, "id": "1037", "type": "BasicTickFormatter"}, {"attributes": {"below": [{"id": "1011"}], "border_fill_color": "whitesmoke", "center": [{"id": "1014"}, {"id": "1018"}, {"id": "1051"}, {"id": "1053"}, {"id": "1054"}, {"id": "1056"}], "left": [{"id": "1015"}], "min_border_top": 15, "name": "test_plot", "plot_height": 400, "plot_width": 1000, "renderers": [{"id": "1032"}], "sizing_mode": "scale_width", "title": {"id": "1035"}, "toolbar": {"id": "1022"}, "toolbar_location": null, "x_range": {"id": "1002"}, "x_scale": {"id": "1007"}, "y_range": {"id": "1003"}, "y_scale": {"id": "1009"}}, "id": "1004", "subtype": "Figure", "type": "Plot"}, {"attributes": {"months": [0, 4, 8]}, "id": "1048", "type": "MonthsTicker"}, {"attributes": {"formatter": {"id": "1026"}, "ticker": {"id": "1012"}}, "id": "1011", "type": "DatetimeAxis"}, {"attributes": {"bounds": "auto", "end": 12, "start": -7}, "id": "1003", "type": "Range1d"}, {"attributes": {"data": {"dates": {"__ndarray__": "AACAbub1dkIAAEDUOPZ2QgAAADqL9nZCAADAn932dkIAAIAFMPd2QgAAQGuC93ZCAAAA0dT3dkIAAMA2J/h2QgAAgJx5+HZCAABAAsz4dkIAAABoHvl2QgAAwM1w+XZCAACAM8P5dkIAAECZFfp2QgAAAP9n+nZCAADAZLr6dkIAAIDKDPt2QgAAQDBf+3ZCAAAAlrH7dkIAAMD7A/x2QgAAgGFW/HZCAABAx6j8dkIAAAAt+/x2QgAAwJJN/XZCAACA+J/9dkIAAEBe8v12QgAAAMRE/nZCAADAKZf+dkIAAICP6f52QgAAQPU7/3ZCAAAAW47/dkIAAMDA4P92QgAAgCYzAHdCAABAjIUAd0IAAADy1wB3QgAAwFcqAXdCAACAvXwBd0IAAEAjzwF3QgAAAIkhAndCAADA7nMCd0IAAIBUxgJ3QgAAQLoYA3dCAAAAIGsDd0IAAMCFvQN3QgAAgOsPBHdCAABAUWIEd0IAAAC3tAR3QgAAwBwHBXdCAACAglkFd0IAAEDoqwV3QgAAAE7+BXdCAADAs1AGd0IAAIAZowZ3QgAAQH/1BndCAAAA5UcHd0IAAMBKmgd3QgAAgLDsB3dCAABAFj8Id0IAAAB8kQh3QgAAwOHjCHdCAACARzYJd0IAAECtiAl3QgAAABPbCXdCAADAeC0Kd0IAAIDefwp3QgAAQETSCndCAAAAqiQLd0IAAMAPdwt3QgAAgHXJC3dCAABA2xsMd0IAAABBbgx3QgAAwKbADHdCAACADBMNd0IAAEByZQ13QgAAANi3DXdCAADAPQoOd0IAAICjXA53QgAAQAmvDndCAAAAbwEPd0IAAMDUUw93QgAAgDqmD3dCAABAoPgPd0IAAAAGSxB3QgAAwGudEHdCAACA0e8Qd0IAAEA3QhF3QgAAAJ2UEXdCAADAAucRd0IAAIBoORJ3QgAAQM6LEndCAAAANN4Sd0IAAMCZMBN3QgAAgP+CE3dCAABAZdUTd0IAAADLJxR3QgAAwDB6FHdCAACAlswUd0IAAED8HhV3QgAAAGJxFXdCAADAx8MVd0IAAIAtFhZ3QgAAQJNoFndCAAAA+boWd0IAAMBeDRd3QgAAgMRfF3dCAABAKrIXd0IAAACQBBh3QgAAwPVWGHdCAACAW6kYd0IAAEDB+xh3QgAAACdOGXdCAADAjKAZd0IAAIDy8hl3QgAAQFhFGndCAAAAvpcad0IAAMAj6hp3QgAAgIk8G3dCAABA744bd0IAAABV4Rt3QgAAwLozHHdCAACAIIYcd0IAAECG2Bx3Qg==", "dtype": "float64", "shape": [122]}, "index": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121], "max_expected": [4, 7, 7, 5, 5, 7, 4, 6, 4, 5, 6, 7, 4, 4, 5, 6, 6, 4, 6, 5, 7, 5, 7, 6, 6, 6, 4, 4, 4, 6, 5, 5, 7, 4, 5, 5, 4, 5, 6, 6, 5, 7, 5, 5, 6, 7, 6, 5, 5, 4, 4, 6, 5, 5, 4, 4, 6, 7, 6, 7, 6, 7, 4, 7, 7, 4, 6, 5, 6, 4, 6, 7, 6, 6, 5, 6, 4, 6, 5, 7, 6, 4, 5, 7, 5, 4, 5, 4, 6, 6, 5, 4, 4, 5, 7, 5, 7, 5, 5, 5, 4, 4, 5, 6, 5, 5, 6, 6, 6, 5, 5, 6, 7, 5, 6, 7, 5, 5, 5, 4, 7, 6], "min_expected": [-1, 1, 0, 1, 0, -2, -2, -1, -2, 1, -1, 0, 0, -2, -2, 0, 1, -2, -1, 0, -2, -1, 1, -1, 1, 0, 0, -1, 1, 0, 0, -1, -2, -2, -2, -1, 0, 0, 0, 0, 0, 0, -2, -2, -1, -2, 1, -1, 0, -2, 1, -1, -1, -1, 0, 1, -2, 1, 1, 1, 0, 1, -1, 1, 1, -1, 0, 1, 0, 1, 1, -1, -2, 1, 1, -1, 1, -2, 1, -1, 0, -1, -1, -2, -2, -1, -2, -1, -2, -1, -1, 1, -2, -1, 1, -2, 1, -1, 1, 1, -2, -2, -1, -2, 1, 1, 0, 1, 0, 1, 0, -2, 1, 1, -1, -2, 0, 0, 1, 0, -2, -2], "values": [0, 1, 4, 0, 4, 3, 0, 3, 2, 2, 1, 4, 1, 2, 2, 0, 3, 1, 2, 0, 3, 0, 3, 3, 2, 4, 4, 0, 3, 1, 0, 3, 2, 3, 1, 3, 4, 4, 4, 3, 3, 3, 2, 3, 1, 4, 1, 3, 3, 1, 4, 3, 0, 3, 0, 4, 4, 2, 4, 3, 1, 1, 3, 2, 1, 2, 2, 2, 2, 2, 0, 2, 1, 1, 4, 3, 2, 3, 2, 2, 0, 2, 2, 4, 3, 0, 0, 1, 3, 4, 1, 3, 3, 3, 2, 2, 4, 0, 4, 3, 1, 4, 4, 4, 2, 4, 4, 0, 3, 1, 3, 3, 1, 0, 0, 0, 1, 4, 1, 0, 1, 0]}, "selected": {"id": "1075"}, "selection_policy": {"id": "1076"}}, "id": "1028", "type": "ColumnDataSource"}, {"attributes": {"months": [0, 6]}, "id": "1049", "type": "MonthsTicker"}, {"attributes": {"border_line_color": null, "click_policy": "hide", "items": [{"id": "1052"}], "label_text_font_size": "8pt", "location": "top_left", "spacing": 0}, "id": "1051", "type": "Legend"}, {"attributes": {"mantissas": [1, 2, 5], "max_interval": 500.0, "num_minor_ticks": 0}, "id": "1039", "type": "AdaptiveTicker"}, {"attributes": {}, "id": "1050", "type": "YearsTicker"}, {"attributes": {"dimension": "height", "line_color": "#CC79A7", "line_dash": [6], "line_width": 2, "location": 1580515200000.0}, "id": "1053", "type": "Span"}, {"attributes": {"label": {"value": "Random Line"}, "renderers": [{"id": "1032"}]}, "id": "1052", "type": "LegendItem"}, {"attributes": {"axis": {"id": "1015"}, "dimension": 1, "ticker": null}, "id": "1018", "type": "Grid"}, {"attributes": {"text": " test_span", "text_font_size": "9pt", "x": 1580515200000.0, "y": 10, "y_units": "screen"}, "id": "1054", "type": "Label"}, {"attributes": {"num_minor_ticks": 5, "tickers": [{"id": "1039"}, {"id": "1040"}, {"id": "1041"}, {"id": "1042"}, {"id": "1043"}, {"id": "1044"}, {"id": "1045"}, {"id": "1046"}, {"id": "1047"}, {"id": "1048"}, {"id": "1049"}, {"id": "1050"}]}, "id": "1012", "type": "DatetimeTicker"}, {"attributes": {"text": ""}, "id": "1035", "type": "Title"}, {"attributes": {"days": [1, 15]}, "id": "1045", "type": "DaysTicker"}, {"attributes": {"axis": {"id": "1011"}, "ticker": null}, "id": "1014", "type": "Grid"}, {"attributes": {"source": {"id": "1028"}}, "id": "1033", "type": "CDSView"}, {"attributes": {"data": {"dates": {"__ndarray__": "AACAbub1dkIAAEDUOPZ2QgAAADqL9nZCAADAn932dkIAAIAFMPd2QgAAQGuC93ZCAAAA0dT3dkIAAMA2J/h2QgAAgJx5+HZCAABAAsz4dkIAAABoHvl2QgAAwM1w+XZCAACAM8P5dkIAAECZFfp2QgAAAP9n+nZCAADAZLr6dkIAAIDKDPt2QgAAQDBf+3ZCAAAAlrH7dkIAAMD7A/x2QgAAgGFW/HZCAABAx6j8dkIAAAAt+/x2QgAAwJJN/XZCAACA+J/9dkIAAEBe8v12QgAAAMRE/nZCAADAKZf+dkIAAICP6f52QgAAQPU7/3ZCAAAAW47/dkIAAMDA4P92QgAAgCYzAHdCAABAjIUAd0IAAADy1wB3QgAAwFcqAXdCAACAvXwBd0IAAEAjzwF3QgAAAIkhAndCAADA7nMCd0IAAIBUxgJ3QgAAQLoYA3dCAAAAIGsDd0IAAMCFvQN3QgAAgOsPBHdCAABAUWIEd0IAAAC3tAR3QgAAwBwHBXdCAACAglkFd0IAAEDoqwV3QgAAAE7+BXdCAADAs1AGd0IAAIAZowZ3QgAAQH/1BndCAAAA5UcHd0IAAMBKmgd3QgAAgLDsB3dCAABAFj8Id0IAAAB8kQh3QgAAwOHjCHdCAACARzYJd0IAAECtiAl3QgAAABPbCXdCAADAeC0Kd0IAAIDefwp3QgAAQETSCndCAAAAqiQLd0IAAMAPdwt3QgAAgHXJC3dCAABA2xsMd0IAAABBbgx3QgAAwKbADHdCAACADBMNd0IAAEByZQ13QgAAANi3DXdCAADAPQoOd0IAAICjXA53QgAAQAmvDndCAAAAbwEPd0IAAMDUUw93QgAAgDqmD3dCAABAoPgPd0IAAAAGSxB3QgAAwGudEHdCAACA0e8Qd0IAAEA3QhF3QgAAAJ2UEXdCAADAAucRd0IAAIBoORJ3QgAAQM6LEndCAAAANN4Sd0IAAMCZMBN3QgAAgP+CE3dCAABAZdUTd0IAAADLJxR3QgAAwDB6FHdCAACAlswUd0IAAED8HhV3QgAAAGJxFXdCAADAx8MVd0IAAIAtFhZ3QgAAQJNoFndCAAAA+boWd0IAAMBeDRd3QgAAgMRfF3dCAABAKrIXd0IAAACQBBh3QgAAwPVWGHdCAACAW6kYd0IAAEDB+xh3QgAAACdOGXdCAADAjKAZd0IAAIDy8hl3QgAAQFhFGndCAAAAvpcad0IAAMAj6hp3QgAAgIk8G3dCAABA744bd0IAAABV4Rt3QgAAwLozHHdCAACAIIYcd0IAAECG2Bx3Qg==", "dtype": "float64", "shape": [122]}, "index": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121], "max_expected": [4, 7, 7, 5, 5, 7, 4, 6, 4, 5, 6, 7, 4, 4, 5, 6, 6, 4, 6, 5, 7, 5, 7, 6, 6, 6, 4, 4, 4, 6, 5, 5, 7, 4, 5, 5, 4, 5, 6, 6, 5, 7, 5, 5, 6, 7, 6, 5, 5, 4, 4, 6, 5, 5, 4, 4, 6, 7, 6, 7, 6, 7, 4, 7, 7, 4, 6, 5, 6, 4, 6, 7, 6, 6, 5, 6, 4, 6, 5, 7, 6, 4, 5, 7, 5, 4, 5, 4, 6, 6, 5, 4, 4, 5, 7, 5, 7, 5, 5, 5, 4, 4, 5, 6, 5, 5, 6, 6, 6, 5, 5, 6, 7, 5, 6, 7, 5, 5, 5, 4, 7, 6], "min_expected": [-1, 1, 0, 1, 0, -2, -2, -1, -2, 1, -1, 0, 0, -2, -2, 0, 1, -2, -1, 0, -2, -1, 1, -1, 1, 0, 0, -1, 1, 0, 0, -1, -2, -2, -2, -1, 0, 0, 0, 0, 0, 0, -2, -2, -1, -2, 1, -1, 0, -2, 1, -1, -1, -1, 0, 1, -2, 1, 1, 1, 0, 1, -1, 1, 1, -1, 0, 1, 0, 1, 1, -1, -2, 1, 1, -1, 1, -2, 1, -1, 0, -1, -1, -2, -2, -1, -2, -1, -2, -1, -1, 1, -2, -1, 1, -2, 1, -1, 1, 1, -2, -2, -1, -2, 1, 1, 0, 1, 0, 1, 0, -2, 1, 1, -1, -2, 0, 0, 1, 0, -2, -2], "values": [0, 1, 4, 0, 4, 3, 0, 3, 2, 2, 1, 4, 1, 2, 2, 0, 3, 1, 2, 0, 3, 0, 3, 3, 2, 4, 4, 0, 3, 1, 0, 3, 2, 3, 1, 3, 4, 4, 4, 3, 3, 3, 2, 3, 1, 4, 1, 3, 3, 1, 4, 3, 0, 3, 0, 4, 4, 2, 4, 3, 1, 1, 3, 2, 1, 2, 2, 2, 2, 2, 0, 2, 1, 1, 4, 3, 2, 3, 2, 2, 0, 2, 2, 4, 3, 0, 0, 1, 3, 4, 1, 3, 3, 3, 2, 2, 4, 0, 4, 3, 1, 4, 4, 4, 2, 4, 4, 0, 3, 1, 3, 3, 1, 0, 0, 0, 1, 4, 1, 0, 1, 0]}, "selected": {"id": "1077"}, "selection_policy": {"id": "1078"}}, "id": "1055", "type": "ColumnDataSource"}, {"attributes": {}, "id": "1016", "type": "BasicTicker"}, {"attributes": {"days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]}, "id": "1042", "type": "DaysTicker"}, {"attributes": {"formatter": {"id": "1037"}, "ticker": {"id": "1016"}}, "id": "1015", "type": "LinearAxis"}, {"attributes": {"bounds": "auto"}, "id": "1002", "type": "DataRange1d"}, {"attributes": {"days": [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]}, "id": "1043", "type": "DaysTicker"}, {"attributes": {}, "id": "1077", "type": "Selection"}, {"attributes": {"days": ["%B %-d"], "hours": ["%B %-d"], "months": ["%B %-d"], "years": ["%B %-d"]}, "id": "1026", "type": "DatetimeTickFormatter"}, {"attributes": {"line_alpha": 0.1, "line_color": "#000000", "x": {"field": "dates"}, "y": {"field": "values"}}, "id": "1031", "type": "Line"}, {"attributes": {}, "id": "1076", "type": "UnionRenderers"}, {"attributes": {"base": {"field": "dates", "units": "data"}, "fill_alpha": 1.0, "level": "underlay", "line_color": "black", "lower": {"field": "max_expected", "units": "data"}, "source": {"id": "1055"}, "upper": {"field": "min_expected", "units": "data"}}, "id": "1056", "type": "Band"}, {"attributes": {}, "id": "1019", "type": "PanTool"}, {"attributes": {"base": 24, "mantissas": [1, 2, 4, 6, 8, 12], "max_interval": 43200000.0, "min_interval": 3600000.0, "num_minor_ticks": 0}, "id": "1041", "type": "AdaptiveTicker"}, {"attributes": {}, "id": "1020", "type": "WheelZoomTool"}, {"attributes": {"days": [1, 8, 15, 22]}, "id": "1044", "type": "DaysTicker"}, {"attributes": {"active_drag": "auto", "active_inspect": "auto", "active_multi": null, "active_scroll": "auto", "active_tap": "auto", "tools": [{"id": "1019"}, {"id": "1020"}, {"id": "1021"}]}, "id": "1022", "type": "Toolbar"}, {"attributes": {"base": 60, "mantissas": [1, 2, 5, 10, 15, 20, 30], "max_interval": 1800000.0, "min_interval": 1000.0, "num_minor_ticks": 0}, "id": "1040", "type": "AdaptiveTicker"}, {"attributes": {}, "id": "1021", "type": "ResetTool"}, {"attributes": {}, "id": "1075", "type": "Selection"}, {"attributes": {"line_color": "#000000", "x": {"field": "dates"}, "y": {"field": "values"}}, "id": "1030", "type": "Line"}], "root_ids": ["1004"]}, "title": "", "version": "2.0.2"}};
    Bokeh.embed.embed_item(item_text);
</script>