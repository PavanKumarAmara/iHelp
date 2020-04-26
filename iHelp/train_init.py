from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa.core.agent import Agent
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy


if __name__ == 'main':
    logging.basicConfig(level='info')
    training_data_file = './data/stories.md'
    model_path = './models/'

    agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])
    agent.train(
        training_data_file,
        augmentation_factor=50,
        max_history=5,
        epochs=100,
        batch_size=10,
        validation_split=0.2
    )
    agent.persist(model_path)