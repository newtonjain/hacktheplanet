.PHONY: test-python ci-test-python

jenkins-test-python:
	pip install pylint
	coverage run ./manage.py test --failfast && coverage xml --omit=jump/urls.py,*/fixtures/*,jump/settings/*_settings.py,*/admin.py,*/__init__.py,*/test*.py,setup.py,manage.py --include=jump/* && flake8 jump | tee pep8.txt
	python ./setup.py sdist

test-python:
	coverage run ./manage.py test -v3; coverage report -m --omit=api/urls.py,*/fixtures/*,config/settings/*.py,*/admin.py,*/__init__.py,*/test*.py,setup.py,manage.py,templates/* --include=api/*
