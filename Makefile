install:
    poetry install

run:
    poetry run brain-games

build:
    poetry build

publish:
    poetry publish

package-install:
    python3 -m pip install --user dist/*.whl
    