
class Files_Utils:

    @staticmethod
    def all_files_recursive_with_extension(path, extension):
        import os
        files = []
        for r, d, f in os.walk(path):
            for file in f:
                if extension in file:
                    files.append(os.path.join(r, file))
        return files
