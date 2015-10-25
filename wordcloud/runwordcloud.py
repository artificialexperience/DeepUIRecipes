#!/usr/bin/env python2
# takes in a csv twitter dump or a plain text file
# and creates a word cloud as a picture
__author__ = 'Roelof (graphific)'

from os import path
import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
            description='A command line tool to create a wordcloud from text.',
            formatter_class=argparse.RawTextHelpFormatter,
    epilog='\nExample:\n'\
                './wordcloud.py -i text.txt -o wordcloud.png (-background white -max_words 2000 -mask_file alice.png)')

    parser.add_argument('-i', '--infile', help='Filename to read text from', required=True)
    parser.add_argument('-o', '--outfile', help='Filename to create picture', required=True)
    parser.add_argument('-c', '--csv', help='Input file is twitter dump in csv', required=False)

    parser.add_argument('-b', '--background', help='background color. default: white', required=False)
    parser.add_argument('-mw', '--max_words', type=int, help='max words. default: 200', required=False)
    parser.add_argument('-mf', '--mask_file', type=str, help='(Optional) mask picture file', required=False)
    parser.add_argument('-fs', '--max_font_size', type=int, help='(Optional) mask picture file', required=False)
    parser.add_argument('-rs', '--relative_scaling', type=float, help='(Optional) relative scaling (opposed to max words, 0.0 - 1.0, ie 0.5)', required=False)
    parser.add_argument('-w', '--width', type=int, help='width. default: 400', required=False)
    parser.add_argument('-h', '--height', type=int, help='height, default: 200', required=False)
    parser.add_argument('-m', '--margin', type=int, help='margin. default: 2', required=False)


    args = parser.parse_args()

    if args.background is None: args.background = 'white'
    if args.max_words is None: args.max_words = 200
    if args.relative_scaling is None: args.relative_scaling = 0
    if args.width is None: args.width = 400
    if args.height is None: args.height = 200
    if args.margin is None: args.margin = 2
    if args.csv is None: args.csv = False else: args.csv = True

    if not args.infile:
        print('Please provide a filename to read the text from.')
        quit()
    if not args.outfile:
        print('Please provide a filename for creating the output png file.')
        quit()

    if args.csv:
        import pandas as pd
        df = pd.read_csv(args.infile)
        # join tweets to a single string
        words = ' '.join(tm.df['tweet'])

        # remove URLs, RTs, and twitter handles
        text = " ".join([word for word in words.split()
                                    if 'http' not in word
                                        and not word.startswith('@')
                                        and word != 'RT'
                                    ])
    else:
        # Read the whole text.
        text = open(args.infile)).read()

    if not args.mask_file:
        wc = WordCloud(background_color=args.background, relative_scaling=args.relative_scaling,stopwords=STOPWORDS.add("said"), max_words=args.max_words, width=args.width, height=args.height, margin=args.margin)
    else:
        alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))
        wc = WordCloud(background_color=args.background, relative_scaling=args.relative_scaling, mask=alice_mask,stopwords=STOPWORDS.add("said"), max_words=args.max_words, width=args.width, height=args.height, margin=args.margin)

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(args.outfile)

    return args.outfile
