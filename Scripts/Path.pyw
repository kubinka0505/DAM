try:
	try:
		Picture = args.image
		Picture = Picture.split("?")[0]
	except AttributeError:
		Picture = fd.askopenfilename(
			title = "Select visual media file",
			initialdir = path.expanduser("~/Documents"),
			filetypes = [("Static Image Files", __Formats)],
			defaultextension = ".gif"
		)
		Picture = path.abspath(Picture)
		if Picture == getcwd():
			raise AttributeError
except AttributeError:
	raise SystemExit("{1}{0}{3}: {2}No image URL inputted!{3}".format(
		Exception.__name__,
		Styles.Yellow, Styles.Red, Styles.Reset
		)
	)

#---#

__STA_TIME = time()

if not path.exists(Picture):
	with get(Picture, stream = True) as URL:
		if URL.ok:
			URL = URL.raw
			Picture = Image.open(URL)
		else:
			raise SystemExit("{3}{0}{5}: {4}URL returns status code {1}{5} ({4}{2}{5}){4}\nImage will not be processed.{5}{6}".format(
				ValueError.__name__, URL.status_code, URL.reason.title(),
				Styles.Yellow, Styles.Red, Styles.Reset, __BEL
				)
			)
else:
	Picture = Image.open(path.abspath(Picture))

if not Picture.format.lower().endswith(__Formats):
	raise SystemExit("{2}{0}{4}: {3}Invalid static image format!{4} ({3}{1}{4}){3}\nImage will not be processed.{4}{5}".format(
		ValueError.__name__, Picture.format.upper(),
		Styles.Yellow, Styles.Red, Styles.Reset, __BEL
		)
	)

Name = str(
	Directory + sep + __name__ + \
	"_" + str(time()).split(".")[1]
	).replace(sep, "/") + ".png"

Name = str(Path(Name).resolve())