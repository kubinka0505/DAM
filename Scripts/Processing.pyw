if Width:
	Percentage = (Width / float(Picture.size[0]))
	Height = int(float(Picture.size[1]) * float(Percentage))
	Picture = Picture.resize((Width, Height), Filter)

print()
Picture = Picture.quantize(2)							; print("  Quantized to 2 colors...")
Picture = Picture.convert("RGB")						; print('  Converted to "RGB..."')
Picture = ImageOps.equalize(Picture)					; print("  Maximized color values...")
if Mode: Picture = ImageOps.invert(Picture)				; print("  {0}Inverted colors{1}...".format(Styles.DarkGray, Styles.Reset))
Picture = Picture.convert("RGBA")						; print('  Converted to "RGBA"...')
Replace_Color(Picture, (255,) * 4, Background_Color)	; print("  Replaced {1}white{3} to {2}{0}{3}...".format("#%02x%02x%02x".upper() % Background_Color, Styles.White, Styles.Yellow, Styles.Reset))
Replace_Color(Picture, (0,) * 4, (0,) * 4)				; print("  Replaced {0}black{1} to transparent...".format(Styles.DarkGray, Styles.Reset))
if Crop_Transparency:
	Picture = Picture.crop(Picture.getbbox())			; print("  Autocropped Picture...")
Picture = Picture.convert("P")							; print('  Converted to palettized mode...')
Picture.save(Name)										; print("  Saved image...")
print()