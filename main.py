import cv2
import os

video_path = "Bad_Apple.mp4"

# Load the video
cap = cv2.VideoCapture(video_path)
print(f"Loaded {video_path}!")

# Get the video properties
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Obtained video properties! {num_frames} frames are about to be converted!")
print(f"FPS: {fps}")

# Set the resize factor
resize_factor = 0.25

# Calculate the new dimensions
new_width = int(width * resize_factor)
new_height = int(height * resize_factor)

# Print the original and new dimensions
print(f'Original dimensions: {width}x{height}')
print(f'New dimensions: {new_width}x{new_height}')

# Initialize an empty list to store the frames
frames = []

# Iterate through the video frames
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Resize the frame
    frame = cv2.resize(frame, (new_width, new_height))

    # Convert the frame to black and white
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, bw_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

    # Convert the frame to a list of lists with 1's and 0's
    frame_list = [[int(pixel == 255) for pixel in row] for row in bw_frame]

    # Append the frame list to the frames list
    frames.append(frame_list)

    print(f"Frame {len(frames)}/{num_frames} converted!")

    # Save the frame to a text file
    filename = f'frame_{len(frames)}.txt'
    filepath = os.path.join('frames', filename)

    with open(filepath, 'w') as f:
        for row in frame_list:
            row_str = ''.join(str(pixel) for pixel in row)
            f.write(row_str + '\n')

    print(f"Frame {len(frames)}/{num_frames} saved!")

# Release the video capture object
cap.release()

# Print the number of frames and the dimensions of each frame
num_frames = len(frames)
print(f'The video contains {num_frames} frames, each with dimensions {height}x{width}.')

# Print the first frame as an example
print(frames[0])
