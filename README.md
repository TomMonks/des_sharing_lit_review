[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TomMonks/des_sharing_lit_review/HEAD)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://tommonks.github.io/des_sharing_lit_review)
[![License: MIT](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
[![License: MIT](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)

# Computer model and code sharing practices in healthcare discrete-event simulation: a systematic scoping review

## Overview 
The materials and data in this repository support: Harper and Monks (2023).  *DES model sharing in healthcare: an analysis of the published literature 2019-2022*.  All materials are published under an [MIT permissive license](https://github.com/TomMonks/des_sharing_lit_review/blob/main/LICENSE). 

## Author ORCIDs

[![ORCID: Harper](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
[![ORCID: Monks](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)

## Write up of study

Methods, and Results are regularly updated in our online Jupyter Book [https://tommonks.github.io/des_sharing_lit_review](https://tommonks.github.io/des_sharing_lit_review)

A **preprint** of the study is available:

> Monks, T., & Harper, A. (2023, June 5). Computer model and code sharing practices in healthcare discrete-event simulation: a systematic scoping review. https://doi.org/10.31219/osf.io/c4ytf

**Bibtex citation:**

```bibtex
@misc{monks_harper_2023,
 title={Computer model and code sharing practices in healthcare discrete-event simulation: a systematic scoping review},
 url={osf.io/c4ytf},
 DOI={10.31219/osf.io/c4ytf},
 publisher={OSF Preprints},
 author={Monks, Thomas and Harper, Alison},
 year={2023},
 month={Jun}
}
```

## Aim and research questions:

The overarching research aim is determine to what extent authors of DES health studies share models and where models are shared how is this done.

### Primary research questions

1. What proportion of DES healthcare studies share code? 
2. How is sharing affected by FOSS, Covid-19, publication type and year of publication?
3. What proportion of studies make use of a reporting guideline?
4. What methods, tools, and resources did authors use to share their computer models and code?
5. To what extent do the DES health community follow best practice for open science when sharing computer models?
6. To what extent can the healthcare DES community improve its sharing of computer models?

## Dependencies

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)

All dependencies can be found in [`binder/environment.yml`]() and are pulled from conda-forge.  To run the code locally, we recommend install [mini-conda](https://docs.conda.io/en/latest/miniconda.html); navigating your terminal (or cmd prompt) to the directory containing the repo and issuing the following command:

> `conda env create -f binder/environment.yml`

**Online Alternatives**:

* Visit our [jupyter book](https://tommonks.github.io/des_sharing_lit_review) for interactive code and explanatory text
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
│   ├── 03_results
│   ├── 04_discussion
│   └── 04_prisma
├── data
├── LICENSE
├── README.md
└── _toc.yml
```
* `binder` - contains the environment.yml file (des_review) and all dependencies managed via conda
* `_config.yml` - configuration of our Jupyter Book
* `content` - the analysis notebooks and markdown arranged by introductory, methods, results, and PRISMA reporting checklist chapters.
* `data` - directory containing data files used by analysis notebooks. 
* `LICENSE` - details of the MIT permissive license of this work.
* `README` - what you are reading now!
* `_toc.yml` - the table of contents for our Jupyter Book.

## Study data

All study data is contained within this repository.  It can be found in the `data` sub-directory.

**Main data files:**

* `share_sim_data_extract.zip`: main study data stored as a CSV. It includes all publications carried forward to the data extraction phase.
* `bp_audit.zip`: Contains the studies and additional data extraction used within the best practice audit of shared computer models.

## Testing 

If any updates to the data are made we recommend re-running the [Data source testing notebook](https://github.com/TomMonks/des_sharing_lit_review/blob/main/content/03_results/12_data_testing_bkp.ipynb).  This will perform a set of tests on the main and best practice audit datasets to check that data is in the correct place and format. 