https://coral.ai/docs/accelerator/get-started/#runtime-on-linux

echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update

sudo apt-get install libedgetpu1-std


rtsp://admin:password@n.n.n.n:554/Streaming/Channels/101 