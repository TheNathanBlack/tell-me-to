from flask import render_template

from . import main


@main.route('/')
@main.route('/name/<name>/')
@main.route('/<one>/name/<name>')
@main.route('/<one>/<two>/name/<name>')
@main.route('/<one>/<two>/<three>/name/<name>')
@main.route('/<one>/<two>/<three>/<four>/name/<name>')
@main.route('/<one>/<two>/<three>/<four>/<five>/name/<name>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>/name/<name>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>/<seven>/name/<name>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>/<seven>/<eight>/name/<name>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>/<seven>/<eight>/<nine>/name/<name>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>/<seven>/<eight>/<nine>/<ten>/name/<name>')
@main.route('/<one>')
@main.route('/<one>/<two>')
@main.route('/<one>/<two>/<three>')
@main.route('/<one>/<two>/<three>/<four>')
@main.route('/<one>/<two>/<three>/<four>/<five>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>/<seven>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>/<seven>/<eight>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>/<seven>/<eight>/<nine>')
@main.route('/<one>/<two>/<three>/<four>/<five>/<six>/<seven>/<eight>/<nine>/<ten>')
def index(**kwargs):
    name = None
    directive = ""
    possible_keys=("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")
    if kwargs:
        if 'name' in kwargs.keys():
            name = kwargs['name']
            del kwargs['name']

        if kwargs:
            directive = ' '.join([ kwargs[possible_keys[key]] for key in range(len(kwargs.keys()))])


    return render_template('index.html', name=name, directive=directive)
