from git_gopher.CommandInterface import CommandInterface
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.GitDataGetter import GitDataGetter

class UpstreamPush(CommandInterface):
    def __init__(self, hist_command_runner: HistoryCommandRunner, git_data_getter: GitDataGetter):
        self._hist_command_runner = hist_command_runner
        self._git_data_getter = git_data_getter

    def run(self):
        branch = self._git_data_getter.get_current_branch_name()
        preview = 'echo "git push -u {2} ' + branch + '"'
        remote = self._git_data_getter.get_remote_name(preview=preview)

        if remote:
            return self._hist_command_runner.run(['git', 'push', '-u', remote, branch])
