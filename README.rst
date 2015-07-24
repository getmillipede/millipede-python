millipede
=========

.. image:: https://travis-ci.org/evadot/millipede.svg
           :target: https://travis-ci.org/evadot/millipede

Print a beautifull millipede to send to your friends !!!

Basic usage::

 $ millipede 20 "Chaud devant! Mon millepatte doit passer!"
 
 Chaud devant! Mon millepatte doit passer!
 
     ╚⊙ ⊙╝
   ╚═(███)═╝
  ╚═(███)═╝
 ╚═(███)═╝
  ╚═(███)═╝
   ╚═(███)═╝
    ╚═(███)═╝
    ╚═(███)═╝
   ╚═(███)═╝
  ╚═(███)═╝
 ╚═(███)═╝
  ╚═(███)═╝
   ╚═(███)═╝
    ╚═(███)═╝
    ╚═(███)═╝
   ╚═(███)═╝
  ╚═(███)═╝
 ╚═(███)═╝
  ╚═(███)═╝
   ╚═(███)═╝
    ╚═(███)═╝

There's also a very convenient `-r` option to reverse the millipede::
 
 $ millipede -r 20 'Aaah, il est passé !'
 
  ╔═(███)═╗
   ╔═(███)═╗
    ╔═(███)═╗
     ╔═(███)═╗
     ╔═(███)═╗
    ╔═(███)═╗
   ╔═(███)═╗
  ╔═(███)═╗
 ╔═(███)═╗
  ╔═(███)═╗
   ╔═(███)═╗
    ╔═(███)═╗
     ╔═(███)═╗
     ╔═(███)═╗
    ╔═(███)═╗
   ╔═(███)═╗
  ╔═(███)═╗
 ╔═(███)═╗
  ╔═(███)═╗
   ╔═(███)═╗
     ╔⊙ ⊙╗
 
 Aaah, il est passé !

Installation from sources
==========================

::

 # create a virtualenv
 $> virtualenv myenv
 $> source myenv/bin/activate
 
 # install (for developement)
 $> pip install -e .
 # Or, to install dependencies to send SMS
 $> pip install -e .[sms]
 
 # install (for production)
 $> pip install .
