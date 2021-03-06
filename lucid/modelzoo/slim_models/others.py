# Copyright 2018 The Lucid Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import, division, print_function
from lucid.modelzoo.vision_base import Model, IMAGENET_MEAN


## Commenting out slim implementations of VGG16 and VGG19 because:
##
##  * They are supposed to be ports of the caffe implementation,
##    which we also provide.
##  * We can't determine the correct input range or whether they are BGR.
##  * They do no provide a softmax layer, leaving us no clear way to test them.
##

# class VGG16_slim(Model):
#   """VGG16 as implemented by the TensorFlow slim framework.
#
#   VGG16 was introduced by Simonyan & Zisserman (2014):
#   https://arxiv.org/pdf/1409.1556.pdf
#   This function provides the pre-trained reimplementation from TF slim:
#   https://github.com/tensorflow/models/tree/master/research/slim
#   We believe the weights were actually trained in caffe and ported.
#   """
#
#   model_path  = 'gs://modelzoo/VGG16.pb'
#   labels_path = 'gs://modelzoo/labels/ImageNet_standard_with_dummy.txt' #TODO
#   dataset = 'ImageNet'
#   image_shape = [224, 224, 3]
#   image_value_range = (-1, 1)
#   input_name = 'input'
#
#   layers = [
#      {'type': 'conv', 'name': 'vgg_16/conv1/conv1_1/Relu', 'size': 64} ,
#      {'type': 'conv', 'name': 'vgg_16/conv1/conv1_2/Relu', 'size': 64} ,
#      {'type': 'conv', 'name': 'vgg_16/conv2/conv2_1/Relu', 'size': 128} ,
#      {'type': 'conv', 'name': 'vgg_16/conv2/conv2_2/Relu', 'size': 128} ,
#      {'type': 'conv', 'name': 'vgg_16/conv3/conv3_1/Relu', 'size': 256} ,
#      {'type': 'conv', 'name': 'vgg_16/conv3/conv3_2/Relu', 'size': 256} ,
#      {'type': 'conv', 'name': 'vgg_16/conv3/conv3_3/Relu', 'size': 256} ,
#      {'type': 'conv', 'name': 'vgg_16/conv4/conv4_1/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_16/conv4/conv4_2/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_16/conv4/conv4_3/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_16/conv5/conv5_1/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_16/conv5/conv5_2/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_16/conv5/conv5_3/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_16/fc6/Relu', 'size': 4096} ,
#      {'type': 'conv', 'name': 'vgg_16/fc7/Relu', 'size': 4096} ,
#    ]


# class VGG19_slim(Model):
#   """VGG19 as implemented by the TensorFlow slim framework.
#
#   VGG19 was introduced by Simonyan & Zisserman (2014):
#   https://arxiv.org/pdf/1409.1556.pdf
#   This function provides the pre-trained reimplementation from TF slim:
#   https://github.com/tensorflow/models/tree/master/research/slim
#   We believe the weights were actually trained in caffe and ported.
#   """
#
#   model_path  = 'gs://modelzoo/VGG19.pb'
#   labels_path = 'gs://modelzoo/labels/ImageNet_standard_with_dummy.txt' #TODO
#   dataset = 'ImageNet'
#   image_shape = [224, 224, 3]
#   image_value_range = (-1, 1)
#   input_name = 'input'
#
#   layers = [
#      {'type': 'conv', 'name': 'vgg_19/conv1/conv1_1/Relu', 'size': 64} ,
#      {'type': 'conv', 'name': 'vgg_19/conv1/conv1_2/Relu', 'size': 64} ,
#      {'type': 'conv', 'name': 'vgg_19/conv2/conv2_1/Relu', 'size': 128} ,
#      {'type': 'conv', 'name': 'vgg_19/conv2/conv2_2/Relu', 'size': 128} ,
#      {'type': 'conv', 'name': 'vgg_19/conv3/conv3_1/Relu', 'size': 256} ,
#      {'type': 'conv', 'name': 'vgg_19/conv3/conv3_2/Relu', 'size': 256} ,
#      {'type': 'conv', 'name': 'vgg_19/conv3/conv3_3/Relu', 'size': 256} ,
#      {'type': 'conv', 'name': 'vgg_19/conv3/conv3_4/Relu', 'size': 256} ,
#      {'type': 'conv', 'name': 'vgg_19/conv4/conv4_1/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_19/conv4/conv4_2/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_19/conv4/conv4_3/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_19/conv4/conv4_4/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_19/conv5/conv5_1/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_19/conv5/conv5_2/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_19/conv5/conv5_3/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_19/conv5/conv5_4/Relu', 'size': 512} ,
#      {'type': 'conv', 'name': 'vgg_19/fc6/Relu', 'size': 4096} ,
#      {'type': 'conv', 'name': 'vgg_19/fc7/Relu', 'size': 4096} ,
#    ]


