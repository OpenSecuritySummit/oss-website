from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev

from oss_hugo.OSS_Session import OSS_Session


class test_OSS_Session(TestCase):
    def setUp(self):
        self.test_session = 'Test Session'
        self.session      = OSS_Session(self.test_session)
        self.result       = None
        self.session.create()

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)
        assert self.session.delete() is True

    def test__init__(self):
        assert self.session.base_folder == 'content/tracks/'
        assert self.session.exists()

    def test_load(self):

        assert OSS_Session('test-session.md'               ).load().exists()
        assert OSS_Session('Test Session'                  ).load().exists()
        assert OSS_Session('aaaa/../test-session.md'       ).load().exists()
        assert OSS_Session('content/tracks/Test Session'   ).load().exists()
        assert OSS_Session('content/tracks/test-session.md').load().exists()
        #

