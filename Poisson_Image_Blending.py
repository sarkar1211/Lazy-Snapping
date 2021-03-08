
import cv2
import getopt
import sys
from Moving_Mask import MaskMover
from os import path
from Poisson_Editing import*

if __name__ == '__main__':
    args = {}

    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hs:t:m:p:")
    except getopt.GetoptError as err:
        print(err)
        exit(2)

    for o, a in opts:
        if o in ("-h"):
            # usage()
            exit()
        elif o in ("-s"):
            args["source"] = a
        elif o in ("-t"):
            args["target"] = a
        elif o in ("-m"):
            args["mask"] = a
        else:
            assert False, "unhandled option"

    if ("source" not in args) or ("target" not in args):
        print('Source or target not defined. Exiting..')
        exit()

    source = cv2.imread(args["source"])
    target = cv2.imread(args["target"])

    if source is None or target is None:
        print('Source or target image does not exist')
        exit()

    if source.shape[0] > target.shape[0] or source.shape[1] > target.shape[1]:
        print('Source image cannot be larger than target image.')
        exit()

    if "mask" not in args:
        print('Mask image not defined. Exiting...')
        exit()
    else:
        path_mask = args["mask"]

    print('Please move the object to desired location to apparate.\n')
    maskm = MaskMover(args["target"], path_mask)
    offsetx, offsety, path_target_mask = maskm.move_mask()

    print('Blending ...')
    mask_target = cv2.imread(path_target_mask, cv2.IMREAD_GRAYSCALE)
    offsetfinal = offsetx, offsety

    # Blend
    result_poisson_blend = edit_poisson(source, target, mask_target, offsetfinal)
    cv2.imwrite(path.join(path.dirname(args["source"]), 'final_result.png'), result_poisson_blend)

    print('Done.\n')
