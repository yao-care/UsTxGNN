---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 984
evidence_level: L5
indication_count: 10
---

# Ofloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ofloxacin: From Antibacterial Use to Hyperamylasemia

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibacterial (DNA gyrase/topoisomerase IV inhibitor) that is marketed in the US in oral, ophthalmic and otic forms.
The TxGNN model's top-ranked prediction is **hyperamylasemia** (score 99.91%), but there are **0 clinical trials** and **0 publications** behind it, and no plausible mechanism, so it is most likely a knowledge-graph artifact.
Two lower-ranked predictions, **septicemic plague** and **monoclonal gammopathy**, have literature support and are covered below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the license data (ofloxacin is a fluoroquinolone antibacterial) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed are ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Ofloxacin is known to inhibit bacterial DNA gyrase and topoisomerase IV, which is why it kills bacteria.

This mechanism has no known effect on serum amylase, so the link between the original antibacterial use and hyperamylasemia is not supported. The very high score alongside zero trials and zero literature suggests a knowledge-graph artifact. The prediction should not be treated as a real repurposing signal.

Among the other top-10 predictions, two have a more credible basis:

- **Septicemic plague (rank 8):** Ofloxacin is active against *Yersinia pestis*, and this is an extension within the antibacterial class rather than a novel repurposing.
- **Monoclonal gammopathy (rank 6):** The evidence concerns infection prophylaxis in myeloma with levofloxacin (the L-isomer of ofloxacin), not treatment of the gammopathy itself.

The remaining predictions (polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant hematological disease, hematological disease with peripheral neuropathy, congenital hematological disorder, punctate epithelial keratoconjunctivitis) have no mechanistic rationale or only irrelevant literature. Fluoroquinolones are themselves associated with peripheral neuropathy, which argues against the rank 7 prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia. None are registered for any of the other top-10 predictions either.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

For reference, the best-supported lower-ranked predictions (all indirect, mostly other fluoroquinolones or animal data):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/) | 2019 | RCT (Phase 3) | Lancet Oncol | Monoclonal gammopathy/myeloma: TEAMM, double-blind placebo-controlled trial of levofloxacin infection prophylaxis in newly diagnosed myeloma |
| [31690402](https://pubmed.ncbi.nlm.nih.gov/31690402/) | 2019 | RCT report | Health Technol Assess | Monoclonal gammopathy/myeloma: full TEAMM report on levofloxacin prophylaxis and health-care-associated infections |
| [32172361](https://pubmed.ncbi.nlm.nih.gov/32172361/) | 2020 | Review | Curr Hematol Malig Rep | Monoclonal gammopathy/myeloma: supportive care principles in myeloma, including infection management |
| [37573150](https://pubmed.ncbi.nlm.nih.gov/37573150/) | 2023 | Cohort | Transpl Infect Dis | Monoclonal gammopathy/myeloma: infectious complications after autologous transplant, with or without levofloxacin prophylaxis |
| [32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/) | 2020 | Review | Clin Infect Dis | Septicemic plague: African green monkey model and FDA approval of antimicrobials under the Animal Rule |
| [32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/) | 2020 | Animal study | Clin Infect Dis | Septicemic plague: effect of delayed treatment on ciprofloxacin and levofloxacin efficacy in pneumonic plague |
| [21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/) | 2011 | Animal study | PLoS Negl Trop Dis | Septicemic plague: levofloxacin tested for pneumonic plague in a nonhuman primate model |
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Animal study | Antibiot Khimioter | Septicemic plague: ofloxacin prophylaxis and treatment in experimental plague in mice |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal study | Antimicrob Agents Chemother | Septicemic plague: ofloxacin among antibiotics active in a murine *Y. pestis* infection model |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | Antimicrob Agents Chemother | Septicemic plague: ofloxacin among the most active agents against 78 *Y. pestis* strains |

---

## US Market Information

The license records do not include approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076622 | Ofloxacin | Solution/drops | A-S Medication Solutions |
| ANDA217904 | Ofloxacin | Solution | Leading Pharma, LLC |
| ANDA091656 | Ofloxacin | Tablet, coated (oral) | Nivagen Pharmaceuticals, Inc. |
| ANDA091656 | Ofloxacin | Tablet, film coated (oral) | Modavar Pharmaceuticals LLC |
| ANDA076527 | Ofloxacin Otic | Solution | Bryant Ranch Prepack |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hyperamylasemia, has no mechanistic link, no trials and no literature, so the high TxGNN score is best treated as a knowledge-graph artifact. Septicemic plague (class-level, preclinical) and monoclonal gammopathy (indirect, levofloxacin-based) are the only predictions worth further review, both at the "Research Question" stage.

**To proceed, the following is needed:**
- The US package insert (warnings and contraindications), which is currently a blocking data gap for safety screening
- Detailed mechanism-of-action data from DrugBank
- For plague: human or Animal Rule-type evidence specific to ofloxacin, since the regulatory precedent is for levofloxacin and ciprofloxacin
- For monoclonal gammopathy: evidence in MGUS specifically, and an ofloxacin-specific study rather than extrapolation from levofloxacin
- Route-compatibility and similarity-to-original-indication assessments, which are still pending

*For research reference only. Not medical advice. Predictions require clinical validation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

