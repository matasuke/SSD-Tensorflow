# Copyright 2015 Paul Balanca. All Rights Reserved.
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
"""Provides data for the Pascal VOC Dataset (images + annotations).
"""
import tensorflow as tf
from datasets import meat_master_common

slim = tf.contrib.slim

FILE_PATTERN = 'meat_master_2018_%s_*.tfrecord'
ITEMS_TO_DESCRIPTIONS = {
    'image': 'A color image of varying height and width.',
    'shape': 'Shape of the image',
    'object/bbox': 'A list of bounding boxes, one per each object.',
    'object/label': 'A list of labels, one per each object.',
}
# (Images, Objects) statistics on every class.
TRAIN_STATISTICS = {
    'none': (0, 0),
    'raw_beaf': (196, 385),
    'half_cooked_beaf': (234, 399),
    'cooked_beaf': (202, 292),
    'over_cooked_beaf': (94, 107),
    'raw_pork': (114, 150),
    'half_cooked_pork': (149, 182),
    'cooked_pork': (168, 218),
    'over_cooked_pork': (21, 24),
    'raw_chicken': (70, 149),
    'half_cooked_chicken': (201, 294),
    'cooked_chicken': (201, 138),
    'over_cooked_chicken': (121, 138),
    'total': (873, 2629),
}
TEST_STATISTICS = {
    'none': (0, 0),
    'raw_beaf': (1, 1),
    'half_cooked_beaf': (1, 1),
    'cooked_beaf': (1, 1),
    'over_cooked_beaf': (1, 1),
    'raw_pork': (1, 1),
    'half_cooked_pork': (1, 1),
    'cooked_pork': (1, 1),
    'over_cooked_pork': (1, 1),
    'raw_chicken': (1, 1),
    'half_cooked_chicken': (1, 1),
    'cooked_chicken': (1, 1),
    'over_cooked_chicken': (1, 1),
    'total': (20, 20),
}
SPLITS_TO_SIZES = {
    'train': 873,
    'test': 0,
}
SPLITS_TO_STATISTICS = {
    'train': TRAIN_STATISTICS,
    'test': TEST_STATISTICS,
}
NUM_CLASSES = 12


def get_split(split_name, dataset_dir, file_pattern=None, reader=None):
    """Gets a dataset tuple with instructions for reading ImageNet.

    Args:
      split_name: A train/test split name.
      dataset_dir: The base directory of the dataset sources.
      file_pattern: The file pattern to use when matching the dataset sources.
        It is assumed that the pattern contains a '%s' string so that the split
        name can be inserted.
      reader: The TensorFlow reader type.

    Returns:
      A `Dataset` namedtuple.

    Raises:
        ValueError: if `split_name` is not a valid train/test split.
    """
    if not file_pattern:
        file_pattern = FILE_PATTERN
    return meat_master_common.get_split(
        split_name,
        dataset_dir,
        file_pattern, reader,
        SPLITS_TO_SIZES,
        ITEMS_TO_DESCRIPTIONS,
        NUM_CLASSES
    )

