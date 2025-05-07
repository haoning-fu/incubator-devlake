from typing import Iterable

import pydevlake as dl


class JFrogPluginConnection(dl.Connection):
    pass


class JFrogPluginScopeConfig(dl.ScopeConfig):
    pass


class JFrogPluginToolScope(dl.ToolScope):
    pass


class JFrogPlugin(dl.Plugin):
    connection_type = JFrogPluginConnection
    tool_scope_type = JFrogPluginToolScope
    scope_config_type = JFrogPluginScopeConfig
    streams = []

    def domain_scopes(self, tool_scope: MyScope) -> Iterable[dl.DomainScope]:
        ...

    def remote_scope_groups(self, connection: JFrogPluginConnection) -> Iterable[dl.RemoteScopeGroup]:
        ...

    def remote_scopes(self, connection, group_id: str) -> Iterable[JFrogPluginToolScope]:
        ...

    def test_connection(self, connection: JFrogPluginConnection) -> dl.TestConnectionResult:
        ...


if __name__ == '__main__':
    JFrogPlugin.start()