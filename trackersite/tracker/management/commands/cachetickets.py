from django.core.management.base import NoArgsCommand
from django.conf import settings
import os.path
import json
from django.utils import translation
from tracker.models import Ticket

class Command(NoArgsCommand):
    help = 'Cache tickets'

    def handle_noargs(self, **options):
        for langcode, langname in settings.LANGUAGES:
            with translation.override(langcode):
                tickets = []
                for ticket in Ticket.objects.order_by('-id'):
                    subtopic = ticket.subtopic
                    if subtopic:
                        subtopic = '<a href="%s">%s</a>' % (ticket.subtopic.get_absolute_url(), ticket.subtopic)
                    else:
                        subtopic = ''
                    tickets.append([
                        '<a href="%s">%s</a>' % (ticket.get_absolute_url(), ticket.pk),
                        unicode(ticket.event_date),
                        '<a class="ticket-summary" href="%s">%s</a>' % (ticket.get_absolute_url(), ticket.summary),
                        '<a href="%s">%s</a>' % (ticket.topic.grant.get_absolute_url(), ticket.topic.grant),
                        '<a href="%s">%s</a>' % (ticket.topic.get_absolute_url(), ticket.topic),
                        subtopic,
                        ticket.requested_by_html(),
                        "%s %s" % (ticket.preexpeditures()['amount'] or 0, settings.TRACKER_CURRENCY),
                        "%s %s" % (ticket.accepted_expeditures(), settings.TRACKER_CURRENCY),
                        "%s %s" % (ticket.paid_expeditures(), settings.TRACKER_CURRENCY),
                        unicode(ticket.state_str()),
                        unicode(ticket.updated),
                    ])
                open(os.path.join(settings.TRACKER_PUBLIC_DEPLOY_ROOT, 'tickets', '%s.json' % langcode), 'w').write(json.dumps({"data": tickets}))