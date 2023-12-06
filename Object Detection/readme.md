# Instructions to obtain results above (Evaluation)

1.	Open Google Colab
2.	Load Evaluation.ipynb
3.	Upload the Yolo Model desired to be tested (best.pt not last.pt). I.e. YOLO Models > 11072023 100epoch 16batch > result > content > yolov5 > runs > train > exp > weights > best.pt
4.	Upload the test.zip (test.zip is generated from the IDCIAv2 dataset)
5.	Run from beginning up until the markdown line Detailed Low Mid High Raw MAE


# Instructions to obtain train/test/validation split
1.	Download IDCIAv2 dataset
2.	Unzip IDCIAv2 dataset
3.	Ensure that EDA.ipynb and ground_truth directory and images are in the same folder 

Ground_truth
+— .csv files
Images
+— .tiff files
EDA.ipynb

4.	Create 3 new folders and name them train, test, validate
5.	Run EDA.ipynb 

# Instructions to obtain test.zip
1.	Run Instruction to obtain train/test/validation split
2.	Zip the test folder

# Instructions to prepare train/validation for yolo training
1.	Run Instruction to obtain train/test/validation split
2.	Drag maketxt.py file to the train and validation folder
3.	Run maketxt.py file for both train and validation to obtain yolo training format
4.	Create a folder called datasets and index in the folder
5.	Create a folder called cell counting and index in the folder
6.	Create two folders called train and valid
7.	For both train and valid, create 2 new folders within them called images and labels
8.	Put training images in the train > images folder
9.	Put training labels (the txt files) in the train > labels folder
10.	Put validation images in the valid > images folder
11.	Put validation labels (the txt files) in the valid> labels folder
12.	Go back to the datasets folder and zip the folder

# Instructions to train yolo models
1.	Open google colab
2.	Open YOLOV5_EXP.ipynb
3.	Upload the dataset.zip file created in Instructions to prepare train/validation for yolo training
4.	Upload cell.yaml to the data folder of yolo
5.	Run blocks of code uptill !zip -r result.zip/content/yolov5/runs/train/exp/

# Instructions to obtain 5px * 5px batch
1.	Do Instructions to prepare train/validation for yolo training up to step 2
2.	Change line 10 and line 11 of maketxt.py to 
xwidth = 5/width
ywidth = 5/height
3.	Continue with Instructions to prepare train/validation for yolo training up until the end

# Instructions to obtain downsampling batch
1.	Do Instructions to prepare train/validation for yolo training up to step 3
2.	Copy and paste Downsampling Scripts.ipynb into the train folder
3.	Create another folder in the directory called train
4.	Run Downsampling Scripts.ipynb
5.	Use the newly created train folder which contains 150 samples as the training dataset
6.	Continue Instructions to prepare train/validation for yolo training up till the end to obtain yolo format training and validation dataset for downsampling batch
