from django.http import Http404
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from django.core.cache import parse_backend_uri

import datetime

def server_list(request):
    try:
        import memcache
    except:
        raise Http404
    stats = {}
    cache_servers = {}
    # It assumes that you're using a right configuration
    servers = parse_backend_uri(settings.CACHE_BACKEND)[1].split(";")
    for server in servers:
        host = memcache._Host(server)
        host.connect()
        if host == 0:
            raise Http404
        try:
            host.send_cmd("stats")
        except:
            break
        while True:
            line = host.readline().split(None)
            if line[0] == "END":
                break
            try:
                val = int(line[2])
                if line[1] == "uptime":
                    value = datetime.timedelta(seconds=val)
                elif line[1] == "time":
                    value = datetime.datetime.fromtimestamp(val)
            except Exception:
                pass
            stats[line[1]] = line[2]
        stats['hit_rate'] = 0
        if int(stats['cmd_get']) != 0:
            stats['hit_rate'] = 100 * int(stats['get_hits']) / int(stats['cmd_get'])
        stats['right_now'] = datetime.datetime.now()
        
        limit_maxbytes = int(stats['bytes'])
        if int(stats['limit_maxbytes']) > 0:
            limit_maxbytes = int(stats['limit_maxbytes'])
        stats['full'] = (100 * int(stats['bytes']) / limit_maxbytes)
        # Add info. for this host to list
        cache_servers[server] = stats
        # Close connection
        host.close_socket()
    dict_vars = {'servers': cache_servers}

    return render_to_response('status.html', dict_vars, RequestContext(request))
