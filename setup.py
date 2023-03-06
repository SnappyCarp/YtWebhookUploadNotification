from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
DESCRIPTION = 'Easy YouTube Upload Notifications'
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    l_d = "\n" + fh.read()


setup(
    name='YtWebhookNotification',
    url='https://github.com/SnappyCarp/YtWebhookNotification',
    author='JediMinecraft1',
    author_email='edmund.spielman@outlook.com',
    packages=find_packages(),
    # Needed for dependencies
    install_requires=['discord-webhook', 'requests', 're'],
    version='0.1',
    license='MIT',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=l_d,
)