## hevi_util Makefile
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1

include INFO.py

RMALL = rm -rf
PY3 = python3
PYTEST = py.test-3 -s
SPHINX = sphinx-build

cache = ./build
prefix=/usr/local
public_html = $(HOME)/public_html/$(name)

modules = $(sort $(wildcard hevi_util/*.py))

##############################################################################

.PHONY: install develop test clean

help::
	@echo Targets:
	@echo "  install - install files into $(prefix)"
	@echo "  develop - install as development mode (symlinks)"
	@echo "  test    - run tests"
	@echo "  clean   - clean generated build files"
	@echo "  ghpages - build documentation to github pages" 

install:
	$(PY3) setup.py install --prefix=$(prefix)

develop:
	$(PY3) setup.py develop

test:
	$(PYTEST)
	
clean::
	$(RMALL) build
	$(RMALL) dist
	$(RMALL) $(name).egg-info

# $(SPHINX) -b html -d $(cache)/doctrees ./doc $(public_html)
  
public_html::
	$(SPHINX) -b html -E ./doc $(public_html)
  
ghpages:
	mkdir -p build
	-cd build && git clone --single-branch -b gh-pages git@github.com:hevi9/$(name) html
	$(SPHINX) -b html -E ./doc build/html
	cd build/html && git add .
	cd build/html && git commit -a -m "Auto update"
	cd build/html && git push origin gh-pages

	
	
