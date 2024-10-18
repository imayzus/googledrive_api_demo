export PYTHONPATH=.:gd_demo
python -m pytest -vv integration_tests/test_authentication.py
python -m pytest -vv integration_tests/test_file_handler.py