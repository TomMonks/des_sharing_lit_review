# Data Extraction

Where possible we always viewed papers at the publishers' site so we could identify, download, and access any supplementary material or information that may not be directly included in the article PDF. If an article built on and cited previously published work/models we followed up the paper in attempt to complete data extraction. Any uncertainty was managed by dual review and an additional proportion of papers were reviewed by both authors. \cite{janssen2020code} handled "model code is available upon request" by emailing authors directly. Given the low response rate found in their study ($<$ 1\%) we chose not to follow up in this study.

We extracted the following data from each article:  

* Type of article: journal, conference (e.g. Winter Simulation Conference), or book.  
* Name of reporting guidelines used (if present)  
* Name of simulation software  
* If the software was commercially or FOSS licenced
* Methods of sharing (see below)
* Licence for shared model (if present) 
* Papers modelling Covid applications

Models or code can be shared as an appendix of a journal article, an author's personal or institutional webpage, a GitHub repository, or a digital repository. Sharing code on a personal or university website or within journal supplementary material is not a good long-term solution. Model code is best documented and archived in a citable, trusted digital repository; it should receive a permanent identifier e.g. a Digital Object Identifier (DOI) and should be used as a software citation in papers. This permanent identifier should resolve to a durable web landing page with descriptive metadata and links to files corresponding to the exact version of the model used in the paper. Publishing and referencing code in a GitHub repository does not make clear which version of the code in the repository was actually used for the publication, does not provide any guarantees of permanence, and can be deleted by the owner at any time. 

We adopt the sharing classification used by Janssen (2020): 

* Archive (Zenodo, Figshare, Open science framework (OSF), Dataverse, Datadryd, CoMSES, university archives, etc); 
* Repository (Github/Lab/Bitbucket, Sourceforge, Google code, etc.); 
* Journal supplementary material, personal and organisational (own website, Dropbox, Researchgate, Google Drive, Amazon Cloudfront. etc.); 
* Platform (e.g. vendor website - e.g. Simul8 Cloud, Simio Cloud, Anylogic Cloud etc. This might also include free infrastructure to support FOSS, e.g. StreamLit.io, RShiny.io, Binder or hybrid free/paid infrastructure like Code Ocean).
  