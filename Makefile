.PHONY: pull

pull:
	git submodule update --init --recursive
	git submodule update --remote
	git submodule update --init --recursive