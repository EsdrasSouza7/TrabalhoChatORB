# OmniORB - getting started

## 1. Create and activate a CONDA env

    $ conda create -n omni-env -c conda-forge python=3.10 omniorb omniorbpy

    $ conda activate omni-env

## 2. Generate Python Code from IDL

    $ omniidl -bpython Example.idl

## 3. Run the OmniORB Service:

    $ omniNames -start

## 3. Run the Server:

    $ python Server.py

## 4. Run the Client:

    $ python Client.py

## 5. Enter the IOR obtained from the server terminal:

    $ Enter IOR of Greetings object:

    IOR:010000001a00000049444c3a4578616d706c6....

    Message from server: Hello from OmniORBpy!
