PYTHON3=python3

default: crawl

all: chameleon ouroboros random-ouroboros multiquines
test: test-chameleon test-ouroboros test-random-ouroboros test-multiquines

dance: chameleon
	@$(PYTHON3) gen.py chameleon-all
	@$(PYTHON3) test.py dance

crawl: chameleon
	@$(PYTHON3) chameleon.py

chameleon:
	@$(PYTHON3) gen.py chameleon

ouroboros:
	@$(PYTHON3) gen.py ouroboros

random-ouroboros:
	@$(PYTHON3) gen.py random-ouroboros

multiquines:
	@$(PYTHON3) gen.py multiquines

test-chameleon:
	@$(PYTHON3) gen.py chameleon-all
	@$(PYTHON3) test.py chameleon

test-ouroboros:
	@$(PYTHON3) gen.py ouroboros-all
	@$(PYTHON3) test.py ouroboros

test-random-ouroboros:
	@$(PYTHON3) gen.py random-ouroboros-all
	@$(PYTHON3) test.py random-ouroboros

test-multiquines:
	@$(PYTHON3) gen.py multiquines-all
	@$(PYTHON3) test.py multiquines

