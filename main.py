from matte import Img
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("image",help="<image_file_name>")
parser.add_argument("--extension","-e", help="-e <change extension>")
parser.add_argument("--resize","-r", help="-r <resize width>")


args = parser.parse_args()


if __name__ == "__main__":
    if(args.resize):
        Img.image_resize(args.image,int(args.resize))
    if(args.extension):
        Img.image_ext(args.image,args.extension)    