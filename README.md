# Telegram Object Detection Bot

This project is a Telegram bot that performs object detection on user-uploaded images using the YOLOv9 deep learning model.

## Features

- Accepts images sent to the bot via Telegram.
- Processes the images using a pre-trained YOLOv9 model.
- Returns the processed image with detected objects highlighted back to the user.
- Handles errors gracefully and ensures smooth user interaction.

## Setup

### Prerequisites

- Python 3.7+
- A valid Telegram Bot API token (create one using [BotFather](https://core.telegram.org/bots#botfather)).
- The YOLOv9 repository.

### Installation

1. Clone the YOLOv9 repository:
   ```bash
   git clone https://github.com/SkalskiP/yolov9.git
   cd yolov9
