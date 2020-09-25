from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev

from oss_hugo.OSS_Schedule import OSS_Schedule
from oss_hugo.OSS_Session import OSS_Session


class test_OSS_Schedule(TestCase):
    def setUp(self):
        self.schedule     = OSS_Schedule()
        self.result       = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)


    def test_sessions_mapped_by_size(self):
        self.result = self.schedule.sessions_mapped_by_size()

    def test_df_sessions_registered_participants(self):
        self.result = self.schedule.df_sessions_registered_participants()



