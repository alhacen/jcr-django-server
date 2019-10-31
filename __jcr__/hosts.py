from django_hosts import patterns, host
from __jcr__.secret import SECRET

HOST = SECRET['SERVER']['HOSTS']

host_patterns = patterns('',
                         host(HOST['API'], 'upcjmi.urls.api', name='api'),
                         host(HOST['ADMIN'], 'upcjmi.urls.admin', name='admin'),
                         host('dev', 'upcjmi.urls.dev', name='dev')
                         )
