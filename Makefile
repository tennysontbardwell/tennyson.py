.PHONY: devenv clean test build install-local publish-test publish-prod check-build
devenv:
	nix-shell

clean:
	rm -rf dist/ build/ *.egg-info/

test:
	nix-shell --run pytest

build: test
	nix-shell --run 'python -m build'

check-build: build
	nix-shell --run 'python -m twine check dist/*'

publish-test: clean check-build
	nix-shell --run 'python -m twine upload --sign-with AFFC0B718C7AF7AAF8B6EC2C76FA7C3D275E4D55 --repository testpypi dist/*'

publish-prod: clean check-build
	nix-shell --run 'python -m twine upload --sign-with AFFC0B718C7AF7AAF8B6EC2C76FA7C3D275E4D55  dist/*'

install-local:
	pip install -e .
