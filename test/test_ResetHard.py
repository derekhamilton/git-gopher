import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.CommandRunner import CommandRunner
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.HistoryCommandRunner import HistoryCommandRunner
from git_gopher.ResetHard import ResetHard

class TestResetHard(unittest.TestCase):

    def test_run(self):
        hash = 'foo'
        command_runner = CommandRunner()
        git_data_getter = GitDataGetter(Fzf(), command_runner)
        git_data_getter.get_commit_hash = MagicMock(return_value=hash)

        hist_command_runer = HistoryCommandRunner(git_data_getter, command_runner)
        hist_command_runer.run = MagicMock()
        reset_hard = ResetHard(hist_command_runer, git_data_getter)
        reset_hard.run()

        hist_command_runer.run.assert_called_once_with(['git', 'reset', '--hard', hash])

if __name__ == '__main__':
    unittest.main()
