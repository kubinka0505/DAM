p = ap(prog = __name__ + "." + __file__.split(".")[-1], description = __doc__, add_help = False)
pr = p.add_argument_group("Required named arguments")
pr.add_argument(
	"-i", "--image", help = "Image URL",
	default = SUPPRESS, type = str, metavar = "http://...", required = 1
	)

po = p.add_argument_group("Optional arguments")
po.add_argument(
	"-o", "--output", help = "Output directory",
	default = "./Images", type = str, metavar = str.__name__
	)
po.add_argument(
	"-w", "--width", help = "Output image width, default is {0}. 0 for original.".format(__Width),
	default = __Width, type = int, metavar = "<{0}".format(__Width)
)
po.add_argument(
	"-bg","--bgcol", help = 'Background color, default is "{0}"'.format(__BGCol),
	default = __BGCol, type = str, metavar = "#..."
	)
po.add_argument("-f","--filter", help = "Resampling filter - random if 0",
	default = 1, type = int, metavar = "0-6"
	)
po.add_argument("-h", "--help", help = "Shows this message", default = SUPPRESS, action = "help")

ps = p.add_argument_group("Switch arguments", "Defaults are True")
ps.add_argument("-c", "--crop", help = "Transparency crop switch", action = "store_true")
ps.add_argument("-m", "--mode", help = "Image colors inversion switch", action = "store_true")
ps.add_argument("-s", "--silent", help = "Disable logs", action = "store_true")
args = p.parse_known_args()[0]

#-----#

try:
	Directory = path.abspath(path.expanduser(args.output))
	Width = args.width
	Background_Color = ImageColor.getrgb(args.bgcol)

	Filter = randint(1, 5) if not args.filter else args.filter
	if not Filter: Filter = randint(0, len(Filters) - 1)

	Crop_Transparency = args.crop
	Mode = args.mode

	if args.silent:
		sys.stdout = open(devnull, "w")
		sys.stderr = open(devnull, "w")
except Exception as Error:
	raise SystemExit("{2}{0}{4}: {3}{1}{4}{5}{6}".format(
		Error.__class__.__name__, str(Error).replace(sep, "/"),
		Styles.Yellow, Styles.Red, Styles.Reset, __BEL
		)
	)