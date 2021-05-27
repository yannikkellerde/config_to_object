# Convert a .ini config file to a typed Object
![/videos/best_now.gif](https://github.com/yannikkellerde/config_to_object/blob/main/videos/best_now.gif?raw=True)

## Installation
Install via pip `pip install config-to-object`.  
There are no dependencies.

## Usage
Create your `.ini` configuration file. For an example look at [example_config.ini](https://github.com/yannikkellerde/config_to_object/blob/main/example_config.ini?raw=True). You can use any type of native python object such as tuples, lists, strings, floats, integers as parameter values (except dict). There type will be automatically recognized when loading the config file.

Load your configuration file using `from config_to_object import load_config` and `config = load_config("path/to/your/config.ini")`

You can access the values from your `.ini` using `.` syntax: `words = config.Params.words`.

If you want your `config` object to be type hinted, so that your IDE can give you better code completions, run `ini_typefile path/to/your/config.ini config_types.py`. Then, in your code add `from config_types import Config` and initialize your config with `config:Config = load_config("path/to/your/config.ini")`