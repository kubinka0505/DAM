def Replace_Color(Image_OBJ: Image, Base_Color: tuple, Target_Color: tuple) -> Image:
	"""Replaces color from `Base_Color` to `Target_Color`, based on their RGBA tuple values."""
	R, G, B, A = Base_Color

	try: R1, G1, B1, A1 = Target_Color
	except ValueError: R1, G1, B1 = Target_Color

	New_Data = []
	for Item in Image_OBJ.getdata():
		if Item[0] == R and Item[1] == G and Item[2] == B:
			try: New_Data.append((R1, G1, B1, A1))
			except: New_Data.append((R1, G1, B1))
		else: New_Data.append(Item)

	return Image_OBJ.putdata(New_Data)

class Styles:
	"""Colored Prints."""
	White = "\33[1m"
	Red = "\033[31m"
	Green = "\033[32m"
	Yellow = "\033[33m"
	LightBlue = "\033[36m"
	DarkGray = "\033[90m"
	Bold = "\033[1m"
	Underscore = "\033[4m"
	Reset = "\033[0m"

#-----#

__BEL = ""
__BGCol = "#36393F"
__Width = 256
__name__ = "".join( [Character[0] for Character in __name__.split(" ")] ).upper()
__Formats = tuple(".bmp .ico .jpeg .jpg .png .tiff .webp".replace(" ", "").split(".")[1:])
system("")