# coding: utf-8

from flask import render_template, Blueprint, Markup


def gist(gist_id, **kwargs):
    script_url = 'https://gist.github.com/{}.js'.format(gist_id)
    return Markup(render_template('gist/gist.html', script_url=script_url))


class Gist(object):
    def __init__(self, app=None, **kwargs):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.register_blueprint(app)
        app.add_template_filter(gist)
        app.add_template_global(gist)

    def register_blueprint(self, app):
        module = Blueprint("gist", __name__,
                           template_folder="templates")
        app.register_blueprint(module)
        return module
