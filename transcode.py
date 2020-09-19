import ffmpeg_streaming
import sys
import datetime
import logging
import os
from ffmpeg_streaming import Formats, Bitrate, Representation, Size, GCS, CloudManager

logging.basicConfig(filename='streaming.log', level=logging.NOTSET, format='[%(asctime)s] %(levelname)s: %(message)s')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/vignesh/Vicky/Code/Transcoder/python_transcode/presales.json"
gcs = GCS()
save_to_gcs = CloudManager().add(gcs, bucket_name="viki_trans_py", folder="transcoded_video")

video = ffmpeg_streaming.input('/Users/vignesh/Vicky/Code/Transcoder/python_transcode/sample.mp4')

def monitor(ffmpeg, duration, time_, time_left, process):
  
  per = round(time_ / duration * 100)
  sys.stdout.write(
      "\rTranscoding...(%s%%) %s left [%s%s]" %
      (per, datetime.timedelta(seconds=int(time_left)), '#' * per, '-' * (100 - per))
  )
  sys.stdout.flush()

_360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
_480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
_720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))

hls = video.hls(Formats.h264())
hls.representations(_360p, _480p, _720p)
hls.output(clouds=save_to_gcs, monitor=monitor)



""" 
LOCAL STORAGE
hls.output('/Users/vignesh/Vicky/Code/Transcoder/python_transcode/transcoded_video/sample.m3u8', monitor=monitor) 
"""