# Flask Video Streaming

This project supports three different camera drivers.
To make it easier to select which driver to use without having to edit the code,
the Flask server looks for a `CAMERA` environment variable to know which camera class to import.
This variable can be set to `pi` or `opencv`, and if it isn't set,
then the emulated camera is used by default.

```bash
# stream video from the opencv camera
CAMERA=opencv python3 app.py

# stream video from the raspberry pi camera
CAMERA=opencv python3 app.py

# stream from video emulator
python3 app.py
```

## Running in Jupyter
environment variables
comment out imports
deactivate the camera_pi.py code.

## Ports
Flask by default serves to port 5000.
This could potentially be a problem if other applications are using that port.
You can check for this via:

```bash
 lsof -i :8000
```

I changed this because it conflicted with Jupyter, which also uses that port.
The code in `app.py` now contains:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9000', threaded=True)
```

Point your browser to `localhost:9000` to see the streaming video.

## Sources
* [Flask Video Streaming Revisited](http://blog.miguelgrinberg.com/post/flask-video-streaming-revisited)
* [Video Streaming with Flask](http://blog.miguelgrinberg.com/post/video-streaming-with-flask)

