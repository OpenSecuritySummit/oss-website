from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev

from oss_hugo.OSS_Participant import OSS_Participant


class test_OSS_Participant(TestCase):

    def setUp(self):
        self.test_name    = 'Test User'
        self.participant  = OSS_Participant(self.test_name)
        self.result       = None
        self.participant.create()
        self.participant.load()

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)
        assert self.participant.delete() is True

    def test__init__(self):
        assert self.participant.base_folder == 'content/participant/'

    def test_exists(self):
        assert self.participant          .exists() is True
        assert OSS_Participant('OSS Bot').exists() is True
        assert OSS_Participant('OSS bot').exists() is True
        assert OSS_Participant('oss bot').exists() is True
        assert OSS_Participant('oss-bot').exists() is True
        assert OSS_Participant('oss_bot').exists() is False
        assert OSS_Participant('oss_bbb').exists() is False
        assert OSS_Participant('Dinis Cruz' ).exists() is True
        assert OSS_Participant('dinis cruz' ).exists() is True
        assert OSS_Participant('Dinis-Cruz' ).exists() is True
        assert OSS_Participant('Dinis Cruz ').exists() is True
        assert OSS_Participant('Dinis_Cruz' ).exists() is False
        assert OSS_Participant('Dinis Cruz_').exists() is False

    def test_field(self):
        self.participant.field('type', 'abc')
        assert self.participant.field('type') == 'abc'
        self.participant.load(True)
        assert self.participant.field('type') == 'participant'
        self.participant.field('type', 'abc')
        self.participant.save()
        self.participant.load(True)
        assert self.participant.field('type') == 'abc'

    def test_load(self):
        assert OSS_Participant('test-user.md'                    ).load().exists()
        assert OSS_Participant('Test User'                       ).load().exists()
        assert OSS_Participant('aaaa/../test-user.md'            ).load().exists()
        assert OSS_Participant('content/participant/Test User'   ).load().exists()
        assert OSS_Participant('content/participant/test-user.md').load().exists()

    def test_save(self):
        new_field = 'abc'
        new_value = '123'
        metadata  = self.participant.metadata()
        assert new_field not in set(metadata)

        metadata[new_field] = new_value             # assign value

        self.participant.data = None                # force reload
        self.participant.load()

        metadata = self.participant.metadata()
        assert new_field not in set(metadata)       # confirm still not there

        metadata[new_field] = new_value             # assign again
        self.participant.save()

        self.participant.data = None  # force reload
        self.participant.load()

        assert new_field in set(metadata)           # confirm that now it is in there









