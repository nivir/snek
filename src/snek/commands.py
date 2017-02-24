import click
import os
import sys
import yaml


from sultan.api import Sultan
from snek.error import SnekInitializationError
from snek.utils import cli_request, load_snekfile


def init_command():
    """
    Creates a New Python project, and places a 'Snekfile' with the necessary information
    to manage a Python Project.
    """
    pwd = os.environ.get('PWD')
    snek = load_snekfile()
    project = snek.get('project', {})
    try:
        click.echo("")
        click.echo("")
        click.echo("----")
        click.echo("Snek")
        click.echo("----")
        click.echo("")
        click.echo("'snek init' will setup your project. Snek will go through a ")
        click.echo("series of questions, and based on your answers, snek will setup")
        click.echo("your python project.")
        click.echo("")
        click.echo("")
        click.echo("Once everything has been setup, run 'snek install' to setup dependencies.")
        click.echo("")
        click.echo("")
        click.echo("For more information, run 'snek --help'")
        can_start = cli_request('Are you ready to get started?', 'Y', choices=['y', 'Y', 'n', 'N'])

        if can_start not in ('y', 'Y'):
            click.echo("OK, we'll stop here.")
        
        project_interpretter = cli_request(
            'Which version of Python?', 
            project.get('interpretter') or sys.version_info.major, 
            choices=[2,3])

        project_name = cli_request(
            'Project Name', 
            project.get('name') or os.path.basename(pwd))

        project_description = cli_request(
            'Project Description',
            project.get('description') or '')

        project_version = cli_request(
            'Project Version', 
            project.get('version') or '0.1.0')

        project_author = cli_request(
            'Project Author',
            project.get('author') or '')

        project_author_email = cli_request(
            'Project Author E-Mail',
            project.get('author_email') or '')

        project_license = cli_request(
            'Project License',
            project.get('license') or '')

        project_type = cli_request(
            'Project Type', 
            project.get('type') or 'cli', 
            choices=['cli', 'gui', 'web'], 
            show_choices=True)

        snekfile_params = {}
        snekfile_params['project'] = {}
        snekfile_params['project']['name'] = project_name
        snekfile_params['project']['description'] = project_description
        snekfile_params['project']['version'] = project_version
        snekfile_params['project']['author'] = project_author
        snekfile_params['project']['author_email'] = project_author_email
        snekfile_params['project']['license'] = project_license
        snekfile_params['project']['type'] = project_type
        snekfile_params['project']['interpretter'] = project_interpretter
        snekfile_params['project']['dependencies'] = {}
        snekfile_params['project']['dependencies']['dev'] = ['ipython', 'ipdb']
        snekfile_params['project']['tasks'] = {}
        snekfile_params['project']['tasks']['hello'] = ['echo "Hello Snek!"', 'cat Snekfile']

        snekfile_path = os.path.join(pwd, 'Snekfile')
        with open(snekfile_path, 'w') as f:
            yaml.dump(snekfile_params, f, default_flow_style=False)

        with Sultan.load(cwd=pwd) as s:
            r = s.cat(snekfile_path).run()
            for l in r:
                print l
        
        isOK = cli_request("Does this look OK?", 'Y', choices=['y', 'Y', 'n', 'N'])
        if isOK in ('n', 'N'):
            click.secho("Please run 'snek init' again to try again.", fg='yellow')
        
        click.secho('Your Snekfile can be found in "%s"' % snekfile_path, fg='green')

    except SnekInitializationError, e:
        
        click.secho("ERROR: %s" % e.message, fg='red')
        return


def steve_command():

    click.echo("           /^\/^\\")
    click.echo("         _|__|  O|")
    click.echo("\/     /~     \_/ \\")
    click.echo(" \____|__________/  \\")
    click.echo("        \_______      \\")
    click.echo("                `\     \                 \\")
    click.echo("                  |     |                  \\")
    click.echo("                 /      /                    \\")
    click.echo("                /     /                       \\\\")
    click.echo("              /      /                         \ \\")
    click.echo("             /     /                            \  \\")
    click.echo("           /     /             _----_            \   \\")
    click.echo("          /     /           _-~      ~-_         |   |")
    click.echo("         (      (        _-~    _--_    ~-_     _/   |")
    click.echo("          \      ~-____-~    _-~    ~-_    ~-_-~    /")
    click.echo("            ~-_           _-~          ~-_       _-~")
    click.echo("               ~--______-~                ~-___-~")