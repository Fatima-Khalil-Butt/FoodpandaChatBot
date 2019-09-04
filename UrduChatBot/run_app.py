from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/foodpandanlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-700516438022-686960774642-728450041478-9278249d32e05544b5d7636175135a4b', #app verification token
							'xoxb-700516438022-714824344163-oQoLIooYosorGHSEvbm5Ruao', # bot verification token
							'rmjDPRE7I9yTXnpWdSgVZcZl', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))