import json

import pandas as pd
import qgrid
from pbx_gs_python_utils.utils import Http
from pbx_gs_python_utils.utils.Files import Files
from pbx_gs_python_utils.utils.Json import Json


class OSS_GSheet_Data:
    def __init__(self):
        self.url   = 'https://pm27fqb78d.execute-api.eu-west-2.amazonaws.com/Prod/gsheets/participants'
        self._data = None
        #self.data_folder = Files.path_combine(__file__, '../../../../data/_sync/json')

    def get_data(self,reload=False):
        if reload or self._data is None :
            raw_data   = Http.GET(self.url)
            self._data= json.loads(raw_data)
        return self._data

    def data_participants_onsite(self,reload=False):
        return self.get_data(reload).get('onsite')
        #data = Json.load_json(Files.path_combine(self.data_folder, 'participants_onsite.json'))
        #return list(data.values())

    def data_participants_remote(self):
        return self.get_data().get('remote')
        # data = Json.load_json(Files.path_combine(self.data_folder, 'participants_remote.json'))
        # return list(data.values())

    def df_participants_onsite(self,columns=None,reload=False):
        df           = pd.DataFrame(self.data_participants_onsite(reload), columns=columns)
        # fix data
        df           = df.fillna('')
        if 'Days' in df.columns:
            df['Days']   = df['Days'  ].apply(lambda x: x.replace(' ', '').split(','))
        if 'Nights' in df.columns:
            df['Nights'] = df['Nights'].apply(lambda x: x.replace(' ', '').split(','))
            df['Nights'] = df['Nights'].apply(lambda x: x if x != [''] else [])
        return df

    def df_participants_remote(self):
        df = pd.DataFrame(self.data_participants_remote())
        return df

    def qgrid_participants_onsite(self,reload=False):
        df_onsite = self.df_participants_onsite(reload)
        return qgrid.show_grid(df_onsite)