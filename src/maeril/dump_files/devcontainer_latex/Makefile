BUILD_DIR = build
TEX_FILE = foobar.tex


.PHONY: all
all: compile


.PHONY: compile
compile:
	latexmk -xelatex -outdir=$(BUILD_DIR) $(TEX_FILE)


.PHONY: format
format:
	tex-fmt $(TEX_FILE)


.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)
