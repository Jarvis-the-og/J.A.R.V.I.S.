🕹️ Jarvis AI Assistant

Jarvis is a Python-based intelligent personal assistant with voice commands, task automation, and smart home integration. It can interact via voice, perform tasks, and control connected devices.

🌟 Completed Features
1. Voice Interaction
Recognizes voice commands both offline and online
Speaks responses using pyttsx3

2. Task Automation
Set alarms and timers
Manage reminders
Create and manage to-do lists
File and folder operations

3. Smart Home Integration
Control IoT devices via ESP32 modules
Interact with connected devices using Python modules

4. Information & Utilities
Web search and technical question answering
Weather updates
Display system status (CPU, RAM, etc.)

🧩 Architecture & Design
Modular Python Structure: Separate modules for alarms, reminders, IoT, and core conversation engine
OOP Principles: Encapsulation, abstraction, and modularity in all major component
GUI & Console Integration: Outputs displayed via GUI in jarvis_ui.py

⚡ Installation

Clone the repository:
git clone https://github.com/<your-username>/Jarvis.git
cd Jarvis

Install required Python libraries:
pip install pyttsx3 speechrecognition pyautogui requests python-dotenv

🚀 Usage

Run the Jarvis UI:
python jarvis_ui.py

Speak commands:
“Set an alarm for 7:30 AM”
“Check system status”
“Turn on the living room lights”

Jarvis will respond via voice and GUI.
