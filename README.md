orchestra-orm
=============

Orchestra-orm (aka _Orchestra Object REST Mapper_ or _Orchestra Object Resource Mapper_) is a high level Python library for easily interacting with  [django-orchestra REST API](https://github.com/glic3rinu/django-orchestra) using object oriented concepts.



Installation
------------

    pip install orchestra-orm


Design Considerations
---------------------

The main goal of this library is to provide fast and easy access to Orchestra REST API: Open a Python interpreter and start interacting right away.

To achieve this goal we have borrowed some ideas from traditional SQL [object relational mappers](http://en.wikipedia.org/wiki/Object-relational_mapping) and applied them to an [hypermedia-driven](http://en.wikipedia.org/wiki/HATEOAS) [resource-oriented](http://en.wikipedia.org/wiki/Resource-oriented_architecture) architecture (Orchestra).

This library has been heavily inspired by [Django's ORM](https://docs.djangoproject.com/en/dev/topics/db/queries/) implementation; also using an [Active Record](http://en.wikipedia.org/wiki/Active_record_pattern) like pattern, plus concurrency based on [asynchronous non-blocking I/O](http://en.wikipedia.org/wiki/Asynchronous_I/O) and caching based on [Identity Mapping](http://en.wikipedia.org/wiki/Identity_map_pattern).

Orchestra-orm leverages the [HATEOAS](http://en.wikipedia.org/wiki/HATEOAS) discoverability of Orchestra's API; rather than relying on a predefined knowledge, resources and methods are autodiscovered on
the fly, while browsing the API.

Our hope is that you can use this library to produce brief, readable and efficient code in a fun and effortless way :)


Object Oriented Modeling
------------------------

The following diagram illustrates the classes used to model Orchestra REST API and how they relate to each other.


![](docs/images/model.png)


* ``Api`` is a good starting point for browsing. It represents the ``Base`` resource of an API and it has ``links`` to ``Manager`` and ``Action``. These relations are discovered from the Link header of the HTTP response.
* ``Manager`` is used for accessing linked ``Collections`` and ``Resources``.
* ``Actions`` are used to represent action-like endpoints (i.e. ``get-auth-token``). Actions are special methods that are not expressed using HTTP verbs (``POST``, ``GET``, etc).
* ``Collection`` is a list of uniform resources; all resources share the same media type (i.e. all registered nodes). For convinience it maintains a ``link`` back to its manager in order to proxy its methods.
* ``Resource`` is a local representation of a remote resource (i.e. a node), basically a ``Resource`` is an object with a URI. It may contain nested resources, or ``RelatedCollections``.
* ``RelatedCollection`` is a subcollection that all its resources are related to the same ``parent`` (i.e. all slivers of a particular node). A ``RelatedCollection`` is able to construct a ``lookup`` for discovering its related ``Manager``, therefore it is able to proxy its methods.
* ``ResourceSet`` is a set container that can be used to perform concurrent operations over a set of non-uniform resources.

