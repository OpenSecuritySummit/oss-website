import pandas as pd
from oss_hugo.API_Hugo_OSS import API_Hugo_OSS

class OSS_Schedule:
    def __init__(self):
        self.hugo = API_Hugo_OSS()

    def sessions_mapped_by_size(self):

        mapping = []
        for path, session in self.hugo.sessions().items():
            content    = session.get('content')
            metadata   = session.get('metadata')
            page_type  = metadata.get('type')
            title      = metadata.get('title')
            track      = metadata.get('track')
            organizers = metadata.get('organizers')
            participants = metadata.get('participants')
            if not organizers: organizers = []
            if not participants: participants = []
            if type(organizers) is str: organizers = organizers.split(',')
            if type(participants) is str: participants = participants.split(',')
            if 'TBD' in organizers: organizers.remove('TBD')
            if 'Pending' in organizers: organizers.remove('Pending')
            if 'you ?' in participants: participants.remove('you ?')

            if title and page_type:
                item = {
                    'title': title,
                    'track': track,
                    'page_type': page_type,
                    'organizers': organizers,
                    'participants': participants,
                    'content': len(content),
                    'path': path
                }
                mapping.append(item)

        df_mappings = pd.DataFrame(mapping)
        df_mappings = df_mappings[['title', 'track', 'page_type', 'content', 'organizers', 'participants']]
        df_sessions = df_mappings[df_mappings['page_type'] != 'track']
        df_sessions = df_sessions.sort_values(['content'], ascending=False).reset_index(drop=True)
        return df_sessions

    #todo get the result below using pandas
    def df_sessions_registered_participants(self):
        results = {}
        for key, value in self.hugo.df_participants().to_dict(orient='index').items():
            title = value.get('title')
            sessions = value.get('sessions')
            for session in sessions:
                if results.get(session) is None: results[session] = []
                results[session].append(title)
        mappings = []
        for key, value in results.items():
            mappings.append({'title': key, 'participants': value, 'participants_count': len(value)})
        df_mappings = pd.DataFrame(mappings)
        df_mappings =  df_mappings[['title', 'participants_count', 'participants']].sort_values(['participants_count'], ascending=False)
        return df_mappings