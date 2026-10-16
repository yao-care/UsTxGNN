---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 547
evidence_level: L5
indication_count: 3
monitor_inn: "COLCHICINE"
predicted_indications: ["Plasmodium falciparum malaria", "familial Mediterranean fever, autosomal dominant", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Colchicine: From Gout and Familial Mediterranean Fever to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine was originally used to treat gout and familial Mediterranean fever (FMF).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**,
but there are currently **0 clinical trials** and only **2 preclinical publications** supporting this direction, so the prediction rests mainly on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; familial Mediterranean fever (the US license records contain no indication text) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 11 authorizations in total (all cancelled; 2 NDAs and 9 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, colchicine is a microtubule-disrupting agent that binds tubulin. Its efficacy in gout and FMF is established, and mechanistically parasite tubulin could be a plausible target in malaria.

The two retrieved papers only offer indirect support. One studied microtubule disruption in *P. falciparum* (a curcumin study, in which colchicine is likely a comparator). The other showed that expression of the parasite *pfmdr1* gene in mammalian cells changes drug susceptibility. Neither shows that colchicine works against malaria.

Selectivity is the main concern. Colchicine has a narrow therapeutic index, and the doses needed for antiparasitic activity would probably cause host toxicity. This prediction should be treated as a hypothesis only.

**Other predicted indications (for reference):**
- **Familial Mediterranean fever, autosomal dominant** (score 99.38%, evidence level L4, Hold): this is essentially a subtype extension of an existing indication rather than true repurposing. The retrieved literature consists mainly of narrative reviews, and no trials are registered.
- **Dermatofibrosarcoma protuberans** (score 99.37%, evidence level L5, Hold): no trials or literature were found. Only a speculative antimitotic link exists, and the disease is driven by the COL1A1-PDGFB fusion and treated with surgery and imatinib.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro/Preclinical | PloS one | Curcumin disrupts microtubules in *P. falciparum*; relevant to parasite microtubules as a target, not direct evidence for colchicine |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro/Preclinical | Molecular and cellular biology | Expression of the plasmodial pfmdr1 gene in mammalian cells increased susceptibility to chloroquine; relates to drug transport and resistance |

---

## US Market Information

All 11 authorizations are cancelled and none lists approved indication text. The five main ones are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204820 | Colchicine (Hikma Pharmaceuticals USA Inc.) | Capsule | Not recorded; cancelled |
| NDA022352 | Colchicine (Bryant Ranch Prepack) | Film-coated tablet | Not recorded; cancelled |
| ANDA209470 | Colchicine (Mylan Pharmaceuticals Inc.) | Film-coated tablet | Not recorded; cancelled |
| ANDA217620 | Colchicine (Camber Pharmaceuticals, Inc.) | Capsule | Not recorded; cancelled |
| ANDA208678 | Colchicine (Endo USA, Inc.) | Capsule | Not recorded; cancelled |

---

## Cytotoxicity

Colchicine is not classified as an antineoplastic drug, but it is an antimitotic agent with a narrow therapeutic index. Please refer to the package insert warnings and precautions for handling and monitoring guidance.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. The knowledge graph does, however, list the following disease contraindications (these are not label text):

- **Blood disorders:** hematologic disease, thrombocytopenia, leukopenia, agranulocytosis, neutropenia (including congenital and idiopathic forms), aplastic anemia
- **Muscle disorders:** myopathy, muscular disease, rhabdomyolysis, familial periodic paralysis
- **Gastrointestinal:** peptic ulcer disease, diarrheal disease
- **Liver and kidney:** liver failure, impaired renal function, acute urate nephropathy

**Drug Interactions:** 100 interactions were found; the first 20 returned are summarized here, and several are Major.
- **Major:** aprepitant, clarithromycin, cobicistat, deferiprone, eliglustat, rolapitant, rosuvastatin, simvastatin
- **Moderate:** metronidazole, cimetidine, eluxadoline, miconazole, tinidazole, deferasirox, strontium chloride Sr-89, fostamatinib, ticagrelor, chloroquine, benznidazole, disulfiram

Chloroquine is a standard antimalarial, so a possible interaction with colchicine is directly relevant to the malaria indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The malaria prediction has a high model score but no clinical trials and only two indirect preclinical papers (evidence level L5). Colchicine's narrow therapeutic index makes selective antiparasitic activity doubtful. Every US authorization is also cancelled.

**To proceed, the following is needed:**
- In vitro activity data of colchicine against *P. falciparum* (potency and selectivity index compared with host cells)
- Evidence that parasite-effective concentrations can be reached safely in humans
- Mechanism of action data and the full package insert warnings and contraindications
- Review of the interaction with chloroquine and other antimalarials
- A fresh regulatory pathway assessment, since no US authorization is currently valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

