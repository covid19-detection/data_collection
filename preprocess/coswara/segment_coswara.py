"""segment_coswara.py: segment 1 multi-utterance audio file
into many sing-utterance audio files using annotation"""

import json
import os
import glob
import scipy.io.wavfile
import pandas as pd
from argparse import ArgumentParser
from math import ceil


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--data',
                         help='path to audio data directory')
    parser.add_argument('--ann',
                         help='path to annotation directory')
    parser.add_argument('--outdir',
                        help='path to output directory')
    args = parser.parse_args()
    return args


def main():
    # Create output directory
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    audio_out = os.path.join(args.outdir, 'data')
    if not os.path.exists(audio_out):
        os.makedirs(audio_out)

    # Get legends of metadata
    legends_file = os.path.join(os.path.dirname(__file__), 'csv_labels_legend.json')
    with open(legends_file, 'r') as f:
        legends = json.load(f)
    quality = ['vol', 'cont', 'quality']
    columns = ['filename']
    columns.extend(list(legends.keys()))
    columns.extend(quality)

    # Create df containing annotations after segmentation
    df = pd.DataFrame(columns=columns)

    # Segmentation using annotations
    available_periods = os.listdir(args.ann)
    for period in available_periods:
        # Check if period is directory
        if not os.path.isdir(os.path.join(args.ann, period)):
            continue

        inds = os.listdir(os.path.join(args.ann, period))
        for i in inds:
            # Check if idx is directory
            if not os.path.isdir(os.path.join(args.data, period, i)):
                continue

            # Load metadata
            with open(os.path.join(args.data, period, i, 'metadata.json'), 'r') as f:
                metadata = json.load(f)

            files = os.listdir(os.path.join(args.ann, period, i))
            for file in files:
                # Get annotation 
                with open(os.path.join(args.ann, period, i, file), 'r') as f:
                    annotation = json.load(f)

                ####
                if annotation['quality'] == 'bad audio':
                    print(os.path.join(args.ann, period, i, file))
                ####

                # Get audio
                audio_file = os.path.join(args.data,period, i, 
                                          file.replace('_v2.json', '.wav'))
                rate, audio = scipy.io.wavfile.read(audio_file)

                # Segment
                n_utterance = (len(list(annotation)) - 5) // 2
                for idx_utt in range(1, n_utterance + 1):
                    start = annotation.get('start_{}'.format(idx_utt))
                    end = annotation.get('end_{}'.format(idx_utt))

                    # Sometimes start or end is None
                    if start is None or end is None:
                        continue

                    start = ceil(start * rate)
                    end = ceil(start * rate)

                    # add metadata to row
                    # filename format : id_type(cough, ...)_idxutt
                    filename = '{}_{}_{}.wav'.format(i, file.replace('_v2.json', ''), idx_utt)
                    row = {}
                    for col in columns:
                        if col == 'filename':
                            row[col] = filename
                        else:
                            row[col] = metadata.get(col, '')

                    for col in quality:
                        row[col] = annotation.get(col, '')
                    df = df.append(row, ignore_index=True)

                    # Save new audio
                    new_audio = audio[start:end]
                    output_name = os.path.join(args.outdir, 'data', filename)
                    scipy.io.wavfile.write(output_name, rate, new_audio)
                    count += 1

    # Save aggregated annotation
    print(df)
    df.to_csv(os.path.join(args.outdir, 'annotation.csv'), index=False)

if __name__ == '__main__':
    args = parse_args()
    main()
