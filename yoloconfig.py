# The new config inherits a base config to highlight the necessary modification
_base_ = 'configs/yolo/yolov3_mobilenetv2_320_300e_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation

model = dict(
    
        bbox_head=dict(num_classes=6),
        )
# Modify dataset related settings
dataset_type = 'CocoDataset'
classes = ('missing_hole','mouse_bite','open_circuit','short','spur','spurious_copper')
data = dict(
    samples_per_gpu=24,
    workers_per_gpu=4,
    train=dict(
        type='RepeatDataset',  # use RepeatDataset to speed up training
        times=10,
        dataset=dict(
            type=dataset_type,
        img_prefix='Experiment_1/data/train',
        classes=classes,
        ann_file='Experiment_1/data/train/_annotations.coco.json')),
    val=dict(
        type=dataset_type,
        img_prefix='Experiment_1/data/valid',
        classes=classes,
        ann_file='Experiment_1/data/valid/_annotations.coco.json'),
    test=dict(
        type=dataset_type,
        img_prefix='Experiment_1/data/test',
        classes=classes,
        ann_file='Experiment_1/data/test/_annotations.coco.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
#load_from = 'Experiment_1/data/pretrained_model/ga_faster_r50_caffe_fpn_1x_coco_20200702_000718-a11ccfe6.pth'
