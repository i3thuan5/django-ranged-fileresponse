from setuptools import setup

description = 'Modified Django FileResponse that adds Content-Range headers.'

setup(
    name='django-ranged-response',
    version='0.2.0',
    description=description,
    url='https://github.com/i3thuan5/django-ranged-response',
    author='Spindle',
    author_email='jeroen@wearespindle.com',
    license='MIT',
    packages=['ranged_response'],
    install_requires=[
        'django',
    ],
    zip_safe=False,
)
