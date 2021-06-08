# data_collection
### Here we can collect, clean, and preprocess data for COVID detection project.
### you can download from my drive account: https://drive.google.com/drive/folders/1yO3O4hre58RlDScMupnyzxLCj4oBRdG8?usp=sharing
#### Các bạn có thể upload các datasets sau khi đã zip/tar vào phần releases và tag các folders này với tên nguyên bản, thông tin đã làm gì đi kèm, và year_month_day (ví dụ 2021_05_29).
#### 3 notebooks có tên audio-albumentations-torchaudio-audiomentations.ipynb; Explore Data Analysis 1.ipynb; và Explore Data Analysis 2.ipynb 
* Mình làm trên dataset:[https://zenodo.org/record/4048312?fbclid=IwAR1XYUC78kSbFTa9T1C-EekPSdFx8llyKQ_fjQLJO0YNi8LdPvjN-xCQi1Y#.YLyRtjYzZpR]; 
* Paper này [https://arxiv.org/pdf/2009.11644.pdf]; 
* Source code của họ tại đây [https://c4science.ch/diffusion/10770/browse/master/?fbclid=IwAR32OoD1fk4G1x4qZbyOFkcjokeAo-mAFL-gBfu9TUQnpY3Ayv_9f8RXd7Y]. 
* Và tên trên Google Drive của mình mà các bạn đặt là public_dataset!!!!
#### Mình đưa thêm phần EDA bằng R của bạn Đỗ Quang Đạt lên đây để mọi người tiện theo dõi. 
* Dataset Đạt dùng làm EDA là từ đây: [https://www.kaggle.com/himanshu007121/coughclassifier-trial]

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
