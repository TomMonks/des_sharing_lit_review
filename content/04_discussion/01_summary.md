# Summary

## Summary of main results

We found that a minority (n=43; 9%) of the 485 papers reviewed shared a simulation model either as a code or visual interactive simulation file. The trend is that sharing has increased during the study period: increasing from ~4% in 2019 to 11% in 2022.  Studies published in journal articles were also more likely to share their model (10%) compared to full conference papers (4%).  This might reflect that conference papers were work in progress and authors were not ready to share their work.  Although we note that in our one model shared via a Winter Simulation Conference paper rated very high in our quality audit (Anaganoustou et al). Regardless of the way the split is calculated sharing of health DES models does not match the findings of Jansson et al (2020) where 18% of studies shared Agent Based Simulation models in 2018. It appears that four years later DES models in health are shared far less often than ABS models in general. 

Of the 43 models shared the majority were implemented using a FOSS simulation tool such as R Simmer. This is perhaps not surprising given the freedom FOSS licenses grant authors and other researchers or health care services that may opt to reuse the work.  Whilel the FOSS finding is positive, we also found that only a minority (~30%) of models aiming to support health services care for patient and society tackle Covid-19 were shared.  

> * To do: how models were shared.
> * To do: software results - unknowns and how this matches elsewhere e.g. Brailsford review and Jansson et al.

Disappointingly, the review found that the uptake of reporting guidelines within healthcare DES was low. Cost-effectiveness studies modelling individual patient trajectories using DES were the most likely to include some mention or cite using reporting guidelines typically one of the ISPOR publications.

## Summary of quality audit results

The quality audit revealed that the tools and methods of sharing DES models could be greatly improved within health and medicine. 

### Open scholorship

We found that very few models were deposited in an open science reposistory such as Zenodo, OSF or even an academic institution. This meant that these model artefacts had no guarantees of long term storage and could not be easily cited. In the case of FOSS or code based models, authors primarily opted for linking to code version control repository such as GitHub or GitLab.  While this allowed authors to share their code it is possible that these peer reviewed links will be invalid in future years. We also found instances were model binary files used within commerical simulation software such as Anylogic were inappropiately committed to GitHub instead of an open science repository.

Similarly, the review found limited use of ORCIDs in repositorys, archives, or plaforms that shared DES models.  This meant there was no robust way for the models artefacts to be linked to a researcher and their portfolios.

The majority of DES models were shared without an open license.  If we split the models into code based and VIM based simulation software we found that VIM models were the least likely to include a clear open license.  The VIM models that did have an open license were typically journal supplementary material and by default adopted the license applied to the journal article as a whole. Without a license authors retain exclusive copywrite to their research artefacts.  This means that other researchers and potential users can view the code/model, but not reuse it or adapt it.  

> * To do: coded models shared with licenses meant for data and media e.g. Creative Commons licenses. Question - should VIMs be shared with CC? as data?

### Tools to facilitate reuse of models

In general, we found that only a minority of DES models are stored with any form of clear instruction to run the model.  This was less likely for VIM models (20%) than code based models (40%). As we did not have licensed copies of all the commerical software used it is possible that instructions were contained within the models themselves.  If this is indeed the case the authors did not describe this within papers or repositories.

Dependency management was in general of a poor quality or not used at all.  Only 25% of code based simulation models had any formal dependency management; while VIM based models faired slightly better informally by stating the version of the software used. This latter result is perhaps due to the simplicity of stating which version of the commerical 'of the shelf' DES software you are using versus a complex software environment for code based DES model. Although we note that in many cases authors did not even state the version of R or Python they were using.

Surprisingly, we found that several of the VIM based DES models shared were not downloadable - even when an author stated it could be downloaded. These were all hosted on cloud based services where the model was interactive and executable to some extent.  We found that some models shared through the same plaforms were downloadable, so a plausible explanation is that that this was just a setting that was missed by study authors.