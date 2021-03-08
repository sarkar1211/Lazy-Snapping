
from Seed_Pixel_Extraction import extract_seed_pixels
from k_means import kmeanalgo
from Calculation_of_probablity import calc_probability
from Display import mydisplay

from PIL import Image

def lazy_Snapping(img , si , k ) :
    s_im = si
    foreg,backg = extract_seed_pixels( s_im , img )
    c_f, i_f = kmeanalgo(k,foreg)
    c_b, i_b = kmeanalgo(k,backg)
    b_w = calc_probability(img , c_f , i_f , c_b , i_b )
    f_g , b_g = mydisplay(b_w, img)
    return f_g , b_g


if __name__ == '__main__':

    img = Image.open('./data/Lazysnapping_data/tableball.jpg')
    str_img = Image.open('./data/Lazysnapping_data/ballstrokes.png')
    lazy_Snapping(img, str_img, 64)

