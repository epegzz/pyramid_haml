# HAML support for pyramid

pyramid\_haml configures your pyramid project to allow the use of [HAML](http://haml-lang.com/) as template markup language.

It uses [PyHAML](http://github.com/mikeboers/PyHAML) as preprocessor for the [Mako](http://www.makotemplates.org/) template renderer.


## Install

1. Simply use pip to get the latest package:

        pip install pyramid_haml

2. Adjust your "your\_project/\_\_init\_\_.py" and add the following line somewhere to in the `main()` function:

        config.include("pyramid_haml")

3. Whenever you use a template file with '.haml' as suffix it will be rendered via PyHAML.

4. Because PyHAML uses the Mako rendering engine, you can configure `pyramid_haml` with the same options as [pyramid_mako](http://docs.pylonsproject.org/projects/pyramid_mako/en/latest/), prefixing each option with `haml.` instead of `mako.`.

## Documentation

You can find documentation on the [PyHAML project page](http://github.com/mikeboers/PyHAML) on github or at the [HAML project website](http://haml-lang.com/).


