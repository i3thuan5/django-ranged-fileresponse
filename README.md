# Django Ranged Response
[![Build Status](https://travis-ci.org/i3thuan5/django-ranged-response.svg?branch=master)](https://travis-ci.org/i3thuan5/django-ranged-response)
[![Coverage Status](https://coveralls.io/repos/github/i3thuan5/django-ranged-response/badge.svg?branch=master)](https://coveralls.io/github/i3thuan5/django-ranged-response?branch=master)

## Why content range?
If you're in the situation that you have an authenticated Django view that returns
files for download, you may have noticed that Safari 9.x doesn't play audio files
properly when returning audio-files. The reason is that Safari sends a HTTP_RANGE request header and expects a proper `Content-Range` response header in return.
There is a [Django ticket](https://code.djangoproject.com/ticket/22479)
for this, however no indication that this feature will be implemented soon.


## Three approches about content range
Choose proper one by your situation.

### 1. Support all dynamic views and static files
The [WhiteNoise](http://whitenoise.evans.io/en/stable/index.html) provides a middleware to support global settings.

### 2. Support static files only
Nginx can support static and media files.

See more details on [Setting up Django and your web server with uWSGI and nginx](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html#configure-nginx-for-your-site). If some views need redirect to static or media files, see [the stackoverflow answer](https://stackoverflow.com/a/23404382/3640653).

### 3. Support specific dynamic views only
This project supports `RangedFileResponse` with content range. Use `RangedFileResponse` for every view you wanted. The views are mostly designed for media API, like speech synthesis, video generators.

You can use it for custom views like:

    import io
    from ranged_response import RangedFileResponse

    def some_proxy_view(request):
        filename = 'myfile.wav'
        response = RangedFileResponse(request, open(filename, 'rb'), content_type='audio/wav')
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response

    def some_dynamic_view(request):
        binarydata = b'RIFF...'
        response = RangedFileResponse(request, io.BytesIO(binarydata), content_type='audio/wav')
        response['Content-Disposition'] = 'attachment; filename="myfile.wav"'
        return response


## About this project
The [original suggested fix](https://github.com/satchamo/django/commit/2ce75c5c4bee2a858c0214d136bfcd351fcde11d)
applies the code to Django's static view. This is a packaged version of that fix,
but uses a modified FileResponse, instead of applying it to Django's static view.
