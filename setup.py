from setuptools  import setup, find_packages


setup(name="pyAERONET",
	version="0.1.1",
	packages=find_packages(),
	install_requires=['tqdm','numpy','pandas'],
	author="Fernando Fernandes",
	author_email="fernando.allysson@usp.br",
	description="this package is useful for downloading AERONET data",
	url="https://github.com/fernandoACF28/pyAERONET",
	classifiers=["Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",],)
