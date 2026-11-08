"""
Created on 2026-11-08

@author: wf
"""

import os
import subprocess

from basemkit.basetest import Basetest


class TestSetup(Basetest):
    """
    test the bash setup script, the deliverable of the one line install
    """

    def setUp(self, debug=False, profile=True):
        Basetest.setUp(self, debug=debug, profile=profile)
        self.script = os.path.join(os.path.dirname(__file__), "..", "scripts", "setup")

    def run_script(self, *args: str) -> subprocess.CompletedProcess:
        """
        run the given command line on the setup script

        Args:
            args: the command line arguments, the first one being the program

        Returns:
            subprocess.CompletedProcess: the completed process with its output
        """
        process = subprocess.run(
            list(args), capture_output=True, text=True, check=False
        )
        return process

    def test_syntax(self):
        """
        the setup script is valid bash
        """
        process = self.run_script("bash", "-n", self.script)
        self.assertEqual(0, process.returncode, process.stderr)

    def test_usage(self):
        """
        -h shows the usage and exits with 1 per the mp style
        """
        process = self.run_script("bash", self.script, "-h")
        if self.debug:
            print(process.stdout)
        self.assertEqual(1, process.returncode)
        self.assertIn("usage: setup", process.stdout)
