"""
Unit and regression test for the projectname package.
"""

# Import package, test suite, and other packages as needed
import sys


import projectname


def test_projectname_imported():
    """Sample test, will always pass so long as import statement worked."""
    print("importing ", projectname.__name__)

    assert "projectname" in sys.modules
