from subprocess import run
import os
import argparse


build_dir = ".build"
output_dir = "pdf"
uid_template = "template.tex"

states = ["debug", "release"]
state = "release"

def tempStore():
    """Sets up the build location to store all the intermediate data before we can send it to the printer"""
    if not os.path.isdir(build_dir):
        os.makedirs(build_dir)
    if not os.path.isdir(build_dir +"/" + output_dir):
        os.makedirs(build_dir + "/" + output_dir)

def clearTempStore():
    run("rm -R {}".format(build_dir), shell=True)

def getArgs():
    """Make and the argparser and collect the arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="The filename of the script to be printed")
    parser.add_argument('number_of_papers', type=int, help="The number of scripts to be printed")
    parser.add_argument('printed_so_far', type=int, default=0, nargs="?",
                        help="If you need to print another batch give the sum printed so far to stop uid collision, 0 if not stated")
    args = parser.parse_args()
    return args


def printRun(coreFile, printSize, uid_offset=0):
    """Takes a core file will print it n times with a uid, note that you can offset this with"""
    with open(uid_template) as f:
        template = f.read()

    def maketag(i):
        """Uses the template tag and will complie one for use in the laverlay process"""
        filename = build_dir + "/{}.tex".format(i)
        with open(filename, "w") as outFile:
            outFile.write(template % i)
        tag_cmd = "pdflatex -output-directory=.build {} ".format(filename)
        run(tag_cmd, shell=True)

    for i in range(uid_offset ,printSize+uid_offset):
        maketag(i)

    for i in range(uid_offset,printSize + uid_offset):
        run("pdftk {} stamp {} output {}".format(coreFile, build_dir +"/{}.pdf".format(i),
                                                 build_dir + "/" + output_dir + "/overlay_{}.pdf".format(i)), shell=True)
    run("./print.sh {}".format(build_dir + "/" + output_dir), shell=True)

    if state != "debug":
        clearTempStore()



if __name__ == "__main__":
    args = getArgs()
    tempStore()
    printRun(args.filename, args.number_of_papers, args.printed_so_far)