class NasnetMobile_slim(Model):
  """NasnetMobile as implemented by the TensorFlow slim framework.

  This function provides the pre-trained reimplementation from TF slim:
  https://github.com/tensorflow/models/tree/master/research/slim
  """

  model_path  = 'gs://modelzoo/vision/slim_models/NasnetMobile.pb'
  labels_path = 'gs://modelzoo/labels/ImageNet_standard_with_dummy.txt' #TODO
  dataset = 'ImageNet'
  image_shape = [224, 224, 3]
  # inpute range taken from:
  # https://github.com/tensorflow/models/blob/master/research/slim/preprocessing/inception_preprocessing.py#L280
  image_value_range = (-1, 1)
  input_name = 'input'
  layers = [
    {'type': 'conv', 'name': 'conv0/Conv2D', 'size': 32},
    {'type': 'conv', 'name': 'cell_stem_0/cell_output/concat', 'size': 44},
    {'type': 'conv', 'name': 'cell_stem_1/cell_output/concat', 'size': 88},
    {'type': 'conv', 'name': 'cell_0/cell_output/concat', 'size': 264},
    {'type': 'conv', 'name': 'cell_1/cell_output/concat', 'size': 264},
    {'type': 'conv', 'name': 'cell_2/cell_output/concat', 'size': 264},
    {'type': 'conv', 'name': 'cell_3/cell_output/concat', 'size': 264},
    {'type': 'conv', 'name': 'reduction_cell_0/cell_output/concat', 'size': 352},
    {'type': 'conv', 'name': 'cell_4/cell_output/concat', 'size': 528},
    {'type': 'conv', 'name': 'cell_5/cell_output/concat', 'size': 528},
    {'type': 'conv', 'name': 'cell_6/cell_output/concat', 'size': 528},
    {'type': 'conv', 'name': 'cell_7/cell_output/concat', 'size': 528},
    {'type': 'conv', 'name': 'reduction_cell_1/cell_output/concat', 'size': 704},
    {'type': 'conv', 'name': 'cell_8/cell_output/concat', 'size': 1056},
    {'type': 'conv', 'name': 'cell_9/cell_output/concat', 'size': 1056},
    {'type': 'conv', 'name': 'cell_10/cell_output/concat', 'size': 1056},
    {'type': 'conv', 'name': 'cell_11/cell_output/concat', 'size': 1056},
    # {'type': 'dense', 'name': 'final_layer/FC/BiasAdd', 'size': 1001},
    {'type': 'dense', 'name': 'final_layer/predictions', 'size': 1001},
  ]


class NasnetLarge_slim(Model):
  """NasnetLarge as implemented by the TensorFlow slim framework.

  This function provides the pre-trained reimplementation from TF slim:
  https://github.com/tensorflow/models/tree/master/research/slim
  """

  model_path  = 'gs://modelzoo/vision/slim_models/NasnetLarge.pb'
  labels_path = 'gs://modelzoo/labels/ImageNet_standard_with_dummy.txt' #TODO
  dataset = 'ImageNet'
  image_shape = [331, 331, 3]
  # inpute range taken from:
  # https://github.com/tensorflow/models/blob/master/research/slim/preprocessing/inception_preprocessing.py#L280
  image_value_range = (-1, 1)
  input_name = 'input'
  layers = [
    {'type': 'conv', 'name': 'conv0/Conv2D', 'size': 96},
    {'type': 'conv', 'name': 'cell_stem_0/cell_output/concat', 'size': 168},
    {'type': 'conv', 'name': 'cell_stem_1/cell_output/concat', 'size': 336},
    {'type': 'conv', 'name': 'cell_0/cell_output/concat', 'size': 1008},
    {'type': 'conv', 'name': 'cell_1/cell_output/concat', 'size': 1008},
    {'type': 'conv', 'name': 'cell_2/cell_output/concat', 'size': 1008},
    {'type': 'conv', 'name': 'cell_3/cell_output/concat', 'size': 1008},
    {'type': 'conv', 'name': 'cell_4/cell_output/concat', 'size': 1008},
    {'type': 'conv', 'name': 'cell_5/cell_output/concat', 'size': 1008},
    {'type': 'conv', 'name': 'reduction_cell_0/cell_output/concat', 'size': 1344},
    {'type': 'conv', 'name': 'cell_6/cell_output/concat', 'size': 2016},
    {'type': 'conv', 'name': 'cell_7/cell_output/concat', 'size': 2016},
    {'type': 'conv', 'name': 'cell_8/cell_output/concat', 'size': 2016},
    {'type': 'conv', 'name': 'cell_9/cell_output/concat', 'size': 2016},
    {'type': 'conv', 'name': 'cell_10/cell_output/concat', 'size': 2016},
    {'type': 'conv', 'name': 'cell_11/cell_output/concat', 'size': 2016},
    {'type': 'conv', 'name': 'reduction_cell_1/cell_output/concat', 'size': 2688},
    {'type': 'conv', 'name': 'cell_12/cell_output/concat', 'size': 4032},
    {'type': 'conv', 'name': 'cell_13/cell_output/concat', 'size': 4032},
    {'type': 'conv', 'name': 'cell_14/cell_output/concat', 'size': 4032},
    {'type': 'conv', 'name': 'cell_15/cell_output/concat', 'size': 4032},
    {'type': 'conv', 'name': 'cell_16/cell_output/concat', 'size': 4032},
    {'type': 'conv', 'name': 'cell_17/cell_output/concat', 'size': 4032},
    # {'type': 'conv', 'name': 'final_layer/FC/BiasAdd', 'size': 1001},
    {'type': 'dense', 'name': 'final_layer/predictions', 'size': 1001},
  ]


