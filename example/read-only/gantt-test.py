from trame.app import get_server
from trame.ui.vuetify import SinglePageWithDrawerLayout
from trame.widgets import vuetify, code

# -----------------------------------------------------------------------------
# Trame setup
# -----------------------------------------------------------------------------

server = get_server(client_type="vue2")
state, ctrl = server.state, server.controller

# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------

state.trame__title = "Viewer"

with SinglePageWithDrawerLayout(server) as layout:
    layout.title.set_text("Viewer")

    with layout.toolbar as toolbar:
        toolbar.dense = True
        vuetify.VSpacer()

    items = [
        {'id': 1, 'summary': 'This is a task.',
         'start_date': '2024-11-02 00:00',
         'end_date': '2024-11-13 00:00',
         'duration': 11,
         'progress': 30,
         'items' :
         [
            {'id': 11, 'summary': 'This is a first subtask',
             'start_date': '2024-11-03 00:00',
             'end_date': '2024-9-13 00:00'},
             {'id': 12, 'summary': 'This is another subtask',
              'start_date': '2024-11-07 00:00',
              'start_date': '2024-11-11 00:00'}
         ]},
        {'id': 2, 'summary': 'This is a task with a longer description.',
         'start_date': '2024-11-03 00:00',
         'end_date': '2024-11-04 00:00',
         'duration': 1}
    ]

    with layout.content:
        with vuetify.VContainer(fluid=True, classes="fill-width"):
            gantt = code.Gantt( fluid=True,
                                canEdit=False,
                               dateLimit=22,
                               startDate='2024-11-01 00:00',
                               endDate='2024-12-01 00:00',
                               title='Gantt-pre-test',
                               items=("items", items))
            ctrl.view_update = gantt.update

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    server.start()
