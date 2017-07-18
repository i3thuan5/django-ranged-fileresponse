from setuptools import setup

description = 'Modified Django FileResponse that adds Content-Range headers.'

setup(
    name='django-ranged-file-response',
    version='0.2.0',
    description=description,
    url='https://github.com/wearespindle/django-ranged-fileresponse',
    author='Spindle',
    author_email='jeroen@wearespindle.com',
    license='MIT',
    packages=['ranged_fileresponse'],
    install_requires=[
        'django',
    ],
    zip_safe=False,
)
