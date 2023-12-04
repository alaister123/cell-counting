# How to run density Estimation approach jupyter notebook 
 - Run each cell of the jupyter notebook step by step 
     - generate_image(): A function that generate the synthetic dataset
     - get_patches(): A function to generate patches 
     - CustomCellDataset() and CellDataset(): wrapper classes for pytorch data loader 
     - CellCountingModel(): A CNN model for density Estimator using the provided image patches 
     - train_and_evaluate(): a function used to train the CNN model
     - acp_estimate(): a function used to measure the acp
 
 - Train and Test datasets:
   - 60%(150 images) of the IDCIAv2  and 1000 simulated images for training 
   - 40%(100 images) of the IDCIAv2 for testing 
   
 - Resources to run the model:
     - The model can be trained in the school pronto HCR and google colab
     
 - The trained version of the model:
     vimport torch
        model= torch.load("/work/LAS/qli-lab/yas/cell_counting_best_model.pt")
        model.eval()
 





