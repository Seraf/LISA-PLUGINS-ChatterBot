from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
try:
    from web.lisa.utils import method_restricted_to, is_ajax
    from web.lisa.settings import LISA_PATH
except ImportError:
    from lisa.utils import method_restricted_to, is_ajax
    from lisa.settings import LISA_PATH

@login_required()
def widget1(request, x, y):
    from ChatterBot.module.chat import Chat
    content = Chat().getTime()
    return render_to_response('widget.html',
                              {
                                  'content': content, 'data-sizex': "1", 'data-sizey': "1",
                                  'data-row': x, 'data-col': y
                              },
                              context_instance=RequestContext(request))
