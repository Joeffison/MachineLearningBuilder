# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mimetypes
import os

from django.core.files.storage import default_storage
from django.http import HttpResponse


def serve_using_django_in_memory(request, filename):
    filename = filename.replace("..", "").replace("tmp/", "").replace("/", "").replace("\\", "")
    filename = os.path.join("tmp", filename)
    file_full_path = default_storage.open(filename, "r")

    data = file_full_path.read()

    response = HttpResponse(data, content_type=mimetypes.guess_type(data)[0])
    response['Content-Disposition'] = "attachment; filename={0}".format(filename)
    response['Content-Length'] = os.path.getsize(filename)
    return response
