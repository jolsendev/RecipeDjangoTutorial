from subprocess import call
call(['python ','docker_terminal.py', "python manage.py test && flake8"])
