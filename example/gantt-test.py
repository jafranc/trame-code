import json
from trame.app import get_server
from trame.ui.vuetify import SinglePageLayout
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

@state.change("items")
def update_items(items, **kwargs):
    text.state.value = json.dumps(state.items, indent=4, sort_keys=True)
#
def update_from_js(*items):
    state.items = list(items)

def validate_state():
    state.items = json.loads(text.state.value)

with SinglePageLayout(server) as layout:
    layout.title.set_text("Viewer")

    with layout.toolbar as toolbar:
        toolbar.dense = True
        vuetify.VSpacer()

    items = [
        {"id": 1, "summary": "This is a task.",
         "start_date": "2024-11-02 00:00",
         "end_date": "2024-11-25 00:00",
         "duration": 23},
        {"id": 2, "summary": "This is a task with a longer description.",
         "start_date": "2024-11-03 00:00",
         "end_date": "2024-11-04 00:00",
         "duration": 1}
    ]

    items_alt = [
        {"id": 3, "summary": "Lorem ipsum.",
         "start_date": "2024-11-07 00:00",
         "end_date": "2024-11-09 00:00",
         "duration": 2}
    ]

    fields = [
        {
            'summary': {
                'label': 'Summary',
                'component': 'gantt-text',
                'width': 300,
                'placeholder': 'Add a new task...'
            },
            'start_date': {
                'label': 'Start',
                'component': 'gantt-date',
                'width': 75,
                'placeholder': 'Start',
                'sort': 'date'
            },
            'end_date': {
                'label': 'End',
                'component': 'gantt-date',
                'width': 75,
                'placeholder': 'End',
                'sort': 'date'
            },
            'duration': {
                'label': 'Days',
                'component': 'gantt-number',
                'width': 50,
                'placeholder': '0'
            }
        }
    ]

    with layout.content:
        with vuetify.VContainer(fluid=True, classes="fill-width"):
            gantt = code.Gantt(fluid=True,
                               canEdit=True,
                               dateLimit=30,
                               startDate='2024-11-01 00:00',
                               endDate='2024-12-01 00:00',
                               title='Gantt-pre-test',
                               fields=fields,
                               update=(update_from_js,"items"),
                               items=("items", items))

        with vuetify.VContainer(fluid=True, classes="fill-width"):
            text = vuetify.VTextarea(
                v_model=( "value", json.dumps(state.items, indent=4, sort_keys=True), "items", items),
                height=600,
                rows=20,
                min_height=500,
                density='compact')
            with vuetify.VBtn(v_model=("items",items), click=validate_state):
                vuetify.VIcon("mdi-cached")

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    server.start()
