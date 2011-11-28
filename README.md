# Pythonic HAML for pyramid

This configures pyramid to allow the use of [HAML](http://haml-lang.com/) as template markup.

It's based on [PyHAML](http://github.com/mikeboers/PyHAML)


## Install

1. Use pip to get the package:

    pip install pyramid_haml

2. Adjust your "your\_project/\_\_init\_\_.py" and add this somewhere to your main function:

    config.include("pyramid_haml")

3. Whenever you use a template with '.haml' as suffic it will be rendered via the PyHAML template
   engine.

## Documentation

You can find documentation on the [PyHAML project page](http://github.com/mikeboers/PyHAML) on github or at the [HAML project website](http://haml-lang.com/).


