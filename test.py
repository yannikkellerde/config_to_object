from config_to_object import load_config
from example_config_types import Config

config:Config = load_config("example_config.ini",encoding="utf-8")

words = config.Params.words
print(words)