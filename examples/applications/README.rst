ElectrumSV - Example Applications
=================================

These are a formalised way to run an extended version of ElectrumSV. They are intended to be
useful in the case where you need access to (for instance) an extended set of RPC
functionality that ElectrumSV has either not incorporated yet, or will not incorporate because
it does not serve the general needs.

Be warned that we do not guarantee that ElectrumSV code and internal state will not be kept
backwards compatible. If you plan to write your own application code, you will need to be
prepared to maintain it and migrate it as ElectrumSV evolves.

However, we may provide useful skeletons. These will be updated as ElectrumSV evolves, and if
you derive from these, it is with the expectation you will be willing to migrate your code
following the changes made to them.

File Upload
-----------

Two ways to upload files are 'b://' and 'Bcat'. This application extends ElectrumSV to provide
a way for users to upload files to the blockchain using either of these two different protocols
based on file size.

WARNING: Electrum historically stores wallet data in one encrypted json file that is decrypted
when loaded, and encrypted when saved. As you accrue more transactions within it which contain
file contents, it will become slower and slower to load. ElectrumSV retains this wallet
structure at this time, and is therefore unsuited to image upload.

WARNING: The Bcat specification is not entirely clear, and the errors displayed on failure when
you view the data on bico.media are unhelpful at best. If you do use this script to upload
files, do so at your own risk as you may end up having uploaded something broken.

WARNING: Use this moderately untested tool at your own risk.

Add the 'examples/applications' directory to your 'PYTHONPATH'.

Then start it the ElectrumSV daemon by::

    electrum-sv daemon -dapp esv_fileupload

Set your RPC username and password::

    electrum-sv setconfig rpcuser my_rpc_username
    electrum-sv setconfig rpcpassword my_rpc_password

This runs ElectrumSV as a daemon providing an extended JSON-RPC API. Then you can make use of
the 'fileupload.py' script, to upload files.

Run the script::

    examples/applications/fileupload.py -f my-cool-picture.jpg -eh 127.0.0.1 -ep 8888
    -u my_rpc_username -p my_rpc_password -wn spending_wallet -wp my_password

Merchant Server
---------------

ElectrumSV provides support for payment requests, both from the side of the consumer and
the merchant. This application extends ElectrumSV to provide suitable functionality for a
local web site to communicate with it via RPC, and detect payments and react to them.

This will be accompanied at a later stage by an example web site, but for now serves as an
initial example of an application.

Add the 'examples/applications' directory to your 'PYTHONPATH'.

Then start it by::

    electrum-sv daemon -dapp esv_merchant_server

