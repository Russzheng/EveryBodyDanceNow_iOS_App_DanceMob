import torch
# import caffe
import numpy as np
from torch.autograd import Variable

import test as models

# pytorch models
model = models.model
input_size = models.input_size
print(input_size)
image = np.random.randint(0, 255, (1, 3, 512, 256))
import sys; print(sys._getframe().f_code.co_name,sys._getframe().f_lineno)
from IPython import embed; embed()
input_data = image.astype(np.float32)
input_var = Variable(torch.from_numpy(input_data))

# pytorch output
model.eval()
output_var = model(input_var)
pytorch_output = output_var.data.cpu().numpy()

# caffe models
# net = caffe.Net('pose_deploy.prototxt', 'pose_iter_584000.caffemodel', caffe.TEST)

# caffe output
# reshape
# net.blobs['image'].data[...] = input_data.reshape((1, 3, 224, 224))

# caffe_output_blobs = net.forward()
# caffe_output = caffe_output_blobs.popitem()[1]


# print the input and outputs
# print(input_size, pytorch_output.shape, caffe_output.shape)
print('pytorch: min: {}, max: {}, mean: {}'.format(pytorch_output.min(), pytorch_output.max(), pytorch_output.mean()))
# print('  caffe: min: {}, max: {}, mean: {}'.format(caffe_output.min(), caffe_output.max(), caffe_output.mean()))

# diff = np.abs(pytorch_output.reshape(-1) - caffe_output.reshape(-1))
# print('   diff: min: {}, max: {}, mean: {}, median: {}'.format(diff.min(), diff.max(), diff.mean(), np.median(diff)))

import sys; print(sys._getframe().f_code.co_name,sys._getframe().f_lineno)
from IPython import embed; embed()

# 1 * 78 * (w / 8) * (h / 8)
