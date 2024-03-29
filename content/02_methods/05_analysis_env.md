# Analysis environment

## Python code

All analysis code was written in Python 3.9.15. Data cleaning and manipulation were done using pandas \cite{mckinney2011pandas} and NumPy \cite{numpy}. All charts were produced with MatPlotLib \cite{Hunter:2007}. Identification of duplicate references was conducted using `pydedup` (available https://github.com/TomMonks/pydedup).  Notebooks were produced using Jupyter Lab v3.5.2. 

## Dependency management

Software dependencies for the code are managed through `conda` and a conda virtual environment.  We provide details below:

```yml
name: des_review
channels:
  - conda-forge
dependencies:
  - jupyterlab=3.5.2
  - jupyterlab-spellchecker=0.7.2
  - matplotlib=3.6.2
  - numpy=1.24.1
  - pandas=1.5.2
  - pip=22.2.2
  - pydot=1.4.2
  - python=3.9.15
  - python-graphviz=0.20.1
  - seaborb=0.12.2
  - scipy==1.10.0
```

## Reference management software

The references were managed via Zotero 6.0.15.  We have created an online Zotero library that contains all references that included a computer model. 

* Papers with shared computer models: https://www.zotero.org/groups/4877863/des_papers_with_code/library

The main database of studies that were included in the data extraction phase is stored as a Comma Separated Value (CSV) file.  It can be found at the following link:

* All studies included in review: https://github.com/TomMonks/des_sharing_lit_review/blob/main/data/share_sim_data_extract.zip
* A CSV containing the best practice review: https://github.com/TomMonks/des_sharing_lit_review/blob/main/data/bp_audit.zip

## Hardware

The computational analyses were run on Intel i9-9900K CPU with 64GB RAM running the Pop!\_OS 20.04 Linux. 