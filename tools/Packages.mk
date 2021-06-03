LIBS := $(shell for pkg in `grep -o '"\.\.\/.*"' pyproject.toml | sed -e 's/"//g'`; do echo $$pkg; done)
WHEELS := $(LIBS:%=%/dist/*.whl)
BUILD_DIR := .

.PHONY: all clean

all: $(BUILD_DIR)/dist/*.whl

clean:
	-rm $(WHEELS) $(BUILD_DIR)/dist/*.whl $(BUILD_DIR)/dist/deps/*.whl

reset: clean
	-rm -rf .venv poetry.lock dist
	poetry install

$(BUILD_DIR)/dist/deps: 
	mkdir -p $(BUILD_DIR)/dist/deps

$(WHEELS): $(BUILD_DIR)/dist/deps 
	mkdir -p $(@D)
	cd $(@D)/../ && poetry build
	cp $@ ${BUILD_DIR}/dist/deps/.

$(BUILD_DIR)/dist/%.whl: $(BUILD_DIR)/dist/deps/*.whl
	poetry build

$(BUILD_DIR)/dist/deps/%.whl: $(WHEELS)
	@echo $@ > /dev/null



