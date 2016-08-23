FROM jeromeku/tf_keras

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

RUN python3 -m pip install jupyterhub notebook ipykernel

RUN python3 -m ipykernel install

RUN pip3 install jupyter

RUN apt-get update && apt-get -y build-dep python3-matplotlib python3-tk

RUN pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0rc0-cp34-cp34m-linux_x86_64.whl

ENTRYPOINT ["/bin/bash"]
