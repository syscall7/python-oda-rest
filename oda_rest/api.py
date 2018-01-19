import requests
import logging
from collections import namedtuple

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

Function = namedtuple('Function', ['name', 'vma', 'args', 'retval'])
Section = namedtuple('Section', ['name', 'vma', 'size', 'flags'])
Comment = namedtuple('Section', ['vma', 'comment'])
User = namedtuple('User', ['username', 'email', 'is_lazy_user'])
Operation = namedtuple('Operation', ['datetime', 'user', 'name', 'desc'])

class OdaProject(object):

    def __init__(self, url, shortname, clone=False):
        self.session = requests.session()
        self.url = "%s/odaweb/api" % url

        try:
            r = self.session.get("%s/masters/%s/can_edit/" % (self.url, shortname))
            can_edit = r.json()
        except Exception as e:
            raise Exception("Could not connect to %s" % self.url)

        if clone:
            logger.debug("Cloning project %s" % shortname)
            r = self.session.get("%s/masters/%s/clone/" % (self.url, shortname))

            if r.ok:
                self.shortname = r.json()
                logger.debug("Cloned project %s to %s" % (shortname,
                                                       self.shortname))
            else:
                raise Exception("Failed to clone project %s" % shortname)

            can_edit = True
        else:
            self.shortname = shortname

        if not can_edit:
            raise Exception("You do not have access to this project.")

    def _fetch(self, kind):
        r = self.session.get("%s/%s/?short_name=%s&revision=0" % (
            self.url, kind, self.shortname))

        if r.ok:
            return r.json()
        else:
            raise Exception("Failed to retrieve %s: %s" %
                            (kind, r.content.decode()))

    def _push(self, kind, params):

        params['short_name'] = self.shortname
        params['revision'] = 0
        url = "%s/%s/" % (self.url, kind)
        headers = {
            'X-CSRFToken': self.session.cookies['csrftoken']
        }
        r = self.session.post(url, json=params,
                              headers=headers)

        if not r.ok:
            raise Exception("Failed to create %s" % kind)

        return r.json()

    def Functions(self):
        return [Function(**f) for f in self._fetch('functions')]

    def Sections(self):
        return [Section(**s) for s in self._fetch('sections')]

    def Comments(self):
        return [Comment(**c) for c in self._fetch('comments')]

    def Operations(self):
        return [Operation(**o) for o in self._fetch('operations')]

    def CreateComment(self, vma, comment):
        params = {
            'vma': vma,
            'comment': comment,
        }
        return self._push('comments', params)
