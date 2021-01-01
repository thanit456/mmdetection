from mmdet.apis import init_detector, inference_detector
import cv2 

config_file = 'configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
# device = 'cuda:0'
device = 'cpu'

# init a detector
model = init_detector(config_file, checkpoint_file, device=device)
# inference the demo image
img = cv2.imread('demo/demo.jpg')
result = inference_detector(model, img)
print(result)
cv2.imwrite('demo/result_demo.jpg', result)