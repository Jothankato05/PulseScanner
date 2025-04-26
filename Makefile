setup:
	./setup.sh

run:
	./run.sh --keywords "brand1,brand2"

package:
	python3 setup.py sdist bdist_wheel

release: package
	@echo "To publish, run: twine upload dist/*"

clean:
	rm -rf venv dist build *.egg-info pulsescanner.db key.key
