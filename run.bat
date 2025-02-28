@echo off
start "App 1" cmd /k streamlit run app.py --server.port 8501
start "App 2" cmd /k streamlit run map.py --server.port 8502
start "App 3" cmd /k python flask_server.py port 8503
