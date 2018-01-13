import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class OdaProject(object):

    URL = "http://localhost:8000/odaweb/api"

    def __init__(self, shortname, clone=False):
        self.session = requests.session()

        if clone:
            logger.debug("Cloning project %s" % shortname)
            r = self.session.get("%s/masters/%s/clone/" % (self.URL, shortname))

            if r.ok:
                self.shortname = r.json()
                logger.debug("Cloned project %s to %s" % (shortname,
                                                       self.shortname))
        else:
            self.shortname = shortname

        if not self.isOwner():
            raise Exception("You do not have access to this project.")

        r = self.session.get("%s/load?short_name=%s&revision=0" %
                             (self.URL, self.shortname))

        if not r.ok:
            raise Exception("Failed to load project")

    def isOwner(self):

        r = self.session.get("%s/masters/%s/is_owner/" % (self.URL,
                                                       self.shortname))

        if r.status_code == 404:
            raise Exception("This project does not exist.")

        return r.json()

    def Functions(self):
        r = self.session.get("%s/functions/?short_name=%s&revision=0" % (
            self.URL, self.shortname))

        if r.ok:
            return r.json()
        else:
            raise Exception("Failed to retrieve functions: %s" % r.content.decode())
