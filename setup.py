from setuptools import setup

setup(
    name='YtWebhookNotification',
    url='https://github.com/SnappyCarp/YtWebhookNotification',
    author='JediMinecraft1',
    author_email='edmund.spielman@outlook.com',
    # Needed to actually package something
    packages=['measure'],
    # Needed for dependencies
    install_requires=['discord-webhook'],
    # *strongly* suggested for sharing
    version='0.1',
    license='MIT',
    description='Easy YouTube Notifications',
    long_description=open('README.md').read(),
)