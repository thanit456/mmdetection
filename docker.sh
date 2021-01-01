docker run --gpus all --shm-size=8g -it \
    -v /home/thanit456/part-time/jumpai/mmdetection/data:/mmdetection/data \
    -v /home/thanit456/part-time/jumpai/mmdetection/checkpoints:/mmdetection/checkpoints \ 
    mmdetection 
