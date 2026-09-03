---
layout: default
title: Polidocanol
parent: 僅模型預測 (L5)
nav_order: 1059
evidence_level: L5
indication_count: 10
---

# Polidocanol
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

# Polidocanol: From Varicose Vein Sclerotherapy to Esophageal Variceal Bleeding

## One-Sentence Summary

> Polidocanol is a surfactant-type sclerosing agent internationally established for treating varicose and spider veins.
> The TxGNN model predicts it may be effective for **Esophageal Varices with Bleeding**,
> with **7 clinical trials** (including one completed Phase 3 RCT) and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Taiwan license registry (0 licenses on file). Per supporting literature in this evidence pack, polidocanol's internationally recognized approved use is sclerotherapy of varicose veins and spider veins (telangiectasia). |
| Predicted New Indication | Esophageal Varices with Bleeding |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for polidocanol is not on file in this evidence pack (flagged as a High-severity data gap, DG002). However, based on well-established pharmacology reflected in the supporting evidence, polidocanol is a surfactant-type sclerosing agent. When injected into or around a blood vessel, it damages the vascular endothelium, triggers local thrombus formation, and induces fibrosis — the mechanism that closes off the target vessel. This is precisely the working principle of endoscopic injection sclerotherapy (EIS), a technique that has been used for decades to control bleeding from esophageal varices in patients with portal hypertension.

The relationship between the original indication (peripheral venous sclerotherapy for varicose/spider veins) and the predicted new indication (esophageal variceal bleeding) is therefore not a novel hypothesis but an extension of the same sclerosant mechanism to a different vascular bed — dilated esophageal submucosal veins instead of superficial leg veins. A dedicated review in the evidence pack, *"An Evidence-Based Review of Off-Label Uses of Polidocanol"* (PMID 29473522), explicitly notes that polidocanol's off-label applications beyond varicose veins remain underappreciated, reinforcing that this repurposing direction is grounded in known pharmacology rather than a pure data-driven artifact.

