from __future__ import unicode_literals, print_function
import argparse
import os

parser = argparse.ArgumentParser(description='Generate video thumbnail')
parser.add_argument('in_filename', help='Input filename')
parser.add_argument('out_filename', help='Output filename')
parser.add_argument(
    '--time', type=int, default=0.1, help='Time offset')
parser.add_argument(
    '--width', type=int, default=120,
    help='Width of output thumbnail (height automatically determined by aspect ratio)')


def simplify_path(in_file, srt_file, out_file):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(file_dir)
    input_file = os.path.join(root_dir, "videos/"+in_file)
    output_file = os.path.join(root_dir, "outputs/"+out_file)
    srt_file = os.path.join(root_dir, "srts/"+srt_file)
    return input_file, output_file, srt_file


def gen_execution_cmd(name, srt_file_path, output):
    command = 'ffmpeg -i \'%s\' -vf "subtitles=\'%s\':force_style=\'Fontsize=24,PrimaryColour=&H0000ff&\'" -c:a copy \'%s\''
    return command % (name, srt_file_path, output)


if __name__ == '__main__':
    name, output, srt_file_path = simplify_path("earth.mp4",  "goofy.srt", "output.mp4")
    command = gen_execution_cmd(name, srt_file_path, output)
    cmd = "ffmpeg -y \
          -loop 1 -t 3 -i /Users/durgeshg/BXBDProjects/pythonWorkSpace/goofy/images/pd-1.jpg \
          -loop 1 -t 6 -i /Users/durgeshg/BXBDProjects/pythonWorkSpace/goofy/images/pd-2.jpg \
          -loop 1 -t 9 -i /Users/durgeshg/BXBDProjects/pythonWorkSpace/goofy/images/pd-3.jpg \
          -loop 1 -t 15 -i /Users/durgeshg/BXBDProjects/pythonWorkSpace/goofy/images/pd-5.jpg \
          -loop 1 -t 18 -i /Users/durgeshg/BXBDProjects/pythonWorkSpace/goofy/images/pd-6.jpg \
          -filter_complex \"concat=n=5\" -shortest \
          -c:v libx264 -pix_fmt yuv420p -c:a copy out.mp4"
    os.system(cmd)
    print("Hey Goofy!!")


