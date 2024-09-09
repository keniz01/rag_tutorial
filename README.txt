# Create virtual environment
python3 -m venv .venv && source .venv/bin/activate 

# Freeze and install packages
pip3 freeze > requirements.txt
pip3 install -r requirements.txt