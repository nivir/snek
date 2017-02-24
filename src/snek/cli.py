import click
import os
import sys
import yaml
import logging

from sultan.api import Sultan
from snek.commands import (init_command, steve_command)
from snek.error import SnekTaskNotFound
from snek.utils import load_snekfile

logger = logging.getLogger('')
logger.setLevel(logging.ERROR)

@click.group('snek')
def snek():
    pass

@snek.command()
def steve():
    """
    Call out steve for a show!
    """
    steve_command()

@snek.command()
def init():
    """
    Creates a New Python project, and places a 'Snekfile' with the necessary information
    to manage a Python Project.
    """
    init_command()

@snek.command()
@click.argument('name')
def run(name):
    """
    Runs a task with the given 'name'.
    """
    snekfile = load_snekfile().get('project', {})
    try:
        tasks = snekfile.get('tasks', {}).get(name)
        if not tasks:
            raise SnekTaskNotFound("'%s' task is not found in Snekfile" % (name))
        
        with Sultan.load() as s:
            for task in tasks:
                click.secho("Executing '%s'" % task, fg='cyan')
                s.commands = [task]
                response = s.run()
                for line in response:
                    print line

    except Exception, e:
        click.secho("ERROR: Unable to run task '%s'" % (name), fg='red')
        click.secho("ERROR: %s" % e.message, fg='red')