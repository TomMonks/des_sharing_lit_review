# Quality Audit


We split our assessment of the quality of how models were shared into two groups: models developed using using a coding language or framework (e.g. MatLab, R, or Python based) and models developed in commercial off the shelf Visual Interactive Modelling software (VIM; e.g. Arena, Anylogic, or Simio).  

We know of no general quality auditing tools for sharing of code and models. However, general guidance for open science and reproducible research is available from the Turing Way {cite}`the_turing_way_community_2022_7470333` developed by The Alan Turing Institute: the UK's official institute for data science and AI. We reviewed the Turing Way checklists for Open Research, Licensing, Reproducible Environments, and Code Testing and selected relevant quality criteria.  We enhanced this list by adapting the high level open scholarship recommendations for modelling and simulation from {cite:p}`taylor2017open`.

We excluded some Turing checklists from our review as they were not relevant to the quality of model sharing.  For example, the Research Data Management checklist is focussed on raw data that in a typical DES study would have used to derive model parameters.  Our focus is on the sharing of the model itself and not underlying raw data. Another example is the Turing's recommendations to publish open notebooks containing all details of experiments. This was on the basis that the modelling and simulation community might adopt a large number of approaches and tools to managing their models and artefacts. Instead we included a broader item checking for instructions to execute experiments in any format.

The metrics within our audit also overlap with what others have listed as requirements for reproducibility of computational studies {cite}`venkatesh_code_2022`.  We list these in Table {ref}`quality-criteria`, to illustrate which data were extracted for the coding and VIM groups, and detail the provenance of the items.

```{table} Quality Audit: Metrics and Sources.
:name: quality-criteria
| Item                               | Description                                                                                                        | Code<sup>a</sup> | VIM<sup>b</sup> | Source(s)                                                                             |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------|------------------|-----------------|---------------------------------------------------------------------------------------|
| Digital Object Identifier          | Does the model have a DOI and promise of persistence? Can it be cited?                                             | y                | y               | Section 6. item 3. Taylor et al (2017)  Turing Way: Open Research Checklist item 4    |
| Open Researcher and Contributor ID | Is the model linked to one or more of the authors via an ORCID?                                                    | y                | y               | Section 6. item 5.  Taylor et al (2017)                                               |
| Licence                            | Does the repository have a recognised open license to control the use of code, liabilty and credit?                | y                | y               | Section 6. item 4. Taylor et al (2017); Turing Way: Licensing Checklist items 1 and 2 |
| Readme file                        | Is there an obvious file that provides an overview of the repository/model and it purpose?                         | y                | y               | Turing Way: Open Research Checklist item 8                                            |
| Link to published paper            | Do models shared externally from journal articles contain a link to the published article?                         | y                | y               | Turing Way: Open Research Checklist item 12                                           |
| Steps to run code                  | Does the readme file or similar describe the steps required to execute the simulation model?                       | y                | y               | Adapted from Turing Way Open Notebooks Checklist                                      |
| Formal dependency management       | Has a formal tool, e.g. renv, conda, or poetry been used to manage software dependencies for the simulation model? | y                | n               | Turing Way: Reproducible Environment Checklist items 1-3                              |
| Informal dependency management     | Has an informal list or description of software, or OS dependencies been provided?                                 | y                | y               | Turing Way: Reproducible Environment Checklist items 1-3                              |
| Code Testing                       | Is there any evidence of tests that have been applied to the code to check that it functions correctly?            | y                | n               | Turing Way: Code Testing Checklist item 1                                             |
| Local execution                    | Can the simulation model and associated files be downloaded and in theory executed on a local machine              | y                | y               | Turing Way: Open Research Checklist item 5                                            |
| Remote execution                   | Can the simulation model be executed online using free or commercial infrastructure?                               | y                | y               | Section 6. item 7. Taylor et al (2017)                                                |
```

## Turing Way - links to checklists.

* [Open Research Checklist](https://the-turing-way.netlify.app/reproducible-research/open/open-checklist.html)
* [Licensing checklist](https://the-turing-way.netlify.app/reproducible-research/licensing/licensing-checklist.html)
* [Reproducible environment checklist](https://the-turing-way.netlify.app/reproducible-research/renv/renv-resources.html)
* [Code Testing checklist](https://the-turing-way.netlify.app/reproducible-research/testing/testing-checklist.html)


## References

```{bibliography}
:filter: docname in docnames
```