from typing import Text, Dict, List

from chatbot_dm.channels.channel import (
    InputChannel,
    OutputChannel,
    UserMessage,
    CollectingOutputChannel,
    RestInput,
)

# this prevents IDE's from optimizing the imports - we need to import the
# above first, otherwise we will run into import cycles
from chatbot_dm.channels.socketio import SocketIOInput

pass

from chatbot_dm.channels.botframework import BotFrameworkInput  # nopep8
from chatbot_dm.channels.callback import CallbackInput  # nopep8
from chatbot_dm.channels.console import CmdlineInput  # nopep8
from chatbot_dm.channels.facebook import FacebookInput  # nopep8
from chatbot_dm.channels.mattermost import MattermostInput  # nopep8
from chatbot_dm.channels.rasa_chat import RasaChatInput  # nopep8
from chatbot_dm.channels.rocketchat import RocketChatInput  # nopep8
from chatbot_dm.channels.slack import SlackInput  # nopep8
from chatbot_dm.channels.telegram import TelegramInput  # nopep8
from chatbot_dm.channels.twilio import TwilioInput  # nopep8
from chatbot_dm.channels.webexteams import WebexTeamsInput  # nopep8

input_channel_classes = [
    CmdlineInput,
    FacebookInput,
    SlackInput,
    TelegramInput,
    MattermostInput,
    TwilioInput,
    RasaChatInput,
    BotFrameworkInput,
    RocketChatInput,
    CallbackInput,
    RestInput,
    SocketIOInput,
    WebexTeamsInput,
]  # type: List[InputChannel]

# Mapping from a input channel name to its class to allow name based lookup.
BUILTIN_CHANNELS = {
    c.name(): c for c in input_channel_classes
}  # type: Dict[Text, InputChannel]
