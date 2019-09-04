from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent #to train model
from rasa_core.policies.keras_policy import KerasPolicy #models that used to train nlu_model 
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	
	training_data_file = './data/stories.md'
	model_path = './models/dialogue'
	
	agent = Agent('foodpanda_domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])
	
	agent.train(
			training_data_file, 
			augmentation_factor = 50, #how many stories we want to  create
			max_history = 2, #how many states we want model to remember
			epochs = 500,#No of forward and backward training process ,in training process
			batch_size = 10,# Amount of samples Used
			validation_split = 0.2)#data to be used to validate the mode;
			
	agent.persist(model_path)