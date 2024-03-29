# Summary

## Summary of main results

We found that a minority (n=47; 8.3%) of the 564 papers reviewed shared a simulation model either as a code or visual interactive simulation file. The trend is that sharing has increased during the study period: increasing from ~4% in 2019 to 8%-10% between 2020 and 2022.  Studies published in journal articles were also more likely to share their computer model (9.7%) compared to full conference papers (4%).  This might reflect that conference papers were work in progress and authors were not ready to share their work.  Although we note that one model shared via a Winter Simulation Conference paper rated very high in our best practice audit {cite}`Anagnostou_2022}`. Regardless of the way the split is calculated, sharing of health DES models does not match the findings from Agent Based Simulation where 18% of studies shared models in 2018 {cite}`janssen2020code`. It appears that four years later DES models in health are shared far less often than ABS models in general. 

Of the 47 models shared the majority were implemented using a FOSS simulation tool such as R Simmer. This is perhaps not surprising given the freedom FOSS licenses grant authors and other researchers or health care services that may opt to reuse the work.  

We also found that only a minority (~25%) of models aiming to support health services to care for patients during the Covid-19 pandemic were shared. It would appear that healthcare DES fell short of the sharing standard other fields had called for during the pandemic {cite}`covid19_transparency`. One positive is that Covid-19 models were shared more often than computer models in general healthcare settings.

Over 65% (31 out of 47) of the DES models shared via a publication were developed using a code based simulation package. Sharing was most often done by GitHub. Open science researchers have stated elsewhere {cite}`janssen2020code, krafczyk_learning_2020, heil_reproducibility_2021` that the gold standard for an open science archive can mint a DOI and provide long term storage guarantees.  Disadvantages of GitHub (and other cloud based version control tools) is that there are no guarantees on how long code will remain stored, and it is unclear which version of the code was used in a publication. We only found two instances of code being managed on both GitHub/Lab and deposited in an open science archive. Models built in commercial VIM software were shared less often (16 out 47 models). The majority of these were attached to journal supplementary material or via AnyLogic Cloud. The latter of these approaches will likely lead to broken links in the future due to changes in commercially provided infrastructure and licensing.

Although FOSS simulation packages made up the majority of the shared/archived models we identified it is still commercial off the shelf simulation packages that dominate the academic literature overall.  We confirmed a prior result {cite}`vazquez-serrano_discrete-event_2021` that Arena was the most used package in healthcare DES, with AnyLogic and Simul8 also being in regular use.  Definitively explaining why model sharing is most associated with FOSS packages is not possible at this time.  We can confirm this is not related to effort needed to perform basic archiving. If we take a digital open science repository such as Zenodo, we note there is no additional work to archive a model file built in a commercial package to one coded in Python.  Our speculations are that this is i.) related the general philosophy of freedom built into FOSS tools. That is, FOSS tools attract certain types of users and these users are more likely to share their model artifacts. ii.) FOSS tools are more likely to be code based (although not exclusively) and that lends itself to managing code via repositories such as GitHub.

Keeping to the topic of simulation software, we found that 11% of studies failed to report what simulation software was used at all.  This result was also observed by {cite}`vazquez-serrano_discrete-event_2021` and by {cite}`brailsford_hybrid_2019` in their exhaustive review of hybrid simulation models.  Our result is somewhat more striking than these previous reviews as we focused our review post publication of the Strengthening the Reporting of Empirical Simulation Studies that recommends authors report software used.  An explanation is that our review found that the uptake of reporting guidelines within healthcare DES was low. Cost-effectiveness studies modelling individual patient trajectories using DES were the most likely to include some mention or cite using reporting guidelines, typically one of the ISPOR publications. 


## Summary of best practice audit results

The quality audit revealed that the tools and methods of sharing DES models could be greatly improved within health and medicine. 

### Open scholarship

We found that very few models were deposited in an open science repository such as Zenodo, OSF or even an academic institution. This meant that these model artifacts had no guarantees of long term storage and could not be easily cited. In the case of FOSS or code based models, authors primarily opted for linking to code version control repository such as GitHub or GitLab.  While this allowed authors to share their code it is possible that these peer reviewed links will be invalid in future years. We also found instances where model binary files used within commercial simulation software such as Anylogic were inappropriately committed to GitHub instead of an open science repository.

Similarly, the review found limited use of ORCIDs in repositories, archives, or platforms that shared DES models.  This meant there was no robust way for the models artifacts to be linked to a researcher and their portfolios.

The majority of DES models were shared without an open license.  If we split the models into code based and VIM based simulation software we found that VIM models were the least likely to include a clear open license.  The VIM models that did have an open license were typically journal supplementary material and by default adopted the license applied to the journal article as a whole. Without a license authors retain exclusive copyright to their research artifacts.  This means that other researchers and potential users can view the code/model, but not reuse it or adapt it.  

### Tools to facilitate reuse of models

In general, we found that only a minority of DES models are stored with any form of clear instruction to run the model.  This was less likely for VIM models (20\%) than code based models (40\%). As we did not have licensed copies of all the commercial software used it is possible that instructions were contained within the models themselves.  If this is indeed the case the authors did not describe this within papers or repositories.

Dependency management was in general of a poor quality or not used at all.  Only 23\% of code based simulation models had any formal dependency management; while VIM based models fared slightly better informally by stating the version of the software used. This latter result is perhaps due to the simplicity of stating which version of the commercial 'of the shelf' DES software you are using versus a complex software environment for code based DES model. Although we note that in many cases authors did not even state the version of R or Python they were using.

Surprisingly, we found that several of the VIM based DES models shared were not downloadable - even when an author stated it could be downloaded. These were all hosted on cloud based services where the model was interactive and executable to some extent.  We found that some models shared through the same platforms were downloadable, so a plausible explanation is that that this was just a setting that was missed by study authors.

Although testing and model verification is standard practice and covered by many simulation text books, we found very little evidence of model testing both of models written in a coding language and commercial software. Given the other findings, it is not surprising that there was limited evidence of testing among the shared models, although this does not mean that testing activities did not take place. An explanation could be that model testing had been completed informally and incrementally as models were coded.

## References

```{bibliography}
:filter: docname in docnames
```