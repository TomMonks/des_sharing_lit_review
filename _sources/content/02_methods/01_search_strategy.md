# Search Strategy

The databases Scopus and PubMed Central were searched to retrieve articles on DES applications in healthcare from 2019 to 2022. Scopus has previously demonstrated wide coverage for systematic reviews of modelling and simulation in multiple domains, including healthcare. We searched PubMed using general terms rather than MeSH Terms, which have been found to produce large numbers of irrelevant results for operations research and operations management papers. The PubMed search allowed inclusion of healthcare simulation applications published in healthcare journals. 

The key search terms included: “health” or “healthcare”, and “discrete”, “event”, and “simulation”, in the title, abstract, and/or keywords. Search years were limited to 2019-2022, and Scopus terms were limited to articles, excluding letters, notes, editorials, conference reviews, short surveys, data papers, and erratums. 
We limited our search years to allow time for the March, 2018 publication of the STRESS guidelines to take effect. STRESS includes the requirement to include a code access statement (Section 6).  This also follows publication of an Open Science checklist , and the February, 2019 release of \emph{The Turing Way}, a guide to reproducible research published by the UK's National Institute for Data Science. 

## Scopus search string

Scopus search strategy for Covid-19 simulation models 2020/22.  In the following search string we replaced `XX` with 19-22 to vary the year of search. 

```
TITLE-ABS-KEY ( ( health  AND  discrete  AND  event  AND  simulation )  OR  ( healthcare  AND  discrete  AND  event  AND  simulation ) )  AND  ( LIMIT-TO ( PUBSTAGE ,  "final" ) )  AND  ( EXCLUDE ( DOCTYPE ,  "le" )  OR  EXCLUDE ( DOCTYPE ,  "no" )  OR  EXCLUDE ( DOCTYPE ,  "cr" )  OR  EXCLUDE ( DOCTYPE ,  "ed" )  OR  EXCLUDE ( DOCTYPE ,  "sh" )  OR  EXCLUDE ( DOCTYPE ,  "dp" )  OR  EXCLUDE ( DOCTYPE ,  "er" ) )  AND  ( LIMIT-TO ( PUBYEAR ,  20XX ) )
```


## Pubmed search string

The pubmed search string was as follows:

```
 (((discrete[Title/Abstract]) AND (event[Title/Abstract])) AND (simulation[Title/Abstract])) AND (("2019"[Date - Publication] : "2022"[Date - Publication]))
```