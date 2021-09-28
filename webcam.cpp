 
#include "opencv2/opencv.hpp"
#include "iostream"

int main(int, char**) {
	// open the first webcam plugged in the computer
	cv::VideoCapture camera(0);
	if (!camera.isOpened()) {
		std::cerr << "ERROR: Could not open camera" << std::endl;
		return 1;
	}

	// create a window to display the images from the webcam
	cv::Mat frame;
	camera >> frame;
	// this will contain the image from the webcam
	

	// display the frame until you press a key
	while (camera.read(frame)) {
		 
		//std::cout << "**";

		// capture the next frame from the webcam
		
		// show the image on the window
		cv::imshow("Webcam", frame);
		// wait (10ms) for a key to be pressed
		if (cv::waitKey(16) >= 0)
			continue;
	}
	return 0;
}