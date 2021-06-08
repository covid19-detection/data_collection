# Data Preprocessing

## 1) Coughvid Crowdsourcing dataset
Đây là phần feature extraction của bạn Đạt trên dataset Coughvid Crowndsourcing dataset:
- Link download: https://drive.google.com/file/d/1iq-GevDfaq6vQHduMDnh_fKhkJn0WYoe/view?usp=sharing
- FeatureExtraction.ipynb: code for feature extraction
- feature.csv: extracted feature for training

## 2) Coswara
Đây là phần segmentation cho dataset Coswara trên những data đã có annotation (25/05/2020 - 12/10/2020).
- Link download : https://drive.google.com/file/d/1FdXoELpbjFhR4wIZZ3ZZC1JyEi6JhDsn/view?usp=sharing

Directory structure:
```
coswara
└───annotation
│   └─── 20200525
|   └─── 20200604
│   └─── .
│   └─── .
└───audio
    └─── 20200525
    └─── 20200604
    └─── .
    └─── .
```

Command for segmentation:
```
python preprocess/coswara/segment_coswara.py --data coswara/audio --ann coswara/annotation/ --outdir segmented_coswara
```

