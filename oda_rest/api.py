import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class OdaProject(object):

    def __init__(self, url, shortname, clone=False):
        self.session = requests.session()
        self.url = "%s/odaweb/api" % url

        if clone:
            logger.debug("Cloning project %s" % shortname)
            r = self.session.get("%s/masters/%s/clone/" % (self.url, shortname))

            if r.ok:
                self.shortname = r.json()
                logger.debug("Cloned project %s to %s" % (shortname,
                                                       self.shortname))
        else:
            self.shortname = shortname

        if not self._isOwner():
            raise Exception("You do not have access to this project.")

    def _isOwner(self):

        r = self.session.get("%s/masters/%s/is_owner/" % (self.url,
                                                       self.shortname))

        if r.status_code == 404:
            raise Exception("This project does not exist.")

        return r.json()

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
        return self._fetch('functions')

    def Sections(self):
        return self._fetch('sections')

    def Comments(self):
        return self._fetch('comments')

    def CreateComment(self, offset, comment):
        params = {
            'offset': offset,
            'comment': comment,
        }
        return self._push('comments', params)
