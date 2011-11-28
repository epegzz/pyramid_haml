from pyramid.threadlocal import get_current_request
from pyramid.events import BeforeRender
from pyramid import mako_templating
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
import haml


def includeme(config):
    config.add_renderer(".haml", HamlRenderer)
    config.add_subscriber\
        ( add_render_args_to_render_globals
        , BeforeRender
        )


def add_render_args_to_render_globals(event):
    """
    Store render args in render_globals so that we can
    access them later if we need them.
    """
    request = get_current_request();
    request.tmpl_context._render_args = event.rendering_val
    event['css'] = filter__css
    event['javascript'] = filter__javascript


class HamlRenderer(object):
    """
    The haml renderer \o/
    """
    def __init__(self, info):
        info.settings['mako.preprocessor'] = haml.preprocessor
        self.makoRenderer = mako_templating.renderer_factory(info)

    def __call__(self, value, system):
        return self.makoRenderer(value, system)



def filter__css(source):
    """
    Use :css in haml files. Yeahy!
    """
    return '<style type="text/css">\n<!--\n\n\%s\n\n-->\n</style>' % _render_mako(source)


def filter__javascript(source):
    """
    Use :javascript in haml files. Yeahy!
    """
    return '<script type="text/javascript">\n%s\n</script>' % _render_mako(source)




def _render_mako(source):
    """
    Helper function.
    """
    request = get_current_request();
    tpl = Template(source)
    buf = StringIO()
    ctx = Context(buf, c=request.tmpl_context, **(request.tmpl_context._render_args))
    tpl.render_context(ctx)
    return buf.getvalue()
