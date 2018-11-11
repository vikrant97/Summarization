from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import time
import math
import sys
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
from optparse import OptionParser
from models.dynamic_m2_model import *
from models.basic_files.dataset_iterator import *
from test_model import *
import os


def main():

    c = Config(sys.argv[1])
    with tf.device('/device:gpu:0'):
        run_attention = run_model(c.config_dir["working_dir"], BasicAttention(), c)
        run_attention.run_training()


if __name__ == '__main__':
    main()
