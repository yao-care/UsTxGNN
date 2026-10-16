---
layout: default
title: Ciprofloxacin
parent: Moderate Evidence (L3-L4)
nav_order: 531
evidence_level: L4
indication_count: 10
monitor_inn: "CIPROFLOXACIN"
predicted_indications: ["diffuse scleroderma", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Ciprofloxacin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Ciprofloxacin is a fluoroquinolone antibiotic, originally used for bacterial infections such as typhoid fever, bacterial pneumonia, anthrax, and infectious diarrhoea.
The TxGNN model predicts it may be effective for **diffuse scleroderma** (score 99.87%), but there are **no registered clinical trials** and only **2 publications**, both indirect or exploratory, supporting this direction. The evidence is model-driven and weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (typhoid fever, salmonellosis, bacterial pneumonia, anthrax, Pseudomonas aeruginosa infection, dysentery, shigellosis, among others) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (all licences cancelled) |
| Number of NDAs | 8 (1 NDA, 7 ANDAs; all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Ciprofloxacin is a fluoroquinolone antibacterial, a class generally known to inhibit bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial infections is well established.

The link to diffuse scleroderma is indirect and runs along two possible routes:

1. **Antifibrotic effect on skin.** An exploratory study (PMID 20507401) examined whether oral ciprofloxacin reduces the severity of scleroderma, a fibrosing autoimmune connective tissue disease.
2. **Gastrointestinal complications.** Small bowel bacterial overgrowth is common in systemic sclerosis and can cause diarrhoea and malabsorption. An antibiotic could plausibly help here. However, the one paper retrieved (PMID 7728404) focuses on detecting overgrowth rather than showing a treatment effect.

The very high TxGNN score is not backed by clinical data. At present this is a hypothesis rather than a validated repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Exploratory antifibrotic skin study | The Journal of Dermatology | Tested whether oral ciprofloxacin reduces scleroderma severity as an antifibrotic, using a controlled, double-blind randomised design per the abstract. The abstract available to us was truncated, so results are not confirmed. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Diagnostic / cohort | British Journal of Rheumatology | 24 systemic sclerosis patients with malabsorption symptoms were assessed for small bowel bacterial overgrowth, with treatment outcomes reported. It mainly addresses detection, not a clear ciprofloxacin effect. |

## US Market Information

All eight US authorisations are cancelled, and none has approved-indication text on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA077859 | Ciprofloxacin (Medsource Pharmaceuticals) | Tablet, film coated | Not recorded |
| ANDA076639 | Ciprofloxacin (Coupler LLC) | Tablet | Not recorded |
| ANDA076593 | Ciprofloxacin Hydrochloride (Westminster Pharmaceuticals) | Tablet, film coated | Not recorded |
| ANDA076558 | Ciprofloxacin (Bryant Ranch Prepack) | Tablet, film coated | Not recorded |
| ANDA208921 | Ciprofloxacin (Bryant Ranch Prepack) | Tablet | Not recorded |

Three further cancelled licences are not shown: ANDA076126 (Carlsbad Technology), NDA019992 (Proficient Rx, solution/drops), and ANDA075939 (Amneal).

## Safety Considerations

Safety information is based on drug-disease relationships from a knowledge graph, not package insert text, and should be confirmed against the label.

- **Conditions flagged as contraindicated in the knowledge graph:**
  - Cardiac: long QT syndrome (including familial), torsades de pointes
  - Neurological: epilepsy, peripheral neuropathy and other peripheral nervous system disease, myasthenia gravis and other neuromuscular junction disease
  - Tendon and joint: tendinitis, periarthritis, Achilles bursitis, heel spur, exostosis
  - Renal and metabolic: kidney disease, pyoureter, potassium deficiency
  - Gastrointestinal: *Clostridium difficile* colitis, perinatal necrotising enterocolitis
  - Other: superimposed infection
- **Drug interactions:** 100 interactions were found. The ones listed include several rated **Major**: hydrocortisone, triamcinolone, dexamethasone, betamethasone (corticosteroids), and bupropion. Many are rated Moderate, including acarbose, metformin, pioglitazone, alogliptin, albiglutide, famotidine, loperamide, alosetron, aprepitant, aspirin, balsalazide, bisacodyl, calcium phosphate, and budesonide.
- **Points relevant to scleroderma:** Corticosteroids are commonly used in scleroderma, and the major interaction with them (together with the tendon-related contraindications) is a particular concern. Scleroderma patients may also have gastrointestinal and neuromuscular involvement, overlapping with flagged conditions.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no clinical trials exist, the supporting literature is exploratory or indirect, and the safety profile (tendon, neuropathy, QT, and corticosteroid interaction concerns) is not favourable for a chronic autoimmune fibrosing disease. Other predicted indications on the list, such as plague, rest on stronger evidence, but they largely extend the existing antibacterial use rather than representing true repurposing.

**To proceed, the following is needed:**
- Full-text review of PMID 20507401 to confirm design, sample size, and outcomes
- Mechanism-of-action data and a plausible antifibrotic pathway
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Clinical evidence for ciprofloxacin in systemic sclerosis small bowel bacterial overgrowth, in comparison with other antibiotics
- A benefit-risk assessment, given the tendon, neuropathy, QT, and corticosteroid interaction risks
- A decision on whether a re-listed US product is available, as all current licences are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

