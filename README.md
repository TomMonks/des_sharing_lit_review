[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/TomMonks/des_sharing_lit_review/main)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390+/)
[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://tommonks.github.io/des_sharing_lit_review)

# DES model sharing in healthcare: an analysis of the published literature 2019-2022

## Overview 
The materials and data in this repository support: Harper and Monks (2023).  *DES model sharing in healthcare: an analysis of the published literature 2019-2022*.  All materials are published under an [MIT permissive license](https://github.com/TomMonks/des_sharing_lit_review/blob/main/LICENSE). 

## Write up of study

A preprint is being prepared.  Methods, and Results are regularly updated in our online Jupyter Book [https://tommonks.github.io/des_sharing_lit_review](https://tommonks.github.io/des_sharing_lit_review)

## Aim and research questions:

The overarching research aim is determine to what extent authors of DES health studies share models and where models are shared how is this done.

### Primary research questions

1. What proportion of DES healthcare papers that share their models and code?
2. What proportion of these papers that use Free and Open Source Simulation and of these what number are shared?
3. What proportion of these papers that tackle covid-19 and share their models?
3. Do these metrics vary by the type of article: journal paper, full conference paper or book chapter?
4. How have these metrics changed in over the three years of the study?
5. What proportion of studies make use of a reporting guideline 
6. What methods, tools, and resources did authors use to share their models and code?
7. To what extent can the healthcare DES community improve its sharing of models?

## Dependencies

Code is written in Python 3.9.

All dependencies can be found in [`binder/environment.yml`]() and are pulled from conda-forge.  To run the code locally, we recommend install [mini-conda](https://docs.conda.io/en/latest/miniconda.html); navigating your terminal (or cmd prompt) to the directory containing the repo and issuing the following command:

> `conda env create -f binder/environment.yml`

**Online Alternatives**:
* Visit our [jupyter book]((https://tommonks.github.io/des_sharing_lit_review) for interactive code and explanatory text
* Run out Jupyter notebooks in binder [![Binder](https://mybinder.org/badge_logo.svg)](https://github.com/TomMonks/des_sharing_lit_review/main)

## Repo overview

```bash
.
├── binder
│   └── environment.yml
├── _config.yml
├── content
│   ├── 01_intro
│   ├── 02_methods
│   └── 03_results
├── data
├── LICENSE
├── README.md
└── _toc.yml
```
* `binder` - contains the environment.yml file (des_review) and all dependencies managed via conda
* `_config.yml` - configuration of our Jupyter Book
* `content` - the analysis notebooks and markdown arranged by introductory, methods and results chapters.
* `data` - directory containing data files used by analysis notebooks
* `LICENSE` - details of the MIT permissive license of this work.
* `README` - what you are reading now!
* `_toc.yml` - the table of contents for our Jupyter Book.
