import argparse
import os
import tempfile
from pdf2image import convert_from_path, convert_from_bytes

def extract(filename, outputDir):
    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path(filename, output_folder = path)
        for index, img in enumerate(images):
            imgname = str(index) + '.jpg'
            imgpath = os.path.join(outputDir, imgname)
            img.save(imgpath)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type = str, default = '菊部丛刊.周剑云编.1918年上海交通图书馆出版.pdf', help = 'pre-train or not')
    parser.add_argument('--outputDir', type = str, default = '菊部丛刊.周剑云编.1918年上海交通图书馆出版', help = 'savi is recommended')
    opt = parser.parse_args()

    extract(opt.filename, opt.outputDir)
