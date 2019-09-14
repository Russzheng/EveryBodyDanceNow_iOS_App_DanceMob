# DanceMob: Mobile Real-Time Motion Transfer – iOS
UC Berkeley Master of Engineering Capstone Project

#### References:
* [Everybody dance now](https://arxiv.org/abs/1808.07371)
* [Pix2PixHD](https://github.com/NVIDIA/pix2pixHD)
* [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
* [OpenPose ShuffleNet Version](https://github.com/tensorboy/pytorch_Realtime_Multi-Person_Pose_Estimation)
* [iOS Mobile Pose Estimation](https://github.com/tucan9389/PoseEstimation-CoreML)

#### What We Have Done:
* Converted OpenPose Caffe models to PyTorch Models with [MMdnn](https://github.com/Microsoft/MMdnn)
* Converted Caffe/PyTorch to CoreML models with [CoreMLTools](https://developer.apple.com/documentation/coreml/converting_trained_models_to_core_ml)
* Shrunk size of detectors and generators significantly
* Deployed both CoreML models in an iOS app
