# For Bazel 3.4.1
mkdir ./bazel-3.4.1
# shellcheck disable=SC2164
cd ./bazel-3.4.1
wget https://github.com/bazelbuild/bazel/releases/download/3.4.1/bazel-3.4.1-dist.zip
sudo apt-get install build-essential openjdk-8-jdk python zip unzip
unzip bazel-3.4.1-dist.zip
env EXTRA_BAZEL_ARGS="--host_javabase=@local_jdk//:jdk" bash ./compile.sh
sudo cp output/bazel /usr/local/bin/

# shellcheck disable=SC2103
cd ..
git clone https://github.com/google/mediapipe.git

# Change directory into MediaPipe root directory
# shellcheck disable=SC2164
cd mediapipe

sudo apt-get install libopencv-core-dev libopencv-highgui-dev \
                     libopencv-calib3d-dev libopencv-features2d-dev \
                     libopencv-imgproc-dev libopencv-video-dev

cd ..
wget https://raw.githubusercontent.com/google/mediapipe/master/setup_opencv.sh
bash ./setup_opencv.sh
