from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class Espy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('espy.intent')
    def handle_espy(self, message):
        self.speak_dialog('espy')


def create_skill():
    return Espy()

