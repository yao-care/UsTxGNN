---
layout: default
title: Miltefosine
parent: Moderate Evidence (L3-L4)
nav_order: 931
evidence_level: L4
indication_count: 4
---

# Miltefosine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Miltefosine: From Antileishmanial Use to Diffuse Cutaneous Leishmaniasis

## One-Sentence Summary

Miltefosine is an oral alkylphosphocholine antileishmanial drug, marketed in the US as IMPAVIDO capsules. The TxGNN model predicts it may be effective for **diffuse cutaneous leishmaniasis (DCL)**. No clinical trials are registered for this indication, but there are **20 publications**, mostly case reports and reviews, and several of the case reports describe a response followed by relapse.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data (the drug is an antileishmanial, so this may be a rediscovery of an existing use; verify against the label) |
| Predicted New Indication | Leishmaniasis, diffuse cutaneous |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold (research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank. Miltefosine is an alkylphosphocholine antileishmanial. It is thought to disrupt parasite membrane lipid metabolism and signaling and to induce apoptosis-like parasite death.

The very high TxGNN score likely reflects a known drug–*Leishmania* link in the knowledge graph. Because the original-indication field is empty, this prediction may be a rediscovery of an existing leishmaniasis use rather than true repurposing. That should be checked against the US label.

DCL is a rare, chronic form of cutaneous leishmaniasis with a heavy parasite burden and weak cell-mediated immunity. It has no established effective treatment. Miltefosine's oral route and its activity in visceral leishmaniasis make it a plausible candidate. Direct DCL evidence is limited to a handful of case reports and one susceptibility study, described below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32853410](https://pubmed.ncbi.nlm.nih.gov/32853410/) | 2020 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Interventions for American cutaneous and mucocutaneous leishmaniasis. Antimonials remain first choice and alternatives are limited. Not DCL-specific. |
| [26938448](https://pubmed.ncbi.nlm.nih.gov/26938448/) | 2016 | Systematic review | PLoS Negl Trop Dis | Treatment of *L. aethiopica* cutaneous leishmaniasis, including severe forms such as DCL. Evidence-based guidelines are lacking. |
| [34048461](https://pubmed.ncbi.nlm.nih.gov/34048461/) | 2021 | Pilot study | PLoS Negl Trop Dis | Miltefosine for cutaneous leishmaniasis in Ethiopia (*L. aethiopica*). Not DCL-specific. |
| [28712122](https://pubmed.ncbi.nlm.nih.gov/28712122/) | 2017 | Cohort/observational | Trop Med Int Health | Clinical features and treatment outcomes of cutaneous leishmaniasis in North-West Ethiopia. Not DCL-specific. |
| [41666471](https://pubmed.ncbi.nlm.nih.gov/41666471/) | 2026 | Case report | Am J Trop Med Hyg | A patient with DCL (*L. amazonensis*), with over 60 prior regimens across 22 years, had complete remission after 180 days of miltefosine. |
| [17441955](https://pubmed.ncbi.nlm.nih.gov/17441955/) | 2007 | Case report | Br J Dermatol | DCL responded to miltefosine but then relapsed. |
| [16796642](https://pubmed.ncbi.nlm.nih.gov/16796642/) | 2006 | Case report | Int J Dermatol | A 31-year-old man with DCL since age 3 was treated with miltefosine. |
| [17172368](https://pubmed.ncbi.nlm.nih.gov/17172368/) | 2006 | Case report | Am J Trop Med Hyg | *L. mexicana* DCL cleared after 4 months of miltefosine, but lesions and parasites returned 2 months after stopping. |
| [25033218](https://pubmed.ncbi.nlm.nih.gov/25033218/) | 2014 | In vitro/in vivo study | PLoS Negl Trop Dis | Miltefosine susceptibility of an *L. amazonensis* isolate from a DCL patient. |
| [33611800](https://pubmed.ncbi.nlm.nih.gov/33611800/) | 2021 | Case report + review | J Cutan Pathol | DCL with HIV co-infection. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204684 | IMPAVIDO (Profounda, Inc.) | Capsule (oral) | Not listed in the supplied data |

---

## Safety Considerations

The evaluation noted these guardrails:
- **Teratogenicity**: contraception is required.
- **GI toxicity**.
- **Relapse or resistance monitoring**: several DCL case reports show relapse after treatment.
- **HIV co-infection** needs special attention.

Drug interaction records were not found. Please refer to the package insert for warnings, contraindications and interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for DCL is limited to case reports and one susceptibility study. There are no trials, and relapse after an initial response is repeatedly reported. The package insert safety data is also missing, which blocks progression to safety screening (S1).

The other three predictions have no supporting evidence and should also stay on Hold (L5, model prediction only):
- *Echinococcus granulosus* infection: no literature.
- Alveolar echinococcosis: the one paper supplied tests other drugs, not miltefosine.
- Smouldering systemic mastocytosis: no literature.

**To proceed, the following is needed:**
- Download and parse the FDA package insert for warnings, contraindications and approved indications, to confirm whether DCL falls within the existing label.
- Obtain mechanism of action data from DrugBank.
- Review DCL-specific evidence, including treatment duration, relapse rates and combination regimens.
- Establish a monitoring plan for relapse and resistance, contraception, and HIV co-infected patients.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

