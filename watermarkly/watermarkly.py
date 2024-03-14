from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageDraw, ImageFont, ImageTk

THEME_COLOR = "#375362"


class WaterMarkly:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("WaterMarkly")
        self.window.config(pady=50, padx=50, bg=THEME_COLOR)
        self.title_label = Label(text="WaterMarkly", font=("Monolisa", 20, "bold"), bg=THEME_COLOR)
        self.title_label.grid(row=0, column=1, )
        self.watermark_input_label = Label(text="Watermark text", font=("Monolisa", 12, "italic"), bg=THEME_COLOR)
        self.watermark_input_label.grid(row=1, column=1)
        self.watermark_input = Entry(width=40)
        self.watermark_input.focus()
        self.watermark_input.grid(row=2, column=0, columnspan=2)
        self.choose_file_btn = Button(text="Choose File", padx=20, pady=15, command=self.image_uploader, bg="green")
        self.choose_file_btn.grid(row=3, column=0)
        self.generate_watermark_btn = Button(self.window, text="generate watermark", padx=20, pady=15,
                                             command=self.regenerate_watermark,
                                             bg="orange")
        self.generate_watermark_btn.grid(row=3, column=1)
        self.image_after = Label()
        self.image_after.grid(row=4, column=0, columnspan=2)

        self.file_path = None
        self.window.mainloop()

    def image_uploader(self):
        file_types = [("Png files", "*.png"), ("Jpg files", "*.jpg"), ("Jpeg files", "*.jpeg")]
        path = filedialog.askopenfilename(initialdir="/home/manoj-kumar/Pictures", filetypes=file_types)
        print(path.split(sep="/").pop())
        if len(path):
            self.file_path = path
            self.generate_watermark(path)
        else:
            print("No file is chosen !! Please choose a file.")

    def generate_watermark(self, file_path):
        file_name = file_path.split(sep="/").pop()
        # open image file
        with Image.open(file_path, mode="r") as image:
            # Create new image obj to draw watermark on
            watermark = Image.new("RGBA", image.size, (0, 0, 0, 0))
            # Create a drawing obj
            draw = ImageDraw.Draw(watermark)
            font_path = "/home/manoj-kumar/fonts/NovaMono/NovaMono for Powerline.ttf"
            font = ImageFont.truetype(font_path, 40)
            draw.text((100, 100), self.watermark_input.get(), font=font, fill=(255, 255, 255, 128))
            image.paste(watermark, (0, 0), watermark)
            image.save(f'results/watermarkly_{file_name}')
            pic = PhotoImage(file=f"results/watermarkly_{file_name}")
            self.image_after.config(image=pic, width=1820, height=750)
            self.image_after.image = pic

    def regenerate_watermark(self):
        self.generate_watermark(file_path=self.file_path)
