import logging
# from systemd.journal import JournaldLogHandler

from numpy.random import random
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import column, widgetbox
from bokeh.models import Button, ColumnDataSource
from bokeh.server.server import Server

"""
create and run a demo bokeh app on a cloud server
"""

"""
Logging
"""
# # get an instance of the logger object this module will use
# logger = logging.getLogger(__name__)
# # instantiate the JournaldLogHandler to hook into systemd
# journald_handler = JournaldLogHandler()
# # set a formatter to include the level name
# journald_handler.setFormatter(logging.Formatter(
#     '[%(levelname)s] %(message)s'
# ))
# # add the journald handler to the current logger
# logger.addHandler(journald_handler)

# # optionally set the logging level
# logger.setLevel(logging.DEBUG)
"""
End log
"""

def run(doc):

    fig = figure(title='random data', width=400, height=200, tools='pan,box_zoom,reset,save')

    source = ColumnDataSource(data={'x': [], 'y': []})
    fig.line('x', 'y', source=source)

    def click(n=100):
        source.data = {'x': range(n), 'y': random(n)}

    button = Button(label='update', button_type='success')
    button.on_click(click)

    layout = column(widgetbox(button), fig)
    doc.add_root(layout)
    click()

# configure and run bokeh server
# kws = {'port': 5006, 'prefix': '/bokeh', 'allow_websocket_origin': ['34.89.113.193','34.89.113.193:5006','34.89.113.193:5000']}
kws = {'port': 5006, 'prefix': '/bokeh', 'allow_websocket_origin': ['34.89.113.193']}

server = Server(run, **kws)
server.start()

if __name__ == '__main__':
    # logger.info(
    #     'Starting Bokeh Server on http://localhost:5006/bokeh'
    # )
    # print()
    server.io_loop.add_callback(server.show, '/')
    server.io_loop.start()
