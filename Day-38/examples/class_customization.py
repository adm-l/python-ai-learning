class Plugin:
    registry = {}

    def __init_subclass__(cls, *, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if plugin_name:
            if plugin_name in Plugin.registry:
                raise ValueError(f"duplicate plugin: {plugin_name}")
            Plugin.registry[plugin_name] = cls


class JsonPlugin(Plugin, plugin_name="json"):
    pass


class CsvPlugin(Plugin, plugin_name="csv"):
    pass


def add_marker(cls):
    cls.marker = "registered"
    return cls


@add_marker
class Example:
    pass


if __name__ == "__main__":
    print("plugins:", sorted(Plugin.registry))
    print("class decorator:", Example.marker)
