---
layout: default
title: Floxuridine
parent: Model Prediction Only (L5)
nav_order: 712
evidence_level: L5
indication_count: 10
monitor_inn: "FLOXURIDINE"
predicted_indications: ["hereditary breast ovarian cancer syndrome", "neutrophil immunodeficiency syndrome", "myeloid leukemia", "CMM7", "pediatric leptomeningeal melanoma", "melanoma", "epithelioid cell uveal melanoma", "ovarian clear cell adenocarcinoma", "central nervous system melanocytic neoplasm", "female breast carcinoma"]
last_modified_at: 2026-10-14
description: "Floxuridine: predicted new indication Hereditary breast ovarian cancer syndrome (evidence level L5). Approved use: Liver cancer / hepatocellular carcinoma"
---

# Floxuridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Floxuridine: From Liver Cancer to Hereditary Breast Ovarian Cancer Syndrome
{: .text-alpha }

## One-Sentence Summary

Floxuridine is a fluoropyrimidine nucleoside analog, originally used for liver cancer (including hepatocellular carcinoma).
The TxGNN model's top-ranked prediction is **Hereditary Breast Ovarian Cancer Syndrome**, but **no clinical trials and no publications** support this specific prediction.
Among the other predictions, the best-supported are **female breast carcinoma** (13 publications, mostly regional liver-directed therapy or preclinical work) and **melanoma** (5 publications, mostly indirect).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Liver cancer / hepatocellular carcinoma (from the knowledge graph; no approved-indication text is available on the US licenses) |
| Predicted New Indication | Hereditary breast ovarian cancer syndrome (rank 1) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no active marketing authorization) |
| Number of NDAs | 2 (both ANDAs, both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the data compiled for this report. Based on the repurposing analysis, floxuridine is a fluoropyrimidine nucleoside analog whose active metabolite, FdUMP, inhibits thymidylate synthase and disrupts DNA synthesis in rapidly dividing cells.

For the top-ranked prediction, the rationale is weak. Hereditary breast ovarian cancer syndrome is a germline predisposition (BRCA-related DNA repair deficiency), not a treatable tumor type. Floxuridine has no known link to that deficiency. The high score most likely reflects the drug's proximity to breast and ovarian cancer in the knowledge graph.

Other predictions have more plausible links, although none is strongly supported:

- **Female breast carcinoma (rank 10):** Fluoropyrimidines are an established class in breast cancer. The clinical signal is limited to breast cancer liver metastases treated with hepatic arterial infusion, which builds on floxuridine's original liver-directed use.
- **Melanoma (rank 6) and uveal melanoma (rank 7):** Uveal melanoma metastasizes preferentially to the liver, so liver-directed floxuridine is a conceivable hypothesis. The evidence is regional, retrospective and indirect, and does not support systemic use in cutaneous melanoma.
- **Myeloid leukemia (rank 3):** Antimetabolite activity is plausible, but the two retrieved papers are indirect.
- **Neutrophil immunodeficiency syndrome (rank 2):** Biologically implausible, because floxuridine causes myelosuppression, including neutropenia, and could worsen the condition.
- **Other melanoma subtypes, CNS melanocytic neoplasm and ovarian clear cell adenocarcinoma (ranks 4, 5, 8, 9):** Prediction only. CNS delivery is a concern, and ovarian clear cell adenocarcinoma is typically chemoresistant.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication, hereditary breast ovarian cancer syndrome. No registered trials were retrieved for any of the other ten predicted indications either.

## Literature Evidence

No literature is available for the top-ranked prediction. The table below shows the most relevant publications for the best-supported prediction, **female breast carcinoma** (rank 10), ordered by study design.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23173748](https://pubmed.ncbi.nlm.nih.gov/23173748/) | 2013 | Cohort | Breast J | Nine heavily pretreated patients with breast cancer liver metastases received hepatic arterial infusion of floxuridine/dexamethasone plus systemic chemotherapy; 7 (78%) had objective responses, and 4 had grade 3 liver enzyme elevations |
| [34657511](https://pubmed.ncbi.nlm.nih.gov/34657511/) | 2021 | Cohort | Technol Cancer Res Treat | Hepatic arterial infusion combined with systemic chemotherapy in 19 patients with breast carcinoma liver metastases (2012–2019); efficacy and safety evaluated |
| [1838261](https://pubmed.ncbi.nlm.nih.gov/1838261/) | 1991 | Phase I/II | Eur J Cancer | Floxuridine plus etoposide plus cisplatin infusion in 36 patients with advanced malignancy; dose-limiting toxicity was stomatitis and diarrhoea, associated with leukopenia and thrombocytopenia |
| [24169176](https://pubmed.ncbi.nlm.nih.gov/24169176/) | 2014 | Cohort | Ann Surg | Decade-long single-institution experience of isolated hepatic perfusion for unresectable liver metastases (indirect; not specific to breast cancer) |
| [20048179](https://pubmed.ncbi.nlm.nih.gov/20048179/) | 2010 | Phase II | J Clin Oncol | Systemic oxaliplatin/capecitabine alternating with hepatic arterial infusion of floxuridine after resection of colorectal liver metastases (indirect; colorectal) |
| [10550572](https://pubmed.ncbi.nlm.nih.gov/10550572/) | 1999 | Clinical study | Cancer Chemother Pharmacol | Scintigraphic and pharmacokinetic approach to predict systemic toxicity of hepatic arterial floxuridine infusion in liver metastases |
| [6230054](https://pubmed.ncbi.nlm.nih.gov/6230054/) | 1984 | Phase I | Gan To Kagaku Ryoho | Phase I study of a floxuridine derivative (FF-705) in solid tumors; transient liver enzyme rises and gastrointestinal effects noted |
| [4287261](https://pubmed.ncbi.nlm.nih.gov/4287261/) | 1966 | Historical report | JAMA | Early report on floxuridine infusion for solid tumors |
| [39388598](https://pubmed.ncbi.nlm.nih.gov/39388598/) | 2024 | Preclinical | Mol Pharm | RNA nanostructures co-delivering floxuridine and gemcitabine with synergistic effect |
| [21863885](https://pubmed.ncbi.nlm.nih.gov/21863885/) | 2011 | Preclinical | Bioconjug Chem | Polymeric conjugates of activated nucleoside analogues to overcome drug resistance |

For **melanoma** (rank 6), the main literature consists of a review of isolated hepatic perfusion (PMID 12004803), a retrospective cohort of isolated hepatic perfusion for liver metastases (PMID 24169176), and preclinical work on a floxuridine silica nanoparticle prodrug (PMID 40259607). For **myeloid leukemia** (rank 3), the retrieved papers are indirect: a floxuridine-containing regimen in gestational trophoblastic neoplasia (PMID 34396643) and a review of liposomal drug co-encapsulation (PMID 29692263).

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075387 (Cancelled) | Floxuridine (Hikma Pharmaceuticals USA Inc.) | Injection, powder, lyophilized, for solution | Not listed |
| ANDA075837 (Cancelled) | Floxuridine (Fresenius Kabi USA, LLC) | Injection, powder, lyophilized, for solution | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium to high. Leukopenia and thrombocytopenia accompanied severe gastrointestinal toxicity in the published combination study (PMID 1838261) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function (liver enzyme elevations were reported with hepatic arterial infusion), renal function, and gastrointestinal toxicity (stomatitis, diarrhoea) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** kidney disease, liver disease, gallbladder disease and cholecystitis, bile duct fibrosis, thrombocytopenia, anemia (including macrocytic anemia), leukopenia, hyperbilirubinemia (including Gilbert syndrome), active peptic ulcer disease, myocardial ischemia and coronary artery disease, and mucosal or upper gastrointestinal conditions (pharyngitis, stomatitis, esophagitis, gastroesophageal reflux disease).
- **Drug Interactions:** 100 interactions were identified. Examples of **Major** interactions include deferiprone, samarium (153Sm) lexidronam, adalimumab and baricitinib. **Moderate** interactions include mercaptopurine, zidovudine, chloramphenicol, azathioprine, bendamustine, aldesleukin, alemtuzumab, anakinra, palifermin, roflumilast, strontium chloride Sr-89, and several vaccines. The only **Minor** example is levofloxacin. Many of these involve additive myelosuppression or immunosuppression.
- **Additional concern:** Pediatric and CNS-directed indications (pediatric leptomeningeal melanoma, CNS melanocytic neoplasm) raise extra safety and delivery concerns.

Package insert warnings and contraindications were not available for this report; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hereditary breast ovarian cancer syndrome, has no trials or literature and no plausible mechanism, since it is a germline predisposition rather than a treatable tumor. Both US ANDAs are cancelled. The best-supported alternatives (breast cancer liver metastases and melanoma liver-directed therapy) rest on small retrospective series and preclinical work. They are better framed as research questions than as repurposing candidates.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block safety screening
- Mechanism of action data from DrugBank
- Reframing the question toward liver-directed use in breast cancer or uveal melanoma liver metastases, with a systematic review of hepatic arterial infusion evidence
- Confirmation of the current availability of floxuridine in the US, since both ANDAs are cancelled
- A route and formulation assessment, since hepatic arterial infusion requires specialised delivery and the route compatibility analysis is still pending
- A monitoring plan for myelosuppression, hepatobiliary toxicity and gastrointestinal toxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

