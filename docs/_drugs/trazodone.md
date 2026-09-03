---
layout: default
title: Trazodone
parent: 僅模型預測 (L5)
nav_order: 1254
evidence_level: L5
indication_count: 10
---

# Trazodone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Trazodone: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Trazodone is a serotonin antagonist and reuptake inhibitor (SARI) originally developed and marketed for major depressive disorder.
The TxGNN model predicts it may also be effective for **Obsessive-Compulsive Disorder (OCD)**,
with **1 historical placebo-controlled RCT** and **19 supporting publications** (mostly older case reports, cohorts, and reviews), but no currently registered clinical trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (per literature: trazodone is "an antidepressant that is FDA-approved for the treatment of depression") |
| Predicted New Indication | Obsessive-Compulsive Disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for trazodone is not available in the current evidence pack. Based on information extracted from the supporting literature, trazodone acts primarily as a 5-HT2A/5-HT2C receptor antagonist combined with weak serotonin transporter (SERT) inhibition — a pharmacological class known as a Serotonin Antagonist and Reuptake Inhibitor (SARI). This distinguishes it from classical SSRIs, though it still modulates central serotonergic tone.

OCD is understood to involve dysregulation of the cortico-striato-thalamic circuit, with serotonin playing a central pathophysiological role — this is the basis for OCD's well-established preferential response to serotonin reuptake inhibitors (SRIs) such as clomipramine, fluoxetine, fluvoxamine, and paroxetine. Because trazodone also engages the serotonergic system, a mechanistic rationale for anti-obsessional activity exists, and this is reflected in decades of case reports and small trials exploring trazodone as an adjunct or alternative in SRI-refractory OCD.

However, the mechanistic link is not strong or consistent. The bulk of the literature (case reports, small cohorts, one PET-imaging correlation study) positions trazodone as a second-line or augmentation option for patients who have failed clomipramine/SSRIs, not as a primary evidence-based treatment. The only controlled trial identified — a double-blind, placebo-controlled study (Pigott et al., 1992) — investigated trazodone's antiobsessional efficacy directly, but does not by itself establish robust efficacy. Overall, the biological plausibility is reasonable but the clinical evidence base remains thin and dated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | RCT | J Clin Psychopharmacol | Double-blind, placebo-controlled trial evaluating trazodone's serotonin-reuptake-inhibiting properties as a potential antiobsessional treatment in OCD patients, following earlier positive case reports and open trials. |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Review | Postgrad Med | Review of trazodone's mechanism, formulation, dosage, and adverse effects, summarizing its use in approved (MDD) and non-FDA-approved conditions including OCD. |
| [8993077](https://pubmed.ncbi.nlm.nih.gov/8993077/) | 1996 | Review | Psychopharmacol Bull | Reviews mono- and polypharmacotherapy of OCD; notes OCD as a diagnosis responds almost exclusively to serotonin reuptake inhibitors (SRIs). |
| [8134850](https://pubmed.ncbi.nlm.nih.gov/8134850/) | 1994 | Review | South Med J | Reviews pharmacologic management of OCD, discussing the serotonin/dopamine dysregulation hypothesis underlying SRI-based treatment. |
| [8331098](https://pubmed.ncbi.nlm.nih.gov/8331098/) | 1993 | Review | J Clin Psychiatry | Reviews biological approaches to treatment-resistant OCD, including augmentation of SRIs with other serotonergic agents. |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | Cohort | Clin Neuropharmacol | Trazodone given to 9 clomipramine/lithium-resistant OCD patients; group showed mild but significant improvement, with 3 patients responding favorably and relapsing on drug withdrawal. |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | Cohort | Psychopathology | PET study showing trazodone-associated OCD symptom improvement correlated with changes in caudate nucleus glucose metabolism. |
| [6703152](https://pubmed.ncbi.nlm.nih.gov/6703152/) | 1984 | Case Report | Am J Psychiatry | Early case report describing trazodone use in obsessive-compulsive disorder. |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | Case Report | J Nerv Ment Dis | Two treatment-refractory patients with OCD and comorbid depression showed rapid improvement in both symptom domains on trazodone. |
| [29343875](https://pubmed.ncbi.nlm.nih.gov/29343875/) | 2017 | Case Report | Riv Psichiatr | Prolonged-release trazodone used to treat the depressive phase in a patient with bipolar II disorder and comorbid OCD. |

---

## US Market Information

Trazodone currently has **no registered NDA and is not marketed** under this profile (Market Status: Not Marketed; Total Licenses: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed key warnings, contraindications, and drug-drug interaction data are not available in the current evidence pack (flagged as a Blocking data gap: TFDA/FDA label warnings and contraindications have not yet been retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only controlled trial (Pigott et al., 1992) is small, decades old, and does not provide a robust efficacy signal; the remaining evidence consists largely of dated case reports, small cohorts, and reviews. Combined with the absence of any current marketing authorization, MOA data, or safety/DDI information, the evidence base is insufficient to move beyond a research question at this stage.

**To proceed, the following is needed:**
- Retrieval of official label warnings and contraindications (DG001, Blocking) before any S1 safety review can proceed
- Confirmed mechanism-of-action data from DrugBank or equivalent source (DG002)
- A modern, adequately powered RCT or systematic review replicating/updating the 1992 trial in OCD
- Drug-drug interaction data, particularly relevant given trazodone's known serotonergic and CYP3A4-related interaction potential in current SRI/SSRI-treated OCD populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

