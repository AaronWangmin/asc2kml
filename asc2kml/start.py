import argparse
import asc2kml

# project_dir = "/media/slam/SHCJ01/20201219135816_WM_SHANGHAI_AFA1119"


def arg_parser():
    parser = argparse.ArgumentParser(description='Project las to image')
    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help='project path',
                        required=True)
    arg = parser.parse_args()
    return arg


if __name__ == "__main__":
    args = arg_parser()
    asc2kml.asc2kml(args.input)
    
