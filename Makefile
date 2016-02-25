## pyapi Makefile
## Copyright (C) 2014 Petri Heinilä, LGPL 2.1

RMALL = rm -rf
RM = rm -f
PIP3 = pip3
TEST = py.test

pycaches = $(shell find . -name __pycache__) 

.PHONY: install develop test clean public_html ghpages

help::
	@echo Targets:
	@echo "  dev         - install as development mode (symlinks)"
	@echo "  clean       - clean generated build files"
	@echo "  check       - validate project"

dev:
	$(PIP3) install --user -U flake8 pytest -e .	

check:: style test
	$(FLAKE) .
	$(TEST)
	
clean::
	$(RMALL) build
	$(RMALL) dist
	$(RMALL) $(name).egg-info
	$(RMALL) $(pycaches)
	

