from rasa.nlu.training_data import load_data
from rasa.nlu import config
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.components import ComponentBuilder
from rasa.nlu.model import Trainer, Interpreter, Metadata

builder = ComponentBuilder(use_cache=True)


def train_nlu(data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file), builder)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name="iHelp")


if __name__ == '__main__':
    train_nlu('./data/nlu.md', 'config.yml', './models/nlu')

# def run_nlu:
#     interpreter=Interpreter.load(,builder)
