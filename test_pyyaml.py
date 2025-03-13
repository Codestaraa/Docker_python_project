# test_pyyaml.py
import yaml

def test_pyyaml_version():
    print(yaml.__version__)
    assert yaml.__version__ is not None  # Add an assertion to make it a valid test
