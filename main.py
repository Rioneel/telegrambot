import telebot
import shutil


import os
import telebot
from telebot import types
BOT_TOKEN = '7094092093:AAHrwOOL2BWiORsteQ6pMV3bVzmAEK5Vf1A'
bot = telebot.TeleBot(BOT_TOKEN)
output_folder="/content/runs/detect/predict"
@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    print("Image Received")
    # Get the photo ID of the largest available photo
    photo = message.photo[-1]
    # Download the photo
    photo_info = bot.get_file(photo.file_id)
    photo_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{photo_info.file_path}"

    # Define the folder where images will be saved
    save_folder = "/content/yolov9/saved_images"
    try:
        shutil.rmtree("/content/yolov9/saved_images")
        shutil.rmtree("/content/yolov9/runs/detect/exp")
        shutil.rmtree("/content/yolov9/runs/detect/exp2")
        shutil.rmtree("/content/yolov9/runs/detect/exp3")
        #print(f"Directory '{directory_path}' and its contents have been removed.")
    except Exception as e:
        print(f"Error while removing directory: {e}")

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Define the image filename
    image_filename = f"{message.from_user.id}_{message.message_id}.jpg"
    image_path = os.path.join(save_folder, image_filename)

    os.system(f"wget -O {image_path} {photo_url}")
    !python detect.py \
    --img 1280 --conf 0.4 --device 0 \
    --weights '/content/drive/MyDrive/PT/v9Animals.pt' \
    --source '/content/yolov9/saved_images'

    # Send the downloaded photo back to the user
    final_image_path = os.path.join("/content/yolov9/runs/detect/exp", image_filename)

    with open(final_image_path, 'rb') as photo_file:
        print(image_path)
        bot.send_photo(message.chat.id, photo_file)

    bot.reply_to(message, "Image saved and sent!")

@bot.message_handler(func=lambda message: True)
def handle_text_messages(message):
    bot.reply_to(message, "Please send an image.")

if __name__ == "__main__":
    bot.polling(none_stop=True)