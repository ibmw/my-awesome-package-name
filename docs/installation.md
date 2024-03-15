# Installation

## Stable release

To install My Awesome Package Name, run this command in your
terminal:

``` console
pip install my-awesome-package-name
```

This is the preferred method to install My Awesome Package Name, as it will always install the most recent stable release.

If you don't have [pip][] installed, this [Python installation guide][]
can guide you through the process.

## From source

The source for My Awesome Package Name can be downloaded from
the [Github repo][].

You can either clone the public repository:

``` console
git clone git://github.com/ibmw/my-awesome-package-name
```

Or download the [tarball][]:

``` console
curl -OJL https://github.com/ibmw/my-awesome-package-name/tarball/master
```

Once you have a copy of the source, you can install it with:

``` console
pip install .
```

  [pip]: https://pip.pypa.io
  [Python installation guide]: http://docs.python-guide.org/en/latest/starting/installation/
  [Github repo]: https://github.com/%7B%7B%20cookiecutter.github_username%20%7D%7D/%7B%7B%20cookiecutter.package_name|slugify%20%7D%7D
  [tarball]: https://github.com/%7B%7B%20cookiecutter.github_username%20%7D%7D/%7B%7B%20cookiecutter.package_name|slugify%20%7D%7D/tarball/master
