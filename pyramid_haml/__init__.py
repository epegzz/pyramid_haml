from pyramid_mako import MakoRendererFactory, PkgResourceTemplateLookup, parse_options_from_settings
import haml


def add_haml_renderer(config, extension, settings_prefix='haml.'):
    """ Register a HAML renderer for a template extension.

    This function is available on the Pyramid configurator after
    including the package:

    .. code-block:: python

       config.add_haml_renderer('.haml', settings_prefix='haml.')

    The renderer will load its configuration from a prefix in the Pyramid
    settings dictionary. The default prefix is 'haml.'.

    The renderer delegates to the Mako renderer and supports all its
    configuration options, except ``preprocessor`` which is overridden
    to be the haml preprocessor.
    """
    renderer_factory = MakoRendererFactory()
    config.add_renderer(extension, renderer_factory)

    def register():
        registry = config.registry
        opts = parse_options_from_settings(
            registry.settings, settings_prefix, config.maybe_dotted)
        opts['preprocessor'] = haml.preprocessor
        lookup = PkgResourceTemplateLookup(**opts)

        renderer_factory.lookup = lookup

    config.action(('haml-renderer', extension), register)


def includeme(config):
    """ Set up standard configurator registrations.  Use via:

    .. code-block:: python

       config = Configurator()
       config.include('pyramid_haml')

    Once this function has been invoked, templates with a ``.haml`` extension
    will be rendered using PyHAML. This can be overridden and more may be
    added via the ``config.add_haml_renderer`` directive. See
    :func:`~pyramid_haml.add_haml_renderer` documentation for more information.
    """
    config.add_directive('add_haml_renderer', add_haml_renderer)

    config.add_haml_renderer('.haml')
