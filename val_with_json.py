#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from pycocotools.coco import COCO
from cocoeval import SelfEval
coco = COCO('D:/Data/coco2017/annotations/instances_val2017.json')

coco_dt = coco.loadRes('all_detections.json')
bbox_eval = SelfEval(coco, coco_dt, all_points=True, iou_type='bbox')
bbox_eval.evaluate()
bbox_eval.accumulate()
bbox_eval.summarize()
bbox_eval.draw_curve()

segm_eval = SelfEval(coco, coco_dt, all_points=True, iou_type='segmentation')
segm_eval.evaluate()
segm_eval.accumulate()
segm_eval.summarize()
segm_eval.draw_curve()
