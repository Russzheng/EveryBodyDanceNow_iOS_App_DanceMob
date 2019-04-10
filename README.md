# EveryBodyDanceNow_iOS_App_DanceMob
UC Berkeley Master Capstone Project

#### References:
* [Pix2PixHD](https://github.com/NVIDIA/pix2pixHD).
* [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose).
* [OpenPose ShuffleNet Version](https://github.com/tensorboy/pytorch_Realtime_Multi-Person_Pose_Estimation).
* [iOS Mobile Pose Estimation](https://github.com/tucan9389/PoseEstimation-CoreML).

#### What We Have Done:
* Convert OpenPose Caffe models to PyTorch Models with [MMdnn](https://github.com/Microsoft/MMdnn)
* Convert Caffe/PyTorch to CoreML models with [CoreMLTools](https://developer.apple.com/documentation/coreml/converting_trained_models_to_core_ml)
* Shrink size of detectors and generators
* Put it into an app