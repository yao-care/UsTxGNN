---
layout: default
title: Dipyridamole
parent: Moderate Evidence (L3-L4)
nav_order: 613
evidence_level: L4
indication_count: 10
---

# Dipyridamole
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

# Dipyridamole: From Antiplatelet Use to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is an established antiplatelet and vasodilator agent that is marketed in the United States as tablets and injection.
The TxGNN model predicts it may be effective for **Prinzmetal angina** (coronary vasospasm), with a very high score of 99.99%.
However, there are **0 clinical trials** and only **14 publications**, and none of these publications shows a therapeutic benefit. Most describe dipyridamole as a cardiac stress-test agent, and one raises a possible safety concern.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, dipyridamole is an antiplatelet and vasodilating agent. It is thought to raise extracellular adenosine by blocking its reuptake (ENT1) and to inhibit phosphodiesterase.

On paper, a vasodilator might seem relevant to a vasospastic angina disorder. In practice, this is not a recognized anti-vasospastic mechanism, and the very high TxGNN score is not backed by clinical data. Most of the retrieved papers concern dipyridamole as a diagnostic stress agent. One report (PMID 3421166) links dipyridamole stress testing, and the sudden withdrawal of its effect with aminophylline, to coronary vasospasm in variant angina. That is a potential **safety signal**, not evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Clinical review | Japanese Circulation Journal | 26 patients with rest angina (13 with Prinzmetal's variant) were given several drugs, including dipyridamole 50 mg. Propranolol did not suppress attacks and tended to aggravate them. The abstract is truncated, so the dipyridamole result is not visible. |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Case report | Am J Cardiol | Tested whether aminophylline, given to end dipyridamole stress, can trigger coronary vasospasm in variant angina. Points to a possible spasm-provoking safety signal. |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Cohort | Br Heart J | 25 patients with exercise-induced ST elevation were tested for reproducibility, and their responses to the dipyridamole echo test were compared. Diagnostic focus. |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Diagnostic study | Jpn Circ J | Dipyridamole-loading thallium-201 imaging had 66% diagnostic accuracy for coronary artery disease. Combined with exercise, sensitivity rose from 71% to 87%. |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Cohort | Zhonghua Xin Xue Guan Bing Za Zhi | Compared clinical features of typical vs atypical coronary artery spasm. The abstract states only the aim, with no results. |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Cohort | Rev Port Cardiol | Assessed the 3-year prognosis of patients with a normal thallium-dipyridamole scan. Diagnostic and prognostic use. |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Diagnostic study | J Am Coll Cardiol | Studied increased echodensity of transiently asynergic myocardium as an echocardiographic sign of ischemia, including ischemia induced by different mechanisms. |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | Reviews the pathophysiology behind noninvasive functional tests of coronary stenosis, including the dipyridamole stress test. |
| [6125623](https://pubmed.ncbi.nlm.nih.gov/6125623/) | 1982 | Review | Kardiologiia | Review of diagnostic and treatment problems in angina. No abstract available. |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Case report | Clin Nucl Med | Single patient with migraine, asthma and variant angina who showed scintigraphic ischemia during stress testing. Discusses "cardiac migraine". |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA040874 | Dipyridamole | Tablet, film coated | Zydus Pharmaceuticals USA Inc. |
| ANDA040542 | Dipyridamole | Tablet, film coated | Oxford Pharmaceuticals, LLC |
| ANDA074521 | Dipyridamole | Injection | Henry Schein, Inc. |
| ANDA074521 | Dipyridamole | Injection | HF Acquisition Co LLC, DBA HealthFirst |

Across all 20 authorizations, the listed dosage forms are film-coated tablet, tablet, capsule, extended-release capsule, and injection. The source data does not give approved indication text for these products.

---

## Safety Considerations

- **Literature signal (not a labeled warning)**: PMID 3421166 links dipyridamole stress testing, and its reversal with aminophylline, to coronary vasospasm in variant angina. Because dipyridamole raises adenosine, coronary steal and slowed sinus or AV node conduction are also theoretical concerns.

Please refer to the package insert for warnings, contraindications and drug interaction information. None is available in the source record.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. There are no registered trials, and none of the retrieved literature shows therapeutic benefit in Prinzmetal angina. The only spasm-related finding points to a possible safety concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example, from DrugBank), plus a clear rationale for a benefit in vasospasm
- Original approved indication text for the US products
- Controlled clinical evidence in Prinzmetal angina, with attention to the vasospasm safety signal

The same evidence pack shows stronger support for dipyridamole in stroke and TIA secondary prevention (large Phase 4 trials such as ESPRIT and PRoFESS, and Cochrane reviews). That is likely an already-established use rather than true repurposing, and should be checked against local labeling.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

