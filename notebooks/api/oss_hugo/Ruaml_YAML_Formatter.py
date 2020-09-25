from ruamel.yaml import YAML

class RuamlYAMLHandler(BaseHandler):
    """
    Load and export YAML metadata. By default, this handler uses YAML's
    "safe" mode, though it's possible to override that.
    """
    FM_BOUNDARY = re.compile(r'^-{3,}$', re.MULTILINE)
    START_DELIMITER = END_DELIMITER = "---"

    def load(self, fm, **kwargs):
        """
        Parse YAML front matter. This uses yaml.SafeLoader by default.
        """
        kwargs.setdefault('Loader', SafeLoader)
        return yaml.load(fm, **kwargs)

    def export(self, metadata, **kwargs):
        """
        Export metadata as YAML. This uses yaml.SafeDumper by default.
        """
        kwargs.setdefault('Dumper', SafeDumper)
        kwargs.setdefault('default_flow_style', False)
        kwargs.setdefault('allow_unicode', True)

        metadata = yaml.dump(metadata, **kwargs).strip()
return u(metadata) # ensure unicode