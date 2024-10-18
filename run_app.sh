export PYTHONPATH=.:gd_demo
uvicorn main:app --reload --host 0.0.0.0 --port 9000 --log-level debug