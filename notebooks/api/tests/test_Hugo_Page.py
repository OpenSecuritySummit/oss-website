from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Files import Files

from oss_hugo.Hugo_Page import Hugo_Page


class test_Hugo_Page(TestCase):

    def setUp(self):
        self.base_folder = 'content/participant'
        self.hugo_page = Hugo_Page(self.base_folder)
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)


    def test__init__(self):
        assert Files.folder_exists(self.hugo_page.folder_oss)
        assert Files.file_name(self.hugo_page.folder_oss) == 'oss2019'
        assert Files.exists(self.hugo_page.file_template)

    def test_participant_create(self):
        name = 'an test user'
        result = self.hugo_page.create(name)

        assert result.get('status') == 'ok'
        data = result.get('data')
        path = self.hugo_page.md_file_path(data['path'] )
        assert data['metadata']['title'] == 'an test user'
        assert data['path'             ] == '/content/participant/an-test-user.md'

        assert Files.exists(path)          is True
        assert self.hugo_page.delete(name) is True
        assert Files.exists(path)          is False

    def test_load_file(self):
        file_path   = self.hugo_page.file_template
        data        = self.hugo_page.load(file_path)
        assert data == {   'path'    : '/content/participant/_template.md'                                   ,
                           'content' : '<!-- put more details about participant here -->'                    ,
                           'metadata': { 'chapter_leader': ''  , 'company'    : '' , 'email'  : ''           ,
                                         'eventbrite_id' : ''  , 'facebook'   : '' , 'image'  : ''           ,
                                         'job_title'     : ''  , 'linkedin'   : '' , 'notes'  : ''           ,
                                         'project_leader': ''  , 'sessions'   : [] , 'status' : 'add-details',
                                         'title'         : ''  , 'travel_from': '' , 'twitter': ''           ,
                                         'type': 'participant' , 'website'    : ''                          }}

    def test_load_save(self):
        file_path   = self.hugo_page.file_template
        data        = self.hugo_page.load(file_path)
        result      = self.hugo_page.save(data)
        assert result.get('status') == 'ok'
