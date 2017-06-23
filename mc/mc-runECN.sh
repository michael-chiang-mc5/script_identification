#!/bin/bash

cd ../ECN/data/

python ../scripts/extract_test_patches.py > ../caffe_models/siw13_simple_5_3_3_1/test_data.txt
cd ..
./tools/eval_siw13 caffe_models/siw13_simple_5_3_3_1/deploy.prototxt caffe_models/siw13_ECNx10_5_3_3_1/siw13_ECNx10_5_3_3_1_train_iter_50000.caffemodel caffe_models/siw13_simple_5_3_3_1/image_mean.binaryproto caffe_models/siw13_simple_5_3_3_1/labels.txt caffe_models/siw13_simple_5_3_3_1/test_data.txt
