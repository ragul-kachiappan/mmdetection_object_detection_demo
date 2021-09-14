# The new config inherits a base config to highlight the necessary modification
_base_ = 'mmdetection/configs/faster_rcnn/faster_rcnn_r50_caffe_dc5_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=6),
        ))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('missing_hole','mouse_bite','open_circuit','short','spur','spurious_copper')
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=8,
    train=dict(
        img_prefix='/content/data/train',
        classes=classes,
        ann_file='/content/data/train/_annotations.coco.json'),
    val=dict(
        img_prefix='/content/data/valid',
        classes=classes,
        ann_file='/content/data/valid/_annotations.coco.json'),
    test=dict(
        img_prefix='/content/data/test',
        classes=classes,
        ann_file='/content/data/test/_annotations.coco.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
#load_from = 'Experiment_1/data/pretrained_model/ga_faster_r50_caffe_fpn_1x_coco_20200702_000718-a11ccfe6.pth'
