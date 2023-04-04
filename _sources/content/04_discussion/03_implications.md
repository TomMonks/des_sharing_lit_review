# Implications

## Reviewers

Reviewers can drastically alter the quality and quantity of DES model sharing within health and medicine. Naturally the reviewers of clinical studies, methodology and health service problems using DES models will have different technical background and knowledge.  We propose two levels of review

### Open scholarship review

Non-technical reviewers, should focus on the open scholarship of the DES model. Reviewers should encourage  authors to deposit their model in a open science archive (for example, their home institution or external such as Zenodo or OSF). Reviewers should favour this option over and above journals supplementary material. We found one instance where authors claim a model is available as supplementary material, but the journal did not provide a link. Open science repositories mint DOI, for citation and findability, and provides guarantees on persistence long term.  Reviewer's can boost findability of the models by asking authors to include their ORCID details wherever the model is deposited.  

Where necessary reviewers should also ask authors to provide an open license with their model. In our study we found that authors provided a mix of open licenses. Appropriate choices used by studies included in our review included the MIT license, GPL-3 and BSD-3. The appropriate license will depend on the project and what software has been used. Guides such as https://choosealicense.com/ can be used to support decisions.

Lastly reviewers should ask authors to provide basic steps to use and run their DES models. This does not need to include a detailed peer review, but instructions should be visible for open scholarship.

### Technical review

Given our study findings, more technical reviewers should still prioritise our recommendations for open scholarship. Long term maintainability of code based models can be maximised through the use of formal dependency management tools. The exact nature of these tools depends on the language used. R and Python were common tools used for DES in our study. Tools such as *renv* and *conda* can be used here respectively. For DES models developed in commercial software reporting guidelines should followed.  The Strengthening the Reporting of Empirical Simulation Studies for DES (STRESS-DES) includes a section on software environment.

## Researchers

To mitigate end of study time constraints (e.g. due to funding or need to publish results), and increase sharing quality, health researchers should consider open working practices from day one of their study.  For researchers using FOSS tools to build models, this could be to setup a GitHub repository (or other cloud version control) workflow. Many guides exist and are free to access; for example, from Software Carpentry (https://swcarpentry.github.io/git-novice/). Repositories can be initially setup as *private* if needed.  Raw study data, and patient records, should not be stored online. However, aggregate simulation model parameters, such as those for statistical distributions, could be included.  Authors may wish to consult our quality audit criteria to support their sharing. For example, to include an open license and deposit in a open science repository in order to mint a DOI.

We also note that many DES studies are conducted using propriety software e.g. Arena with a minority using FOSS packages such as SimPy.  While training and time is a consideration in all studies, we encourage researchers to consider a FOSS simulation tool to enable health services such as the NHS to easily take up and use their work without financial or nuanced licensing blocks. 

## Funders

The results of our study complement the findings of the Goldacre review into using health data to support research and analysis (ref Goldacre, 2022). I.e. funders should incentivise researchers to share their DES models. We echo Goldacre's call for "UKRI and/or NIHR to launch an open funding call specifically for open code projects in health data science". One addition to Goldacre's recommendations, in context of our DES findings, is that encouraging or requiring researchers to make use of well maintained FOSS simulation tools that facilitate open working and reuse.  This latter requirement should assist in raising the proportion of Covid-19 DES studies where executable models are shared.