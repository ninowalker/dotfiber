from behave import *
import os
import shutil
from invoke import Context


@given(u'an envvar FIBER_PREFIX=.')
def step_impl(context):
    os.environ['FIBER_PREFIX'] = context.path
    Context().run("mkdir -p {}".format(context.path))
    Context().run("ls {}".format(context.path))

@when(u'we exec {cmd}')
def step_impl(context, cmd):
    Context().run(cmd)

@when(u'we run the install script')
def step_impl(context):
    assert os.path.exists("./install")
    Context().run("./install")


@then(u'the directory ./{path} exists')
def step_impl(context, path):
    assert os.path.exists(os.path.join(context.path, path))
    assert os.path.isdir(os.path.join(context.path, path))

@then(u'the file ./{path} exists')
def step_impl(context, path):
    assert os.path.exists(os.path.join(context.path, path))
    assert os.path.isfile(os.path.join(context.path, path))

@when(u'we run .fiber {params}')
def step_impl(context, params):
    path = os.path.join(context.path, ".fiber/env/bin/.fiber")
    context.result = Context().run("{} {}".format(path, params))
