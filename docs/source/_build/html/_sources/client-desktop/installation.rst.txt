Installing tryton
=================

Installation
------------

Once you've downloaded and unpacked a tryton source release, enter the
directory where the archive was unpacked, and run:

::
    
    python setup.py install

Note that you may need administrator/root privileges for this step, as
this command will by default attempt to install tryton to the Python
site-packages directory on your system.

For advanced options, please refer to the easy_install_ and/or the
distutils_ documentation:

.. _easy_install: http://setuptools.readthedocs.io/en/latest/easy_install.html

.. _distutils: http://docs.python.org/inst/inst.html

To use without installation, run ``bin/tryton`` from where the archive was
unpacked.

.. .. toctree::
..    :maxdepth: 2

..    usage
