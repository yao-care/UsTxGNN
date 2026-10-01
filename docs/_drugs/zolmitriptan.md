---
layout: default
title: Zolmitriptan
parent: Moderate Evidence (L3-L4)
nav_order: 1311
evidence_level: L4
indication_count: 3
---

# Zolmitriptan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Zolmitriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Zolmitriptan is a 5-HT1B/1D receptor agonist (triptan) marketed in the US for the acute treatment of migraine.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but this is a model prediction with **0 registered clinical trials** and **19 publications**, none of which studies brainstem aura patients.
The high score most likely reflects the drug's existing migraine association in the knowledge graph rather than new repurposing evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute migraine with or without aura (inferred from the literature; license indication text is not provided) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured mechanism-of-action field is not available for this drug. The literature describes zolmitriptan as a selective 5-HT1B/1D receptor agonist. Preclinical work shows it combines partial agonist activity with the ability to inhibit trigeminovascular activation both centrally and peripherally (PMID 9399012, PMID 12083998). Its efficacy in acute migraine is established in randomised, placebo-controlled trials.

Migraine with brainstem aura is a migraine subtype (historically called basilar migraine), so a biological link to the original indication is plausible. The model's score likely comes from this close relationship to migraine in general.

The evidence does not yet support applying the mechanism to this subtype:
- None of the 19 retrieved articles studies brainstem aura patients. They are general migraine or triptan reviews, guidelines, and tolerability or effectiveness studies.
- Triptans have traditionally been used cautiously in this subtype because of vasoconstriction concerns in patients with brainstem or basilar symptoms.
- The two other predictions (atrophoderma vermiculata and ulerythema ophryogenesis) have no trials, no literature, and no plausible mechanistic link. They are rated L5 and Hold and are likely knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Clinical report | Headache | Reports on triptan use in basilar migraine and migraine with prolonged aura. This is the most directly relevant article. The abstract excerpt gives no outcome data. |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT (subgroup analysis) | Neurol Sci | Frovatriptan 2.5 mg vs zolmitriptan 2.5 mg in 18 patients with migraine with aura, from a double-blind crossover study. |
| [27329280](https://pubmed.ncbi.nlm.nih.gov/27329280/) | 2016 | RCT | Headache | TEENZ study (NCT01211145). Zolmitriptan nasal spray in adolescents aged 12–17 with acute migraine. Primary outcome was pain-free status at 2 hours. |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | Randomised study | Cephalalgia | 36 patients with and without aura and early allodynia, randomised to six triptan groups. Early treatment effects on pain and allodynia were compared. |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis | J Headache Pain | Frovatriptan vs rizatriptan, zolmitriptan and almotriptan in migraine with aura. Triptans are likely not efficacious when taken during the aura phase. |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies in adults. |
| [10473025](https://pubmed.ncbi.nlm.nih.gov/10473025/) | 1999 | Review | Drugs | Zolmitriptan in migraine. Placebo-controlled trials show rapid onset, with headache relief seen at 45 minutes. |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Review | Expert Opin Pharmacother | Zolmitriptan's clinical applications in migraine. Good 2-hour response and pain-free rates, and improvement in associated symptoms. |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Front Neurol | Treatment options in vestibular migraine. Specialised randomised trials are scarce. |
| [17177580](https://pubmed.ncbi.nlm.nih.gov/17177580/) | 2007 | Observational | Clin Drug Investig | Postmarketing surveillance of zolmitriptan 5 mg nasal spray, covering real-world effectiveness and satisfaction. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA205074 | Zolmitriptan | Orally disintegrating tablet | Alembic Pharmaceuticals Inc. |
| NDA021450 | ZOMIG | Metered spray | Amneal Pharmaceuticals LLC |
| ANDA202890 | Zolmitriptan | Orally disintegrating tablet | Zydus Pharmaceuticals USA Inc. |
| ANDA202560 | Zolmitriptan | Orally disintegrating tablet | Glenmark Pharmaceuticals Inc., USA |

Other dosage forms on the US market include tablets, film-coated tablets, and nasal spray. Approved-indication text was not provided in the license records.

---

## Safety Considerations

- **Subtype-specific concern**: Triptans have traditionally been used cautiously in patients with brainstem or basilar symptoms because of vasoconstriction concerns. Clinical safety in this subtype needs a separate review before any recommendation.

No other safety data were available (no warnings, contraindications, or drug interaction records). Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. There are no trials, and no retrieved study evaluates zolmitriptan in brainstem aura patients. A subtype-specific vasoconstriction safety concern remains unresolved, and the package insert safety data are missing, which blocks safety screening. The evidence is a research question, not a repurposing signal.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, obtained and parsed
- A focused review of triptan safety in brainstem aura and basilar-type migraine, including vasoconstriction risk
- Structured mechanism-of-action data (for example, from DrugBank)
- Clinical studies or case series specific to migraine with brainstem aura

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

