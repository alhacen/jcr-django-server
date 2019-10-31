from django_hosts import patterns, host
from __jcr__.secret import SECRET

HOST = SECRET['SERVER']['HOSTS']

host_patterns = patterns('',
                         host(HOST['API'], '__jcr__.urls.api', name='api'),
                         host(HOST['ADMIN'], '__jcr__.urls.admin', name='admin'),
                         host('dev', '__jcr__.urls.dev', name='dev')
                         )
