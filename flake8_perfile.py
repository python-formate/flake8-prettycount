# stdlib
from configparser import ConfigParser
from pprint import pprint
from typing import Any, Dict

# 3rd party
from domdf_python_tools.paths import PathPlus

# this package
from flake8_prettycount.__main__ import main
from flake8_prettycount.application import Application


def parse_config():
	parser = ConfigParser()
	parser.read_string(PathPlus("tox.ini").read_text())

	config: Dict[str, Dict[str, Any]] = {
			"flake8": dict(parser["flake8"]),
			}

	for section in [sec for sec in parser.sections() if sec.startswith("flake8:")]:
		if "inherit" in parser[section]:
			config[section] = dict(config[parser[section]["inherit"]])
		else:
			config[section] = {}

		for key, value in parser[section].items():
			config[key] = value.format_map(config[section])

	# pprint(config)

	for filename in PathPlus("flake8_prettycount").rglob("*.py*"):
		print(filename)
		for section in config:
			app = Application()

			if section.startswith("flake8:") and filename.match(section[7:]):
				args = [str(filename)]

				if "select" in config[section]:
					args.extend(["--select", config[section]["select"].replace(' ', ',')])
				if "ignore" in config[section]:
					args.extend(["--ignore", config[section]["ignore"].replace(' ', ',')])

				app.run(args)

			# app.exit()


if __name__ == "__main__":
	parse_config()
