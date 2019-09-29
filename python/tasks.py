from invoke import task


@task
def build(c, clean=False):
    if clean:
        print("Cleaning!")
    print("Building!")


@task
def hi(c, name):
    print("Hi {}!".format(name))