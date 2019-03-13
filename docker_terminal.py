import sys
from subprocess import call

def callDocker(arg):
    if len(sys.argv) != 2:
        print("USAGE:\n python docker_terminal \"[command to send to docker]\"")
        return 1
    call(["docker-compose", "run", "app", "sh","-c", arg])

callDocker(sys.argv[1])
