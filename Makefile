install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py
	
lint:
	pylint --disable=R,C sm_text.py
	
test:
	python -m pytest -vv --cov=sm_text test_sm_text.py 
	python -m pytest -vv --cov=tweet_consol_fns test_consolidate_twitter.py
	
all: install lint test 