clean-pycache:
	find ./ -type d -name '__pycache__' -exec rm -rf {} +

lint:
	poetry run ruff check src/* --fix

format:
	poetry run ruff format src/*

imports:
	poetry run ruff check src/* --select I --fix

pretty:
	$(MAKE) lint
	$(MAKE) format
	$(MAKE) imports

codigo-penal-html:
	python scripts/scraper.py --output_path ./data/codigo_penal/html \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr001.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr002.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr003.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr004.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr005.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr006.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr007.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr008.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr009.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr010.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr011.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr012.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr013.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr014.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr015.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr016.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr017.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr018.html" \
		--webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr019.html"

codigo-penal-txt:
	python scripts/html-to-txt.py --input_path ./data/codigo_penal/html --output_path ./data/codigo_penal/text

codigo-penal-full:
	$(MAKE) codigo-penal-html
	$(MAKE) codigo-penal-txt