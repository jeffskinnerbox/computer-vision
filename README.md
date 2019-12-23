<!--
Maintainer:   jeffskinnerbox@yahoo.com / www.jeffskinnerbox.me
Version:      0.0.1
-->


![work-in-progress](http://www.foxbyrd.com/wp-content/uploads/2018/02/file-4.jpg "These materials require additional work and are not ready for general use.")

---

* [Tensorflow Jupyter notebook on Docker](http://containertutorials.com/docker-ml/tensorflow_jupyter.html#tensorflow-jupyter-notebook-on-docker)

# My Jupyter Notebooks
My expanding set of Jupyter Notebooks.

Pull text from `/home/jeff/blogging/content/ideas/`.


What if you Jupyter environment isn't on your local computer,
but instead on a remote compute accessible via TCP/IP?
You want to open and manipulate an Jupyter Notebook running on the remote computer.
This can be done by opening an SSH tunnel.
This tunnel will forward the port used by the remotely running Jupyter Notebook server instance
to a port on your local machine,
where it can be accessed in a browser just like a locally running Jupyter Notebook instance.

On the remote machine, start the Jupyter Notebooks server:

```bash
# on the remote machine, start the jupyter notebooks server
jupyter notebook --no-browser --port=8889
```

On the local machine, start an SSH tunnel:

```bash
# on the local machine, start an SSH tunnel
# run in background: ssh -f -N -L localhost:8888:localhost:8889 remote_user@remote_host
# run in foreground: ssh -N -L localhost:8888:localhost:8889 remote_user@remote_host
ssh -N pi@BlueRPi -L localhost:8888:localhost:8889
```

Now enter `localhost:8888` in your favorite browser to use the remote Jupyter Notebook!

**Within Chromebook ....**

1. In one window, login to desktop -- cd Jupyter-Notebooks ; jupyter notebook --no-browser --port=8889
2. In 2nd window -- ssh -N jeff@desktop -L localhost:8888:localhost:8889
3. In 3rd window -- gnome-www-browser
4. Now enter `localhost:8888` in the browser and now you can acccess the remote Jupyter Notebook!

# Jupyter Notebooks
* [Bringing the best out of Jupyter Notebooks for Data Science](https://towardsdatascience.com/bringing-the-best-out-of-jupyter-notebooks-for-data-science-f0871519ca29)
* [How to Write a Jupyter Notebook Extension](https://towardsdatascience.com/how-to-write-a-jupyter-notebook-extension-a63f9578a38c)



# Things to Add to Your Notebooks
* [ImageAI State-of-the-art Recognition and Detection AI with few lines of code](http://imageai.org/#features)
    * [Train Image Recognition AI with 5 lines of code](https://towardsdatascience.com/train-image-recognition-ai-with-5-lines-of-code-8ed0bdd8d9ba)
    * [Object Detection with 10 lines of code](https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606)
