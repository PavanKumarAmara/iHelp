from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa.nlu.training_data import load_data
import zoom as zoom_details

class ActionGetZoomLink(Action):
    def name(self):
        return 'zoom_link'

    def run(self, dispatcher, tracker, domain):
        zoom_of = tracker.get_slot('person')
        zoom_link = zoom_details.d[zoom_of.lower()]
        response = """The Zoom link of {} is seeded as, {}""".format(zoom_of, zoom_link)
        dispatcher.utter_message(response)
        return [SlotSet('person', zoom_of)]
