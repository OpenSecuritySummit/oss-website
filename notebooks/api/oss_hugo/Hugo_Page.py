import frontmatter
from pbx_gs_python_utils.utils.Files import Files

from oss_hugo.Files_Utils import Files_Utils


class Hugo_Page():
    def __init__(self, base_folder=None, folder_oss=None):
        self.folder_oss  = folder_oss
        self.base_folder = base_folder

        if folder_oss  is None: self.folder_oss  = Files.path_combine(__file__, '../../../..')
        if base_folder is None: self.base_folder = '.'

        self.file_template = Files.path_combine(self.folder_oss,"{0}/{1}".format(self.base_folder,'_template.md'))
        self._all_md_files = None

    def create(self, name):
        name = name.replace('.md','')
        template = self.load(self.file_template)
        template['metadata']['title'] = name
        template['path']  = template['path'].replace('_template', self.fix_name(name))
        file_path = self.md_file_path(template['path'])
        if Files.exists(file_path):
            return { 'status': 'error', 'data':'target file already existed: {0}'.format(file_path)}
        return self.save(template)

    def delete(self, name):
        if Files.exists(name):
            full_path = name
        else:
            virtual_path = "{0}/{1}".format(self.base_folder, self.fix_name(name) + '.md')
            full_path = self.md_file_path(virtual_path)
        if Files.exists(full_path) is False:
            return False
        Files.delete(full_path)

        return Files.exists(full_path) is False

    def all_md_files(self):
        if self._all_md_files is None:
            path = Files.path_combine(self.folder_oss, self.base_folder)
            self._all_md_files = Files_Utils.all_files_recursive_with_extension(path, '.md')
        return self._all_md_files

    def find_in_md_files(self, name):
        target_file = "{0}.md".format(self.fix_name(name))
        for md_file in self.all_md_files():
            if Files.file_name(md_file) == target_file:
                return md_file
        return None

    def fix_name(self, name):
        return name.replace(' ','-').lower()

    def md_file_path(self, virtual_path:str):
        if virtual_path.startswith('/'): virtual_path = virtual_path[1:]
        return Files.path_combine(self.folder_oss,virtual_path)

    def load(self, path):
        if Files.exists(path):
            try:
                file_data     = frontmatter.load(path)
                relative_path = path.replace(self.folder_oss,'')
                data = { 'path': relative_path , 'content': file_data.content, 'metadata': file_data.metadata }
                return data
            except Exception as error:
                print('[Hugo_Page][load] for {0} error: {1}'.format(path,error))
                

    def save(self, data):
        try:
            post              = frontmatter.Post(data.get('content'))
            post.metadata     = data.get('metadata')
            for key, value in post.metadata.items():
                default_value = '' if key not in ['sessions'] else []
                post.metadata[key] = value if value else default_value

            file_path = self.md_file_path(data['path'] )

            Files.write(file_path, frontmatter.dumps(post))
            if Files.exists(file_path):
                return { 'status': 'ok', 'data': data}
            else:
                return {'status': 'error', 'data': 'file not saved ok: {0}'.format(file_path) }
        except Exception as error:
            return { 'status': 'error', 'data': error }