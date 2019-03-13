from subprocess import call
call(["docker", "build", "."])
call(["docker-compose", "build"])
