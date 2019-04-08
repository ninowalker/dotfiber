import shutil
import os


def before_scenario(context, scenario):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    context.config.setup_logging()
    context.path = path = os.path.join(os.getcwd(), ".scratch")
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
