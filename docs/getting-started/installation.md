---
title: Installing pyDVL
alias: 
    name: installation
    text: Installing pyDVL
---

# Installing pyDVL

To install the latest release use:

```shell
pip install pyDVL
```

To use all features of influence functions use instead:

```shell
pip install pyDVL[influence]
```

This includes a dependency on [PyTorch](https://pytorch.org/) (Version 2.0 and above) 
and thus is left out by default.

In the case you use Cuda v11.2 ~ 11.8, you can enable eigen computations
(for low-rank approximations)
with [CuPy](https://docs.cupy.dev/en/stable/index.html) on GPU:

```shell
pip install pyDVL[cupy]
````

If you use a different version of Cuda,
please install CuPy [manually](https://docs.cupy.dev/en/stable/install.html).


In order to check the installation you can use:

```shell
python -c "import pydvl; print(pydvl.__version__)"
```

You can also install the latest development version from
[TestPyPI](https://test.pypi.org/project/pyDVL/):

```shell
pip install pyDVL --index-url https://test.pypi.org/simple/
```

## Dependencies

pyDVL requires Python >= 3.8, [Memcached](https://memcached.org/) for caching
and [Ray](https://ray.io) for parallelization. Additionally,
the [Influence functions][pydvl.influence] module requires PyTorch (see
 [[installation]]).

ray is used to distribute workloads both locally and across nodes. Please follow
the instructions in their documentation for installation.

## Setting up the cache

memcached is an in-memory key-value store accessible over the network. pyDVL
uses it to cache certain results and speed-up the computations. You can either
install it as a package or run it inside a docker container (the simplest). For
installation instructions, refer to the
[Getting started](https://github.com/memcached/memcached/wiki#getting-started)
section in memcached's wiki. Then you can run it with:

```shell
memcached -u user
```

To run memcached inside a container in daemon mode instead, do:

```shell
docker container run -d --rm -p 11211:11211 memcached:latest
```

!!! Warning
    To read more about caching and how it might affect your usage, in particular
    about cache reuse and its pitfalls, please read the documentation for the
    [caching module][pydvl.utils.caching].
