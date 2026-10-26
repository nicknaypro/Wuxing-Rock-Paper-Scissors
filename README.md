Wuxing Rock Paper Scissors – Oẳn tù tì Ngũ hành
A camera-based Rock Paper Scissors game inspired by the Five Elements (Wuxing) philosophy, built with Python, OpenCV, and MediaPipe.

📌 Introduction
Wuxing Rock Paper Scissors is a simple interactive game that allows players to play Oẳn tù tì using hand gestures captured through a webcam.
Unlike traditional Rock Paper Scissors, which uses three moves, this game features five elements: Metal, Wood, Water, Fire, and Earth. Each element has its own strengths and weaknesses according to the game's rules.
The project combines computer vision and a simple game system to provide an interactive gaming experience without requiring a keyboard to select moves.

✨ Features
Hand Gesture Recognition: Detects the player's hand through a webcam and recognizes supported hand gestures.
Five-Element Gameplay: Supports Metal, Wood, Water, Fire, and Earth.
Computer Opponent: Randomly selects an element for each round.
Real-Time Preview: Displays the currently recognized move on the screen.
Round Results: Shows both the player's move and the computer's move, along with the result.
Replay Support: Allows players to start another round without restarting the application.

🎮 Game Rules
The game uses five elements based on the Wu Xing concept. Each element can defeat two other elements, while choosing the same element results in a draw.
<img width="814" height="814" alt="gamerule" src="https://github.com/user-attachments/assets/00e55548-7cb3-4217-926f-22366beaaa14" />

The game follows three possible outcomes:
Win: The player's element defeats the computer's element.
Draw: Both sides choose the same element.
Lose: The computer's element defeats the player's element.

The computer randomly selects one of the five elements for each round.

🛠️ Technologies Used
Python – Main programming language.
OpenCV – Captures webcam frames and displays the game interface.
MediaPipe – Detects and tracks hand landmarks for gesture recognition.

📋 Requirements
Before running the project, make sure you have:
- Python installed.
- A working webcam.
- The required Python libraries.
- The MediaPipe hand landmark model file, hand_landmarker.task, placed in the project directory.

🚀 Installation and Setup
1. Clone the repository
git clone <repository-url>
cd <repository-folder>

Replace the placeholders with the actual URL and folder name of your repository.

2. Install the dependencies
pip install opencv-python mediapipe

3. Prepare the model file
Place hand_landmarker.task in the project root directory, alongside main.py.

4. Run the game
python main.py

Make sure your webcam is connected and available before starting the application.

🕹️ How to Play
- Run main.py to launch the game.
- Allow the application to access your webcam if prompted.
- Position your hand within the camera's view.
- Observe the move displayed on the screen to check whether your gesture is recognized correctly.
- Press Space to start a round.
- Hold a supported gesture steady while the game captures your move.
- View the result, including your move, the computer's move, and whether you win, lose, or draw.
- Press Space to play another round.
- Press Esc to exit the game.

Keep your hand clearly visible and hold your gesture steady to improve recognition.
