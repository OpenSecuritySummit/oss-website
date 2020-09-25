import numpy  as np
import pandas as pd
import qgrid
from pbx_gs_python_utils.utils.Files import Files
from oss_hugo.Files_Utils import Files_Utils

from oss_hugo.Hugo_Page import Hugo_Page
from oss_hugo.OSS_GSheet_Data import OSS_GSheet_Data
from oss_hugo.OSS_Participant import OSS_Participant
from oss_hugo.OSS_Session import OSS_Session


class API_Hugo_OSS:

    def __init__(self):
        self.folder_oss = Hugo_Page().folder_oss
        self._participants = None
        self._sessions     = None

    def md_files_in_folder(self, target):
       path = Files.path_combine(self.folder_oss, target)
       return Files_Utils.all_files_recursive_with_extension(path,'.md')

    def md_files_participants(self):
        return self.md_files_in_folder(OSS_Participant().base_folder)

    def md_files_sessions(self):
        return self.md_files_in_folder(OSS_Session().base_folder)

    def load_files(self,paths,index_by_title=False):
        results = {}
        for path in paths:
            data = Hugo_Page().load(path)
            if data:
                if index_by_title:
                    results[data.get('metadata').get('title')] = data
                else:
                    results[data.get('path')] = data
        return results

    def load_oss_participants(self,paths):
        results  = {}
        for path in paths:
            participant = OSS_Participant(name=path)
            if participant.exists():
                results[participant.name] = participant
        return results

    def load_oss_sessions(self,paths):
        results  = {}
        for path in paths:
            session = OSS_Session(name=path)
            if session.exists():
                results[session.name] = session
        return results

    #def save_file(self, data):
    #@use_local_cache_if_available
    def participants(self,reload=True, return_oss_participants=False):
        if self._participants is None or reload:
            if return_oss_participants is False:         # this was the original workflow (before the creation of the OSS_Participant class)
                self._participants = self.load_files(self.md_files_participants())
            else:
                self._participants = self.load_oss_participants(self.md_files_participants())
        return self._participants

    def participants_oss(self, reload=True):
        return self.participants(reload=reload,return_oss_participants=True)

    def participants_metadatas(self):
        #return self.participants()
        return [participant.get('metadata') for participant in self.participants().values()]

    def sessions(self,reload=True, return_oss_sessions=False):
        if self._sessions is None or reload:
            if return_oss_sessions is False:                            # this was the original workflow (before the creation of the OSS_Session class)
                self._sessions = self.load_files(self.md_files_sessions())
            else:
                self._sessions = self.load_oss_sessions(self.md_files_sessions())
        return self._sessions

    def sessions_metadatas(self):
        return [session.get('metadata') for session in self.sessions().values()]

    def sessions_oss(self, reload=True):
        return self.sessions(reload=reload,return_oss_sessions=True)

    def gsheet_data(self):
        return OSS_GSheet_Data()

    def df_field(self,field):
        df = self.df_participants(['title', field])
        df[field].replace('', np.nan, inplace=True)
        df = df.dropna().reset_index(drop=True)
        df.index += 1
        return df

    def df_merged_gsheet_and_hugo_data(self,reload=False):
        df_hugo = pd.DataFrame(self.participants_metadatas())
        df_gsheet = self.gsheet_data().df_participants_onsite(reload)
        df_gsheet['GSheet'] = True
        df_hugo  ['Hugo'  ] = True
        df_hugo  ['Name'  ] = df_hugo['title']
        df_hugo = df_hugo[['Name', 'status', 'company', 'Hugo']]
        df_both = pd.merge(df_hugo, df_gsheet, on='Name', how='outer').fillna('')
        #df_both.fillna('*')
        df_both = df_both[['Name', 'company', 'Company', 'Payment Status', 'GSheet', 'Hugo']]
        df_both = df_both[df_both['Name'] != '']
        return df_both

    def df_participants(self,columns=None):
        return pd.DataFrame(self.participants_metadatas(),columns=columns)

    def df_sessions(self,columns=None, field_type=None):
        df = pd.DataFrame(self.sessions_metadatas(), columns=columns)
        if field_type:
            return df[df['type']==field_type].reset_index(drop=True)

        df['organizers'] = df['organizers'].apply(lambda x: x.split(',') if type(x) is str else x)
        return df

    def qgrid_merged_gsheet_and_hugo_data(self,reload=False):
        df_both = self.df_merged_gsheet_and_hugo_data(reload)
        return qgrid.show_grid(df_both)

    def qgrid_participants(self,columns=None):
        return qgrid.show_grid(self.df_participants(columns))