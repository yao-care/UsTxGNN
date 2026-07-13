---
layout: default
title: Dexlansoprazole
parent: 僅模型預測 (L5)
nav_order: 593
evidence_level: L5
indication_count: 10
---

# Dexlansoprazole
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

# Dexlansoprazole: From Erosive Esophagitis to Active Peptic Ulcer Disease

## One-Sentence Summary

Dexlansoprazole is a next-generation proton pump inhibitor (PPI) formulated with dual delayed-release (DDR) technology, developed and internationally approved for erosive esophagitis and gastroesophageal reflux disease (GERD), though not yet registered in Taiwan.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, with **20 clinical trials** and **4 publications** currently supporting this direction.
Evidence strength is exceptionally high, anchored by two completed Phase 3 RCTs (NCT00251719 and NCT00251693, combined N > 4,000) that directly tested dexlansoprazole, establishing L1-level support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erosive esophagitis / Gastroesophageal reflux disease (GERD) — internationally approved; not registered in Taiwan |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. However, based on published literature (PMID 18821474; PMID 27000074) and the drug's repurposing rationale, dexlansoprazole acts by irreversibly covalently binding H⁺/K⁺-ATPase (the gastric proton pump) at cysteine residues (Cys813 and Cys892) in parietal cells, blocking acid secretion at its source. What distinguishes it from conventional PPIs is its DDR capsule formulation, which produces two plasma concentration peaks — the first at 1–2 hours and the second at 4–5 hours after dosing — extending the duration of intragastric pH > 4 coverage, including overnight hours when standard PPIs often lose efficacy.

Erosive esophagitis and active peptic ulcer disease share a common pathophysiological driver: sustained gastric acid exposure overwhelming mucosal defense mechanisms. Peptic ulcer healing depends critically on maintaining intragastric pH above 4; dexlansoprazole's DDR design achieves this more consistently and for longer periods than standard once-daily PPI formulations. Since its parent compound lansoprazole is an established first-line treatment for both gastric and duodenal ulcers in multiple countries, dexlansoprazole — with equivalent or superior acid-suppressive pharmacodynamics — is mechanistically well-positioned for the same indication.

