from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import os, json
try:
    from web.lisa.utils import method_restricted_to, is_ajax
    from web.lisa.settings import LISA_PATH
except ImportError:
    from lisa.utils import method_restricted_to, is_ajax
    from lisa.settings import LISA_PATH

@login_required()
def widget1(request, x, y):
    from ChatterBot.modules.chat import Chat
    content = json.loads(Chat().getTime())
    return render_to_response(os.path.abspath(os.path.dirname(__file__) + '/templates/widget.html'),
                              {
                                  'content': str(content['body']), 'data_sizex': "1", 'data_sizey': "1",
                                  'data-row': x, 'data-col': y
                              },
                              context_instance=RequestContext(request))