# Declare the following targets always out-of-date, so make will re-run them
# even if files/directories with these names exist
.PHONY: all doc clean

all : doc

doc :
	mkdir -p html/
	mkdir -p sources_compiled/
	cp -r source/* sources_compiled/
	######
	sphinx-apidoc -efo sources_compiled/ ../mymodule
	sphinx-build -b html sources_compiled/ html/

clean :
	find 'html/' -mindepth 1 -delete
	find 'sources_compiled/' -mindepth 1 -delete