class PnasnetMobile_slim(Model):
  """PnasnetMobile as implemented by the TensorFlow slim framework.

  This function provides the pre-trained reimplementation from TF slim:
  https://github.com/tensorflow/models/tree/master/research/slim
  """

  model_path  = 'gs://modelzoo/vision/slim_models/PnasnetMobile.pb'
  labels_path = 'gs://modelzoo/labels/ImageNet_standard_with_dummy.txt' #TODO
  dataset = 'ImageNet'
  image_shape = [224, 224, 3]
  # inpute range taken from:
  # https://github.com/tensorflow/models/blob/master/research/slim/preprocessing/inception_preprocessing.py#L280
  image_value_range = (-1, 1)
  input_name = 'input'
  layers = [
    {'type': 'conv', 'name': 'conv0/Conv2D', 'size': 32},
    {'type': 'conv', 'name': 'cell_stem_0/cell_output/concat', 'size': 65},
    {'type': 'conv', 'name': 'cell_stem_1/cell_output/concat', 'size': 135},
    {'type': 'conv', 'name': 'cell_0/cell_output/concat', 'size': 270},
    {'type': 'conv', 'name': 'cell_1/cell_output/concat', 'size': 270},
    {'type': 'conv', 'name': 'cell_2/cell_output/concat', 'size': 270},
    {'type': 'conv', 'name': 'cell_3/cell_output/concat', 'size': 540},
    {'type': 'conv', 'name': 'cell_4/cell_output/concat', 'size': 540},
    {'type': 'conv', 'name': 'cell_5/cell_output/concat', 'size': 540},
    {'type': 'conv', 'name': 'cell_6/cell_output/concat', 'size': 1080},
    {'type': 'conv', 'name': 'cell_7/cell_output/concat', 'size': 1080},
    {'type': 'conv', 'name': 'cell_8/cell_output/concat', 'size': 1080},
    {'type': 'dense', 'name': 'final_layer/predictions', 'size': 1001}
  ]


class PnasnetLarge_slim(Model):
  """PnasnetLarge as implemented by the TensorFlow slim framework.

  This function provides the pre-trained reimplementation from TF slim:
  https://github.com/tensorflow/models/tree/master/research/slim
  """

  model_path  = 'gs://modelzoo/vision/slim_models/PnasnetLarge.pb'
  labels_path = 'gs://modelzoo/labels/ImageNet_standard_with_dummy.txt' #TODO
  dataset = 'ImageNet'
  image_shape = [331, 331, 3]
  # inpute range taken from:
  # https://github.com/tensorflow/models/blob/master/research/slim/preprocessing/inception_preprocessing.py#L280
  image_value_range = (-1, 1)
  input_name = 'input'
  layers = [
    {'type': 'conv', 'name': 'conv0/Conv2D', 'size': 96},
    {'type': 'conv', 'name': 'cell_stem_0/cell_output/concat', 'size': 270},
    {'type': 'conv', 'name': 'cell_stem_1/cell_output/concat', 'size': 540},
    {'type': 'conv', 'name': 'cell_0/cell_output/concat', 'size': 1080},
    {'type': 'conv', 'name': 'cell_1/cell_output/concat', 'size': 1080},
    {'type': 'conv', 'name': 'cell_2/cell_output/concat', 'size': 1080},
    {'type': 'conv', 'name': 'cell_3/cell_output/concat', 'size': 1080},
    {'type': 'conv', 'name': 'cell_4/cell_output/concat', 'size': 2160},
    {'type': 'conv', 'name': 'cell_5/cell_output/concat', 'size': 2160},
    {'type': 'conv', 'name': 'cell_6/cell_output/concat', 'size': 2160},
    {'type': 'conv', 'name': 'cell_7/cell_output/concat', 'size': 2160},
    {'type': 'conv', 'name': 'cell_8/cell_output/concat', 'size': 4320},
    {'type': 'conv', 'name': 'cell_9/cell_output/concat', 'size': 4320},
    {'type': 'conv', 'name': 'cell_10/cell_output/concat', 'size': 4320},
    {'type': 'conv', 'name': 'cell_11/cell_output/concat', 'size': 4320},
    {'type': 'dense', 'name': 'final_layer/predictions', 'size': 1001}
  ]
