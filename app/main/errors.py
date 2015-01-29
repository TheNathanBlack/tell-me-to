from flask import render_template, redirect, url_for
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return redirect(url_for('main.index'))


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