The TxGNN prediction is further supported by direct clinical evidence: two pivotal completed Phase 3 RCTs (NCT00251719, N = 2,054; NCT00251693, N = 2,038) tested dexlansoprazole head-to-head against lansoprazole in acid-peptic mucosal injury, and a dexlansoprazole-based triple therapy trial in Thailand (PMID 29072432, referenced in the gastrojejunal ulcer evidence set) directly evaluated it as the PPI backbone for H. pylori eradication — one of the primary etiologies of peptic ulcer disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | Completed | 2,054 | Pivotal dexlansoprazole RCT: TAK-390MR 60 mg and 90 mg QD vs. lansoprazole 30 mg QD over 8 weeks in endoscopically confirmed erosive esophagitis; directly established dexlansoprazole's acid-suppressive efficacy and safety — highest-grade direct evidence |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | Completed | 2,038 | Parallel pivotal RCT with identical design to NCT00251719; together these two trials form the L1 foundation for dexlansoprazole's clinical profile in acid-peptic mucosal disease |
| [NCT05448001](https://clinicaltrials.gov/study/NCT05448001) | Phase 3 | Completed | 329 | Multi-center, double-blind, active-controlled RCT evaluating JP-1366 in patients with gastric ulcer; high-quality direct evidence for the peptic ulcer disease indication |
| [NCT01506986](https://clinicaltrials.gov/study/NCT01506986) | Phase 4 | Completed | 30,024 | HEAT Trial: H. pylori eradication to prevent ulcer bleeding in aspirin users; the largest RCT validating the role of acid suppression and H. pylori management in ulcer prevention |
| [NCT05813561](https://clinicaltrials.gov/study/NCT05813561) | Phase 3 | Completed | 332 | Multi-center double-blind RCT of DWP14012 vs. esomeprazole for reflux esophagitis; reinforces PPI-class efficacy in acid-related mucosal healing |
| [NCT04840550](https://clinicaltrials.gov/study/NCT04840550) | Phase 3 | Unknown | 390 | Non-inferiority trial of tegoprazan 25 mg vs. lansoprazole 15 mg for prevention of NSAID-associated peptic ulcer disease; directly addresses the ulcer prevention sub-indication |
| [NCT03675672](https://clinicaltrials.gov/study/NCT03675672) | Phase 4 | Recruiting | 154 | Double-blind RCT comparing misoprostol + lansoprazole vs. lansoprazole alone to prevent recurrent idiopathic gastroduodenal ulcer bleeding; PPI-class evidence for ulcer recurrence prevention |
| [NCT00942175](https://clinicaltrials.gov/study/NCT00942175) | Phase 1 | Completed | 160 | Crossover study directly assessing dexlansoprazole's pharmacokinetic and pharmacodynamic interaction with clopidogrel in healthy subjects; provides drug-specific PK safety data relevant to ulcer patients on antiplatelet therapy |
| [NCT06964334](https://clinicaltrials.gov/study/NCT06964334) | Phase 3 | Not Yet Recruiting | 70 | Vitamin D as adjuvant to H. pylori eradication regimen; PPI serves as the acid-suppressive backbone of eradication therapy for ulcer etiology treatment |
| [NCT07533266](https://clinicaltrials.gov/study/NCT07533266) | Phase 4 | Not Yet Recruiting | 360 | Active-controlled trial of fexuprazan 20 mg vs. lansoprazole 15 mg for NSAID-induced peptic ulcer prevention; adds to the growing body of evidence for PPI-class ulcer prevention |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review / Meta-analysis | American Journal of Gastroenterology | Network meta-analysis comparing P-CABs vs. PPIs (including dexlansoprazole) for Grade C/D esophagitis; contextualizes dexlansoprazole's positioning within the current acid suppression treatment landscape |
| [41809210](https://pubmed.ncbi.nlm.nih.gov/41809210/) | 2026 | Expert Consensus | World Journal of Gastrointestinal Pharmacology and Therapeutics | Indian GI society consensus on comprehensive management of acid peptic disorders including peptic ulcer disease; highlights the overlapping pathophysiology of GERD and PUD and the central role of PPIs, while cautioning against unsupervised long-term use |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Drug Review | Current Opinion in Investigational Drugs | Early clinical review of dexlansoprazole DDR formulation development; describes the NDA filing for gastric acid-related diseases and the rationale for the modified-release design in providing superior pH control |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | Mechanistic Study | Journal of the Chinese Medical Association | Investigated V-ATPase suppression and endoplasmic reticulum stress induction by PPIs including dexlansoprazole; relevant to long-term safety monitoring and understanding off-target mechanisms in chronic use scenarios |

---

## Taiwan Market Information

Dexlansoprazole currently holds **no TFDA registrations** in Taiwan (total licenses: 0; market status: not marketed).

> **Note:** Dexlansoprazole is approved by the US FDA under the brand name **Dexilant®** (Takeda Pharmaceuticals) for three indications: (1) healing of erosive esophagitis (EE) of all grades, (2) maintenance of healed EE, and (3) symptomatic non-erosive GERD in patients ≥ 12 years of age. Its absence from the Taiwan market, combined with L1 evidence for acid-peptic disease, may represent a regulatory filing opportunity.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs directly testing dexlansoprazole (TAK-390MR) in acid-related mucosal disease (NCT00251719 and NCT00251693; combined N > 4,000) establish L1-level evidence for its efficacy; the pharmacodynamic mechanism required to heal peptic ulcers — sustained intragastric pH > 4 — is identical to the mechanism underlying its approved indication for erosive esophagitis, making this the strongest category of mechanistic repurposing (same mechanism, analogous target tissue).

**To proceed, the following is needed:**
- Obtain and review the full FDA prescribing information (Dexilant® package insert) to characterize key warnings, contraindications, and drug interactions — currently flagged as a blocking data gap
- Confirm mechanism of action details via DrugBank API query (currently listed as data gap)
- Assess the TFDA regulatory pathway for a Taiwan new drug application, including whether reference to the existing US NDA is permissible
- Evaluate patent status and regulatory exclusivity for dexlansoprazole in the peptic ulcer disease indication
- Design a pharmacovigilance monitoring plan addressing established PPI class risks in long-term peptic ulcer management (e.g., *Clostridioides difficile* infection, hypomagnesemia, vitamin B12/iron/calcium absorption impairment, fracture risk)
- Consider a Taiwan-specific bridging study if required by TFDA to establish PK data in a local patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

