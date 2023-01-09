# NER-Based-Project
NER-Based-Project

## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05- initialize the dvc project
```bash
dvc init
```

### STEP 06- commit and push the changes to the remote repository

# 🆕 Personal Infromation Tagger Based on Named entity recognition
```bash
Named entity recognition (NER) helps you easily identify the key elements in a text, like names of people, places, brands, monetary values, and more.Extracting the main entities in a text helps sort unstructured data and detect important information, which is crucial if you have to deal with large datasets.
```
# 💽 Dataset 
```bash
XTREME is a benchmark for the evaluation of the cross-lingual generalization ability of pre-trained multilingual models that covers 40 typologically diverse languages and includes nine tasks.
```
# 📚 Approach 
```bash
1. Get data and properly create text and label (Can be done using https://explosion.ai/demos/displacy-ent.
2. Use trasnformer Roberta architecture for training the ner tagger
3. Use hugging face for Robereta Tokenizer
4. Train and Deploy model for use-cases
```
## 🧑‍💻 Tech Used
```bash
1. Natural Language processing
2. Pytorch 
3. Transformer 
4. FastApi 
```
## 🏭 Industrial Use-cases 
```bash
1. Search and Recommendation system 
2. Content Classification 
3. Customer Support 
4. Research Paper Screening 
5. Automatically Summarizing Resumes 
```
## 👋 Conclusion 
```bash
We have shown how to train our own name entity tagger along with proper inplementaion of train and predict pipeline.
```