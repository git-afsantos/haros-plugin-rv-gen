# HAROS RV Generation Plugin

This package provides a [HAROS](https://github.com/git-afsantos/haros) plugin to generate runtime monitors based on [HPL](https://github.com/git-afsantos/hpl-specs) specifications.
In essence, this plugin is just a wrapper for the [HPL RV gen](https://github.com/git-afsantos/hpl-rv-gen) library.

## Installing

Installing a pre-packaged release:

```bash
pip install haros-plugin-rv-gen
```

Installing from source:

```bash
git clone https://github.com/git-afsantos/haros-plugin-rv-gen.git
cd haros-plugin-rv-gen
pip install -e .
```

## Usage

Annotate systems and nodes with HPL properties in HAROS files to have runtime monitor generation take place.

## Bugs, Questions and Support

Please use the [issue tracker](https://github.com/git-afsantos/haros-plugin-rv-gen/issues).

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md).
