#!/usr/bin/env python3

"""
Module tests GithubOrgClient methods
"""

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from typing import Dict
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """
    Class tests GithubOrgClient methods
    """

    @parameterized.expand(
        [
            ("google", {"name": "google"}),
            ("abc", {"name": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org: str, expected: Dict, mock_org: Mock):
        """Tests org method"""
        mock_org.return_value = expected
        obj = GithubOrgClient(org)
        self.assertEqual(obj.org, expected)
        mock_org.assert_called_once_with("https://api.github.com/orgs/" + org)
    
    def test_public_repos_url(TestCase):
        """Method tests _public_repos_url"""