Under its international synonym **Lauromacrogol**, polidocanol injection has already been directly studied in randomized controlled trials for esophageal and gastric varices (e.g., NCT02361593, NCT01923064), and a completed Phase 3 RCT (NCT00161915) compared polidocanol-based sclerotherapy against ligation/fibrin sealant for hemostasis in bleeding esophageal varices. This gives the TxGNN prediction meaningful mechanistic and clinical-trial corroboration, even though it falls short of being a novel discovery — it largely reflects existing off-label/regional clinical practice (particularly in Asia, where lauromacrogol sclerotherapy is common).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02361593](https://clinicaltrials.gov/study/NCT02361593) | NA | Completed | 120 | RCT of transparent cap-assisted endoscopic sclerotherapy with lauromacrogol (polidocanol) injection for esophageal varices — direct evidence. |
| [NCT00161915](https://clinicaltrials.gov/study/NCT00161915) | Phase 3 | Completed | N/A | RCT comparing fibrin sealant vs. ligature (± polidocanol) for hemostasis and rebleeding prophylaxis in bleeding esophageal varices. |
| [NCT01923064](https://clinicaltrials.gov/study/NCT01923064) | NA | Completed | 96 | RCT comparing cyanoacrylate+lipiodol vs. cyanoacrylate+lauromacrogol injection for gastric varices. |
| [NCT02468206](https://clinicaltrials.gov/study/NCT02468206) | NA | Completed | 64 | Endoscopic cyanoacrylate vs. BRTO for prevention of gastric variceal rebleeding (indirect comparator study, not polidocanol-based). |
| [NCT05500625](https://clinicaltrials.gov/study/NCT05500625) | NA | Unknown | 70 | EUS-guided coil + cyanoacrylate vs. BRTO for gastric varices (indirect, non-polidocanol). |
| [NCT02468167](https://clinicaltrials.gov/study/NCT02468167) | NA | Unknown | 70 | Cyanoacrylate vs. BRTO for acute gastric variceal bleeding (indirect, non-polidocanol). |
| [NCT02468180](https://clinicaltrials.gov/study/NCT02468180) | NA | Unknown | 70 | Cyanoacrylate vs. BRTO for primary prophylaxis of gastric variceal bleeding (indirect, non-polidocanol). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9255525](https://pubmed.ncbi.nlm.nih.gov/9255525/) | 1997 | RCT | Endoscopy | Prospective study of cyanoacrylate + polidocanol vs. polidocanol alone in unselected cirrhotic patients with bleeding esophageal varices. |
| [32517718](https://pubmed.ncbi.nlm.nih.gov/32517718/) | 2020 | Review | BMC Gastroenterology | Systematic review and pooled analysis of rebleeding risk after cyanoacrylate-based treatment of gastroesophageal varices. |
| [30170340](https://pubmed.ncbi.nlm.nih.gov/30170340/) | 2019 | Review | J Gastroenterol Hepatol | Review of balloon-occluded retrograde transvenous obliteration (BRTO), including sclerosant evolution for gastric varices. |
| [29473522](https://pubmed.ncbi.nlm.nih.gov/29473522/) | 2017 | Review | Curr Clin Pharmacol | Evidence-based review of off-label uses of polidocanol beyond varicose/spider vein treatment. |
| [36509625](https://pubmed.ncbi.nlm.nih.gov/36509625/) | 2023 | Case series | Archives de Pédiatrie | Endoscopic sclerotherapy with polidocanol for cardiac varices in children/adolescents. |
| [33731585](https://pubmed.ncbi.nlm.nih.gov/33731585/) | 2021 | Cohort/Review | Eur J Gastroenterol Hepatol | Complications and risk factors of elective cyanoacrylate + lauromacrogol injection for gastric varices. |
| [35879573](https://pubmed.ncbi.nlm.nih.gov/35879573/) | 2022 | Cohort (RCT design) | Surgical Endoscopy | Novel balloon compression-assisted endoscopic injection sclerotherapy vs. ligation for esophageal varices. |
| [2358974](https://pubmed.ncbi.nlm.nih.gov/2358974/) | 1990 | Case series | J Pediatr Gastroenterol Nutr | Endoscopic sclerotherapy (including ethoxysclerol/polidocanol-class agents) in children with bleeding esophageal varices. |
| [1778718](https://pubmed.ncbi.nlm.nih.gov/1778718/) | 1991 | Case report | International Surgery | Report on fatal gastric bleeding following endoscopic injection sclerotherapy for esophageal varices. |
| [35898831](https://pubmed.ncbi.nlm.nih.gov/35898831/) | 2023 | Case series | DEN Open | Management of esophageal varices during endoscopic submucosal dissection for esophageal cancer. |

---

## US Market Information

Polidocanol currently has **no marketing authorization on file** in this evidence pack (Market status: Not Marketed; 0 licenses recorded). No product name, dosage form, or approved-indication text is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug–drug interaction data were not available in this evidence pack — flagged as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis is well established (sclerosant-induced endothelial injury/thrombosis/fibrosis underlying decades of clinical EIS practice), and one completed Phase 3 RCT plus multiple direct polidocanol/lauromacrogol trials support efficacy in bleeding esophageal varices — meeting L2 evidence criteria. However, the drug has no marketing authorization on file and no formal safety/MOA documentation in this jurisdiction, so guardrails are required before any clinical application.

**To proceed, the following is needed:**
- TFDA package insert / label (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Formal review of local approval pathway, given zero existing licenses
- Note: secondary prediction "esophageal varices without bleeding" (L3, Research Question stage) has weaker support — guideline-preferred prophylaxis is beta-blockers/ligation, not sclerotherapy
- Note: ranks 3–10 (e.g., monosomy X, cone dystrophy, retinal disorders) are flagged in the evidence pack itself as likely knowledge-graph noise with no mechanistic plausibility or supporting literature — recommend **Hold**, no further action
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

