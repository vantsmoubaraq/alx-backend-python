#!/usr/bin/env python3

"""
Module tests GithubOrgClient methods
"""

from unittest import TestCase, mock
from unittest.mock import patch, Mock, PropertyMock
from typing import Dict
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """
    Class tests GithubOrgClient methods
    """

    @parameterized.expand(
        [
            ("google", {"tydd": "xyrt"}),
            ("abc", {"name": "Abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org: str, expected: Dict, mock_org: Mock):
        """Tests org method"""
        mock_org.return_value = expected
        obj = GithubOrgClient(org)
        self.assertEqual(obj.org, expected)
        mock_org.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """Method tests _public_repos_url"""
        expected = "https://api.github.com/orgs/repo"
        payload = {"repos_url": "https://api.github.com/orgs/repo"}
        with patch('client.GithubOrgClient.org', PropertyMock(
                    return_value=payload)):
            obj = GithubOrgClient("TechAccess")
            self.assertEqual(obj._public_repos_url, expected)

    @patch("client.get_json")
    def test_public_repos(self, mock_obj: Mock):
        """Method tests property _public_repos"""
        expected = {"Command": "git_push"}
        mock_obj.return_value = expected

        result = "github.com/techaccess"
        with patch("client.GithubOrgClient._public_repos_url", PropertyMock(
                    return_value=result)) as mock_repo:
            obj = GithubOrgClient("TechAccess")
            self.assertEqual(obj._public_repos_url, result)
