from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Files import Files

from oss_hugo.OSS_GSheet_Data import OSS_GSheet_Data


class test_OSS_GSheet_Data(TestCase):

    def setUp(self):
        self.gsheet_data = OSS_GSheet_Data()
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test__init__(self):
        assert type(self.gsheet_data.url) == str

    def test_get_data(self):
        assert set(self.gsheet_data.get_data()) == {'onsite','remote'}

    def test_data_participants_onsite(self):
        assert len(self.gsheet_data.data_participants_onsite()) > 100

    def test_data_participants_remote(self):
        assert len(self.gsheet_data.data_participants_remote()) > 20

    def test_df_participants_onsite(self):
        data = self.gsheet_data.df_participants_onsite()                 
        assert set(data) == { 'Accommodation','Chapter Leader','Company','Days','ID','Location','Name',
                              'Nights','Page On website','Payment Status','Project Leader',
                              'Skills/Topics','Sponsor'}
        assert type(data['Days'][0]) == list

    def test_df_participants_remote(self):
        assert set(self.gsheet_data.df_participants_remote()) == {'Location', 'ID', 'Name'}