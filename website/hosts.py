from django_hosts import patterns, host

host_patterns = patterns('',
                         host(r'scrimbler', 'scrimbler.urls', name='scrimbler'),
                         )
