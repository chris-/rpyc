.. _api-ref:

API Reference
=============

Serialization
-------------
.. toctree::   
   :maxdepth: 1
   :hidden:
   
   api/core_brine

* :ref:`api-brine` - A simple and fast serialization format for immutable data (numbers, string, 
  tuples, etc.). Brine is the "over-the-wire" encoding format of RPyC.

* :ref:`api-vinegar` - A configurable serializer for exceptions. Vinegar extracts the exception's
  details and stores them in a brine-friendly format.

IO Layer
--------
.. toctree::
   :maxdepth: 1
   :hidden:
   
   api/core_stream

* :ref:`api-stream` - The stream layer (byte-oriented, platform-agnostic streams)

* :ref:`api-channel` - The channel layer (framing and compression)

Protocol
--------
.. toctree::
   :maxdepth: 1
   :hidden:
   
   api/core_netref
   api/core_protocol
   api/core_service


* :ref:`api-protocol` - The RPyC protocol (:class:`Connection <rpyc.core.protocol.Connection>` class)

* :ref:`api-service` - The RPyC service model

* :ref:`api-netref` - Implementation of transparent object proxies (netrefs) 

* :ref:`api-async` - Asynchronous object proxies (netrefs)

Server-Side
-----------
.. toctree::
   :maxdepth: 1
   :hidden:
   
   api/utils_server
   api/utils_authenticators
   api/utils_registry

* :ref:`api-server` - The core implementation of RPyC servers; includes the implementation of 
  the forking and threaded servers.

* :ref:`api-registry` - Implementation of the Service Registry; the registry is a bonjour-like
  discovery agent, with which RPyC servers register themselves, and allows clients to locate 
  different servers by name.

* :ref:`api-authenticators` - Implementation of two common authenticators, for SSL and TLSlite.

Client-Side
-----------
.. toctree::
   :maxdepth: 1
   :hidden:

   api/utils_factory
   api/utils_classic
   api/utils_ssh

* :ref:`api-factory` - general-purpose connection factories (over pipes, sockets, SSL, SSH, 
  TLSlite, etc.)

* :ref:`api-classic` - *Classic-mode* factories and utilities

* :ref:`api-helpers` - Various helpers (``timed``, ``async``, ``buffiter``, etc.)

* :ref:`api-ssh` - Wrappers for SSH, required for establishing RPyC connections over SSH tunnels.
  In order to establish such a connection, use :func:`rpyc.utils.factory.ssh_connect`.





