import LCD_1in44
import LCD_Config
from PIL import Image, ImageDraw, ImageFont, ImageColor
import time

def main():
    LCD = LCD_1in44.LCD()

    print('> Init LCD')
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    print('> draw border')
    draw.line([(0, 0), (LCD.width-1, 0)],         fill="BLUE", width=2)
    draw.line([(LCD.width-1, 0), (LCD.width-1, LCD.height-1)], fill="BLUE", width=2)
    draw.line([(LCD.width-1, LCD.height-1), (0, LCD.height-1)], fill="BLUE", width=2)
    draw.line([(0, LCD.height-1), (0, 0)],       fill="BLUE", width=2)

    print('> draw text')
    draw.text((5, 10), "Hello, world!",          font=font, fill="RED")
    draw.text((5, 30), "Custom message line 2",  font=font, fill="GREEN")
    draw.text((5, 50), "Line 3 here",            font=font, fill="BLACK")

    # Push the image to the LCD at X=0, Y=0
    LCD.LCD_ShowImage(image, 0, 0)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        LCD.LCD_Clear()

if __name__ == "__main__":
    main()
